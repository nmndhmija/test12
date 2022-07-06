import http.client
import json

conn = http.client.HTTPConnection("127.0.0.1", 8000)
shippmentUpdatePayload = json.dumps({
    "tracking_id": "89539783491",
    "client_order_id": "20952",
    "order_type": "forward",
    "status": {
        "received_by": "SEFE",
        "current_status_body": "Your Order has been successfully Delivered",
        "current_status_type": "RTO",
        "current_status_location": "MADHYA MARG OFFICE",
        "current_status_time": "21 Dec 2016, 15:24"
    },
    "info": {
        "to_city": "CHANDIGARH",
        "to_pincode": "160015",
        "from_pincode": "110042",
        "cod_amount": 312.5,
        "from_city": "NEW DELHI"
    },
    "track_arr": [
        {
            "status_array": [
                {
                    "status_time": "17 Dec 2016, 13:17",
                    "status_body": "Order Placed at Pickrr",
                    "status_location": "NEW DELHI"
                }
            ],
            "status_name": "OP"
        },
        {
            "status_array": [
                {
                    "status_time": "18 Dec 2016, 03:14",
                    "status_body": "Order Picked by Pickrr",
                    "status_location": "NEW DELHI"
                }
            ],
            "status_name": "PP"
        },
        {
            "status_array": [
                {
                    "status_time": "19 Dec 2016, 19:55",
                    "status_body": "SHIPMENT ARRIVED",
                    "status_location": "COD PROCESSING CENTRE III"
                },
                {
                    "status_time": "21 Dec 2016, 09:11",
                    "status_body": "SHIPMENT ARRIVED",
                    "status_location": "MADHYA MARG OFFICE"
                }
            ],
            "status_name": "OT"
        },
        {
            "status_array": [
                {
                    "status_time": "21 Dec 2016, 09:38",
                    "status_body": "SHIPMENT OUT FOR DELIVERY",
                    "status_location": "MADHYA MARG OFFICE"
                }
            ],
            "status_name": "OO"
        },
        {
            "status_array": [
                {
                    "status_time": "21 Dec 2016, 12:24",
                    "status_body": "CONSIGNEE NOT AVAILABLE",
                    "status_location": "MADHYA MARG OFFICE"
                }
            ],
            "status_name": "NDR"
        },
        {
            "status_array": [
                {
                    "status_time": "21 Dec 2016, 14:25",
                    "status_body": "SHIPMENT OUT FOR DELIVERY",
                    "status_location": "MADHYA MARG OFFICE"
                }
            ],
            "status_name": "OO"
        },
        {
            "status_array": [
                {
                    "status_time": "21 Dec 2016, 15:24",
                    "status_body": "SHIPMENT DELIVERED",
                    "status_location": "MADHYA MARG OFFICE"
                }
            ],
            "status_name": "DL"
        }
    ]
})

