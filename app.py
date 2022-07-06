import json
import http.client
from threading import Thread
import threading
from chalice import Chalice, Response
from woocommerce import API
import razorpay
import datetime
from urllib.parse import parse_qs
import asyncio
app = Chalice(app_name='webhooks')

def background(f):
    '''
    a threading decorator
    use @background above the function you want to run in the background
    '''
    def backgrnd_func(*a, **kw):
        threading.Thread(target=f, args=a, kwargs=kw).start()
    return backgrnd_func
    
@app.route('/pickrr', methods=['GET', 'POST'], content_types=['application/json'])
def shippingUpdates():
    request = app.current_request
    if request.method == 'POST':
        Response(body="Success",
                 status_code=200,
                 headers={'Content-Type': 'text/plain'})
        resp = json.loads(request.raw_body)
        updateType = resp['status']['current_status_type']
        awb = resp['tracking_id']
        remarks = resp['status']['current_status_body']
        if updateType == 'DL' or updateType == 'OO' or updateType == 'RTO' or updateType == 'PP':
            order_id = resp['client_order_id']
            phonenumber, orderkey, name, total, address, payment = getOrderDetails(
                order_id)
            if updateType == 'PP':
                orderPickedUp(order_id, name, awb, phonenumber, orderkey)
            elif updateType == 'DL':
                orderDelivered(order_id, name, phonenumber)
            elif updateType == 'OO':
                orderOFD(order_id, total, phonenumber, payment)
            elif updateType == 'RTO':
                orderRTO(order_id, phonenumber, awb, remarks, name)
    else:
        return Response(body='FAIL!',
                        status_code=500,
                        headers={'Content-Type': 'text/plain'})
        pass


@app.route('/neworder', methods=['GET', 'POST'], content_types=['application/json'])
def newOrder():
    request = app.current_request
    if request.method == 'POST':
        Response(body="Success",
                 status_code=200,
                 headers={'Content-Type': 'text/plain'})
        resp = json.loads(request.raw_body)
        orderStatus = resp['status']
        payment = resp['payment_method']
        if orderStatus == 'processing':
            total = resp['total']
            name = resp['shipping']['first_name'] + \
                " "+resp['shipping']['last_name']
            phonenumber = resp['shipping']['phone']
            phonenumber = ''.join(phonenumber[1:].split(' '))
            email = resp['billing']['email']
            address = resp['shipping']['address_1']+" "+resp['shipping']['address_2']+", " + \
                resp['shipping']['city']+" "+resp['shipping']['state'] + \
                "| "+resp['shipping']['postcode']
            order_id = resp['id']
            orderDate = datetime.datetime.strptime(
                resp['date_created'].split("T")[0], "%Y-%m-%d")
            traits = {
                "name": name, "email": email, "Address": address, "Latest Order": order_id
            }
            createInteraktContact(phonenumber, traits)
            if payment == 'cod':
                newCODorder(orderDate, total, order_id, name,
                            phonenumber, email, address, payment)
            else:
                eventTraits = {"Order Number": order_id, "Total": total, "Name": name,
                               "Email": email, "Payment Method": payment, "Address": address}
                sendInteraktEvent(
                    phonenumber, "New Prepaid Order", eventTraits)
    else:
        return Response(body='FAIL!',
                        status_code=500,
                        headers={'Content-Type': 'text/plain'})
        pass


@app.route('/invoicepaid', methods=['GET', 'POST'], content_types=['application/json'])
def invoicePaid():
    request = app.current_request
    if request.method == 'POST':
        Response(body="Success",
                 status_code=200,
                 headers={'Content-Type': 'text/plain'})
        resp = json.loads(request.raw_body)
        order = resp['payload']['invoice']['entity']['description'].split(
            "#")[-1]
        paymentID = resp['payload']['payment']['entity']['id']
        billing, shipping, line_items, shipping_lines = cancelOrder(order)
        phonenumber = ''.join(billing['phone'][1:].split(' '))
        sendInteraktEvent(phonenumber, "COD to Prepaid", {
                          "Old Order Number": order, "Payment ID": paymentID})
        createNewOrder(billing, shipping, line_items,
                       shipping_lines, paymentID)
    else:
        return Response(body='FAIL!',
                        status_code=500,
                        headers={'Content-Type': 'text/plain'})
        pass


@app.route('/paymentcaptured', methods=['GET', 'POST'], content_types=['application/json'])
def paymentCaptured():
    request = app.current_request
    if request.method == 'POST':
        Response(body="Success",
                 status_code=200,
                 headers={'Content-Type': 'text/plain'})
        resp = json.loads(request.raw_body)
        description = resp['payload']['payment']['entity']['description']
        phonenumber = resp['payload']['payment']['entity']['contact'].split(
            "+91")[-1]
        amount = resp['payload']['payment']['entity']['amount']/100
        paymentID = resp['payload']['payment']['entity']['id']
        createInteraktContact(phonenumber, {"Payment ID": paymentID})
        sendInteraktEvent(phonenumber, "Payment Captured", {
                          "Payment ID": paymentID, "Amount": amount, "Description": description})
    else:
        return Response(body='FAIL!',
                        status_code=500,
                        headers={'Content-Type': 'text/plain'})
        pass




@app.route('/popupform', methods=['GET', 'POST'], content_types=['application/x-www-form-urlencoded'])
def popUpForm():
    popUp(app.current_request)
    return Response(body="Success",
                    status_code=200,
                    headers={'Content-Type': 'text/plain'})
@background
def popUp(request):
    if request.method == 'POST':
        resp = parse_qs(request.raw_body.decode())
        print("Request: ", request.raw_body)
        print("Type: ", type(request.raw_body))
        print("Decoded: ", request.raw_body.decode())
        print("Parsed: ", resp)
        try:
            product = resp['Product'][0]
        except KeyError:
            product = ""
        try:
            name = resp['Name'][0]
        except KeyError:
            name = ""
        phonenumber = str(resp['Phone'][0])
        phonenumber = phonenumber[-10:] if len(
            phonenumber) > 10 else phonenumber
        request = (json.dumps({
            "name": name,
            "phonenumber": phonenumber,
            "product": product}))
        conn = http.client.HTTPSConnection(
            "huqvx7dth4.execute-api.ap-south-1.amazonaws.com")
        headers = {
            'Content-Type': 'application/json'
        }
        conn.request("POST", "/api", request, headers)
        res = conn.getresponse()
        data = res.read()
        url, product, total, discountedPrice = getCartURL(product)
        print(data.decode("utf-8"))
        createInteraktContact(phonenumber, {
            "Name": name, "Cart URL": url, "Product": product, "Total": total, "Discounted Price": discountedPrice})
        sendInteraktEvent(phonenumber, "Coupon code Pop Up filled", {
            "Name": name, "Cart URL": url, "Product": product, "Total": total, "Discounted Price": discountedPrice})

def woocommerce_api_client():
    woocommerce = API(
        url='https://www.dharishahayurveda.com',
        consumer_key='ck_e3f107055ebf4d93d244aded86ed5320eb6a30c2',
        consumer_secret='cs_e9e9937b4617cb99e25be4e1fa11fde08e8551fc',
        version='wc/v3',
        timeout=10
    )
    return woocommerce


def getCartURL(product):
    woocommerce = woocommerce_api_client()
    try:
        product = woocommerce.get(
            "products", params={'search': product}).json()[0]
        name = ''.join(product['name'].split('-')[:2])
        mrp = product['regular_price']
        total = int(mrp)*3
        finalPrice = total/2
        id = product['id']
        url = "https://www.dharishahayurveda.com/cart/?alg_apply_coupon=FULLCOURSE&add-to-cart=" + \
            str(id)+"&quantity=3"
        shortURL = firebaseLinkShortner(url)
    except IndexError:
        name = "Product"
        total = "1000"
        finalPrice = "500"
        shortURL = "https://www.dharishahayurveda.com/shop/"
    return (shortURL, name, total, finalPrice)