newOrderPayload = json.dumps({
    "id": 21177,
    "parent_id": 0,
    "status": "processing",
    "currency": "INR",
    "version": "6.6.1",
    "prices_include_tax": "true",
    "date_created": "2022-06-26T06:33:57",
    "date_modified": "2022-06-26T06:33:57",
    "discount_total": "0.00",
    "discount_tax": "0.00",
    "shipping_total": "0.00",
    "shipping_tax": "0.00",
    "cart_tax": "109.01",
    "total": "1017.45",
    "total_tax": "109.01",
    "customer_id": 3095,
    "order_key": "wc_order_gy1xUxwlX81qH",
    "billing": {
        "first_name": "Jagdish Prasad",
        "last_name": "Khurana",
        "company": "",
        "address_1": "New friends colony Jaipur road",
        "address_2": "76",
        "city": "Alwar",
        "state": "RJ",
        "postcode": "301001",
        "country": "IN",
        "email": "khuranajp@yahoo.co.in",
        "phone": "099969 00902"
    },
    "shipping": {
        "first_name": "Jagdish Prasad",
        "last_name": "Khurana",
        "company": "",
        "address_1": "New friends colony Jaipur road",
        "address_2": "76",
        "city": "Alwar",
        "state": "RJ",
        "postcode": "301001",
        "country": "IN",
        "phone": "099969 00902"
    },
    "payment_method": "cod",
    "payment_method_title": "Cash on delivery",
    "transaction_id": "",
    "customer_ip_address": "2401:4900:1c1b:6800:91d6:489d:7d07:5dee",
    "customer_user_agent": "Mozilla/5.0 (Linux; Android 12; I2127) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
    "created_via": "checkout",
    "customer_note": "",
    "date_completed": "null",
    "date_paid": "null",
    "cart_hash": "cc653512b7350e937ca1c3530b286c99",
    "number": "21177",
    "meta_data": [
        {
            "id": 428155,
            "key": "_billing_phone_formatted",
            "value": "094140 16142"
        },
        {
            "id": 428156,
            "key": "_shipping_phone_formatted",
            "value": "094140 16142"
        },
        {
            "id": 428157,
            "key": "is_vat_exempt",
            "value": "no"
        },
        {
            "id": 428158,
            "key": "_cfw",
            "value": "true"
        },
        {
            "id": 428159,
            "key": "_wc_facebook_for_woocommerce_order_placed",
            "value": "yes"
        },
        {
            "id": 428164,
            "key": "_new_order_email_sent",
            "value": "true"
        },
        {
            "id": 428165,
            "key": "_ga_tracked",
            "value": "1"
        },
        {
            "id": 428166,
            "key": "_wc_facebook_for_woocommerce_purchase_tracked",
            "value": "yes"
        }
    ],
    "line_items": [
        {
            "id": 26060,
            "name": "Prostpro - 60 Capsules - For enlarged prostate",
            "product_id": 9171,
            "variation_id": 0,
            "quantity": 3,
            "tax_class": "gst-12",
            "subtotal": "908.44",
            "subtotal_tax": "109.01",
            "total": "908.44",
            "total_tax": "109.01",
            "taxes": [
                {
                    "id": 480,
                    "total": "109.0125",
                    "subtotal": "109.0125"
                }
            ],
            "meta_data": [],
            "sku": "PROST0060",
            "price": 302.8125,
            "image": {
                "id": "10711",
                "src": "https://www.dharishahayurveda.com/wp-content/uploads/2021/04/ProstPro.png"
            },
            "parent_name": "null"
        }
    ],
    "tax_lines": [
        {
            "id": 26062,
            "rate_code": "IN-RJ-12% IGST-3",
            "rate_id": 480,
            "label": "12% IGST",
            "compound": "false",
            "tax_total": "109.01",
            "shipping_tax_total": "0.00",
            "rate_percent": 12,
            "meta_data": []
        }
    ],
    "shipping_lines": [
        {
            "id": 26061,
            "method_title": "Free shipping",
            "method_id": "free_shipping",
            "instance_id": "2",
            "total": "0.00",
            "total_tax": "0.00",
            "taxes": [],
            "meta_data": [
                {
                    "id": 179200,
                    "key": "Items",
                    "value": "Prostpro - 60 Capsules - For enlarged prostate &times; 3",
                    "display_key": "Items",
                    "display_value": "Prostpro - 60 Capsules - For enlarged prostate &times; 3"
                }
            ]
        }
    ],
    "fee_lines": [],
    "coupon_lines": [],
    "refunds": [],
    "payment_url": "https://www.dharishahayurveda.com/checkout/order-pay/21177/?pay_for_order=true&key=wc_order_gy1xUxwlX81qH",
    "is_editable": "false",
    "needs_payment": "false",
    "needs_processing": "true",
    "date_created_gmt": "2022-06-26T06:33:57",
    "date_modified_gmt": "2022-06-26T06:33:57",
    "date_completed_gmt": "null",
    "date_paid_gmt": "null",
    "currency_symbol": "₹",
    "_links": {
        "self": [
            {
                "href": "https://www.dharishahayurveda.com/wp-json/wc/v3/orders/21177"
            }
        ],
        "collection": [
            {
                "href": "https://www.dharishahayurveda.com/wp-json/wc/v3/orders"
            }
        ],
        "customer": [
            {
                "href": "https://www.dharishahayurveda.com/wp-json/wc/v3/customers/3095"
            }
        ]
    }
})