def cancelOrder(orderID):
    data = {
        "status": "converted"
    }
    res = woocommerce_api_client().put("orders/"+str(orderID), data).json()
    return (res['billing'], res['shipping'], res['line_items'], res['shipping_lines'])


def createNewOrder(billing, shipping, line_items, shipping_lines, paymentID):
    items = []
    for i in range(len(line_items)):
        item = line_items[i]
        items.append({'total': str(float(item['total'])*.85), 'subtotal': str(float(item['subtotal'])*.85), 'quantity': item['quantity'],
                     'product_id': item['product_id'], 'tax_class': item['tax_class'], 'variation_id': item['variation_id']})
    for i in range(len(shipping_lines)):
        rem_list = ['id', 'instance_id', 'taxes', 'meta_data']
        [shipping_lines[i].pop(key) for key in rem_list]
    print(shipping_lines)
    data = {
        "payment_method": "razorpay",
        "payment_method_title": "Razor Pay -UPI/Paytm/Cards",
        "transaction_id": paymentID,
        "set_paid": True,
        "billing": billing,
        "shipping": shipping,
        "line_items": items,
        "shipping_lines": shipping_lines
    }
    print(woocommerce_api_client().post("orders", data).json())


def razorpayClient():
    client = razorpay.Client(
        auth=("rzp_live_2rUGsNNlSYgmfS", "EQ8YY2CiWyZdh9zW9cDqT3Uy"))
    client.set_app_details({"name": "Dharishah", "version": "1.0.0"})
    return client


def razorpayCreatePayment(amount, expiry, orderNumber, name, phonenumber):
    res = razorpayClient().payment_link.create({
        "amount": amount,
        "currency": "INR",
        "accept_partial": False,
        "description": "Order #"+str(orderNumber),
        "expire_by": expiry,
        "customer": {
            "name": name,
            "contact": "+91"+str(phonenumber)
        },
        "notify": {
            "sms": False,
            "email": False
        },
        "reminder_enable": False
    })
    return res['short_url']


def createInteraktContact(phonenumber, traits):
    conn = http.client.HTTPSConnection("api.interakt.ai")
    payload = json.dumps(
        {"countryCode": "+91", "phoneNumber": phonenumber, "traits": traits})
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic dEtQUnRmelJvVXU1WXp2OGxZSlNpWW1TRm44TWMteWxVVXkyY1dwM0lwczo='
    }
    conn.request("POST", "/v1/public/track/users/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data


def newCODorder(orderDate, total, order_id, name, phonenumber, email, address, payment):
    orderWeekday = orderDate.weekday()
    expiry = orderDate + \
        datetime.timedelta(
            days=2) if orderWeekday == 6 else orderDate + datetime.timedelta(days=1)
    expiry = expiry.replace(hour=10, minute=0, second=0, microsecond=0)
    expiry = int(expiry.timestamp())
    discount = round(float(total) * 0.15, 2)
    prepaidTotal = int(float(total)*85)
    paymentLink = razorpayCreatePayment(
        prepaidTotal, expiry, order_id, name, phonenumber)
    paymentURL = paymentLink.split("/")[-1]
    eventTraits = {"Order Number": order_id, "Total": total, "Name": name, "Email": email,
                   "Payment Method": payment, "Address": address, "Discount Available": discount, "Link to Discount": paymentURL}
    sendInteraktEvent(phonenumber, "New COD Order", eventTraits)


def orderPickedUp(order_id, name, awb, phonenumber, orderkey):
    event = "Order Picked Up"
    phone = phonenumber
    url = "https://dharishahayurveda.com/wp-admin/admin-ajax.php?action=generate_wpo_wcpdf&document_type=invoice&order_ids=" + \
        order_id+"&order_key="+orderkey
    traits = {"Order Number": order_id, "Name": name,
              "AWB Number": "/#/?tracking_id="+awb,
              "Order Invoice Link": firebaseLinkShortner(url)
              }
    sendInteraktEvent(phone, event, traits)


def orderDelivered(order_id, name, phonenumber):
    event = "Order Delivered"
    phone = phonenumber
    traits = {"Order Number": order_id,
              "Name": name,
              }
    sendInteraktEvent(phone, event, traits)


def orderOFD(order_id, total, phonenumber, payment):
    event = "Out For Delivery"
    phone = phonenumber
    traits = {"Order Number": order_id,
              "Order Total": total,
              "Payment": payment
              }
    sendInteraktEvent(phone, event, traits)


def orderRTO(order_id, phonenumber, awb, remarks, name):
    print(phonenumber)
    event = "RTO"
    traits = {"Order Number": order_id, "Remarks": remarks}
    template = "rto_pickrr"
    bodyValues = [order_id, name, awb]
    buttonValues = {"0": ["/#/?tracking_id="+awb]}
    sendInteraktEvent(phonenumber, event, traits)
    sendInteraktTemplate(bodyValues, template, buttonValues, "8222075444")


def getOrderDetails(order_id):
    woocommerce = woocommerce_api_client()
    order = woocommerce.get('orders/'+str(order_id)).json()
    phonenumber = ''.join(str(order['billing']['phone'])[1:].split(' '))
    orderkey = order['order_key']
    name = order['shipping']['first_name']+' '+order['shipping']['last_name']
    total = order['total']
    address = order['shipping']['address_1']+' '+order['shipping']['address_2']+' ' + \
        order['shipping']['city']+' '+order['shipping']['state'] + \
        ' '+order['shipping']['postcode']
    payment = order['payment_method']
    return (phonenumber, orderkey, name, total, address, payment)


def firebaseLinkShortner(url):
    conn = http.client.HTTPSConnection("firebasedynamiclinks.googleapis.com")
    payload = json.dumps({
        "dynamicLinkInfo": {
            "domainUriPrefix": "https://dharishah.com",
            "link": url,
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request(
        "POST", "/v1/shortLinks?key=AIzaSyA27ZgjuEeVeiNziAp7urdxWnddYkOs0Dw", payload, headers)
    res = conn.getresponse()
    data = res.read()
    shortLink = json.loads(data)['shortLink']
    return shortLink


def sendInteraktEvent(phonenumber, event, traits):

    conn = http.client.HTTPSConnection("api.interakt.ai")
    payload = json.dumps(
        {"countryCode": "+91", "phoneNumber": phonenumber, "event": event, "traits": traits})
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic dEtQUnRmelJvVXU1WXp2OGxZSlNpWW1TRm44TWMteWxVVXkyY1dwM0lwczo='
    }
    conn.request("POST", "/v1/public/track/events/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    datea = json.loads(data.decode("utf-8"))
    print(datea)
    if(datea["result"] == True):
        return data
    else:
        arr = [(i+": "+str(traits[i])) for i in traits]
        error = [event, 'ERROR: '+str(datea["message"]), 'PHONENUMBER: '+str(
            phonenumber)]+arr[:2]+[arr[-1]]
        sendInteraktTemplate(error, 'errors', {}, "9996900902")


def sendInteraktTemplate(bodyValues, template, buttonValues, phonenumber):
    conn = http.client.HTTPSConnection("api.interakt.ai")
    payload = (json.dumps({
        "countryCode": "+91",
        "phoneNumber": phonenumber,
        "type": "Template",
        "template": {
            "name": template,
            "languageCode": "en",
            "bodyValues": bodyValues,
            "buttonValues": buttonValues
        }
    }
    ))
    headers = {
        'Authorization': 'Basic dEtQUnRmelJvVXU1WXp2OGxZSlNpWW1TRm44TWMteWxVVXkyY1dwM0lwczo=',
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/v1/public/message/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