invoicePaidPayload = json.dumps({
    "entity": "event",
    "account_id": "acc_BFQ7uQEaa7j2z7",
    "event": "invoice.paid",
    "contains": [
        "payment",
        "order",
        "invoice"
    ],
    "payload": {
        "payment": {
            "entity": {
                "id": "pay_DEWHsM9ByjCjYS",
                "entity": "payment",
                "amount": 479030,
                "currency": "INR",
                "status": "captured",
                "order_id": "order_DEWHZoU57pgISd",
                "invoice_id": "inv_DEWHZlfIcdVIXL",
                "international": "false",
                "method": "netbanking",
                "amount_refunded": 0,
                "refund_status": "null",
                "captured": "true",
                "description": "Invoice #21185",
                "card_id": "null",
                "bank": "HDFC",
                "wallet": "null",
                "vpa": "null",
                "email": "gaurav.kumar@example.com",
                "contact": "+919123456789",
                "notes": [],
                "fee": 11305,
                "tax": 1724,
                "error_code": "null",
                "error_description": "null",
                "created_at": 1567686993
            }
        },
        "order": {
            "entity": {
                "id": "order_DEWHZoU57pgISd",
                "entity": "order",
                "amount": 479030,
                "amount_paid": 479030,
                "amount_due": 0,
                "currency": "INR",
                "receipt": "15",
                "offer_id": "null",
                "offers": {
                    "entity": "collection",
                    "count": 0,
                    "items": []
                },
                "status": "paid",
                "attempts": 1,
                "notes": [],
                "created_at": 1567686976
            }
        },
        "invoice": {
            "entity": {
                "id": "inv_DEWHZlfIcdVIXL",
                "entity": "invoice",
                "receipt": "15",
                "invoice_number": "15",
                "customer_id": "cust_BtQNqzmBlAXyTY",
                "customer_details": {
                    "id": "cust_BtQNqzmBlAXyTY",
                    "name": "Gaurav Kumar",
                    "email": "gaurav.kumar@example.com",
                    "contact": "9123456789",
                    "gstin": "24AABCJ1087G1ZT",
                    "billing_address": {
                        "id": "addr_DEVxnrfJblan6u",
                        "type": "billing_address",
                        "primary": "true",
                        "line1": "84th Floor, Millennium Tower, ",
                        "line2": "Corner of 1st and 1st",
                        "zipcode": "560096",
                        "city": "Bangalore",
                        "state": "Karnataka",
                        "country": "in"
                    },
                    "shipping_address": {
                        "id": "addr_DEVzXQePDJFIQJ",
                        "type": "billing_address",
                        "primary": "true",
                        "line1": "Warehouse 1194, Warehouse Lane",
                        "line2": "Warehouse District",
                        "zipcode": "560128",
                        "city": "Bangalore",
                        "state": "Karnataka",
                        "country": "in"
                    },
                    "customer_name": "Gaurav Kumar",
                    "customer_email": "gaurav.kumar@example.com",
                    "customer_contact": "9123456789"
                },
                "order_id": "order_DEWHZoU57pgISd",
                "payment_id": "pay_DEWHsM9ByjCjYS",
                "status": "paid",
                "expire_by": 1569868199,
                "issued_at": 1567686976,
                "paid_at": 1567686996,
                "cancelled_at": "null",
                "expired_at": "null",
                "sms_status": "sent",
                "email_status": "sent",
                "date": 1567682379,
                "terms": "Terms and COnditions for Webhooks",
                "partial_payment": "true",
                "gross_amount": 425000,
                "tax_amount": 54030,
                "taxable_amount": 425000,
                "amount": 479030,
                "amount_paid": 479030,
                "amount_due": 0,
                "first_payment_min_amount": "null",
                "currency": "INR",
                "description": "Test Invoice for Webhooks",
                "notes": [],
                "comment": "Customer Notes for Webhooks",
                "short_url": "https: //rzp.io/i/FLy8PgO",
                "view_less": "true",
                "billing_start": "null",
                "billing_end": "null",
                "type": "invoice",
                "group_taxes_discounts": "false",
                "supply_state_code": "29",
                "user_id": "BFQ7uKsprYMg6p",
                "created_at": 1567686976,
                "idempotency_key": "null"
            }
        }
    },
    "created_at": 1567686996
})

paymentCapturedPayload = json.dumps({
    "entity": "event",
    "account_id": "acc_BFQ7uQEaa7j2z7",
    "event": "payment.captured",
    "contains": [
        "payment"
    ],
    "payload": {
        "payment": {
            "entity": {
                "id": "pay_DESlfW9H8K9uqM",
                "entity": "payment",
                "amount": 100,
                "currency": "INR",
                "base_amount": 100,
                "status": "captured",
                "order_id": "order_DESlLckIVRkHWj",
                "invoice_id": "null",
                "international": "false",
                "method": "netbanking",
                "amount_refunded": 0,
                "amount_transferred": 0,
                "refund_status": "null",
                "captured": "true",
                "description": "null",
                "card_id": "null",
                "bank": "HDFC",
                "wallet": "null",
                "vpa": "null",
                "email": "gaurav.kumar@example.com",
                "contact": "+91465000ghj08",
                "notes": [],
                "fee": 2,
                "tax": 0,
                "error_code": "null",
                "error_description": "null",
                "error_source": "null",
                "error_step": "null",
                "error_reason": "null",
                "acquirer_data": {
                    "bank_transaction_id": "0125836177"
                },
                "created_at": 1567674599
            }
        }
    },
    "created_at": 1567674606
})

payload = "Product=wsfds&Name=hbmnb&Phone=8327347928&form_id=7dc62a5&form_name=Whatsapp"
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}
conn.request("POST", "/popupform", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
