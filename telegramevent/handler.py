
SHIPPING_OPTIONS = [
    {
        "id": "1",
        "title": "To go",
        "prices": [
            {
                "label": "To go",
                "amount": 0
            }
        ]
    },
    {
        "id": "2",
        "title": "Delivery",
        "prices": [
            {
                "label": "Express delivery for 30min",
                "amount": 300
            }
        ]
    }
]


def get_inline_keyboard_button(web_app):
    inline_keyboard_markup = {}

    inline_keyboard_button = {}
    inline_keyboard_button["text"] = "Order Food"
    inline_keyboard_button["web_app"] = {"url": web_app}

    inline_keyboard_markup["inline_keyboard"] = [[inline_keyboard_button]]

    return inline_keyboard_markup

def get_message(data, web_app):
    message = {}
    message["chat_id"] = data["message"]["chat"]["id"]
    message["text"] = "<strong>Let's get started</strong> \ud83c\udf5f \n\nPlease tap the button below to order your perfect lunch!"
    message["parse_mode"] = "HTML"
    message["reply_markup"] = get_inline_keyboard_button(web_app)

    return message


def answer_shipping_query(data):
    query_id = data["shipping_query"]["id"]
    address = data["shipping_query"]["shipping_address"]

    answer = {}
    answer["shipping_query_id"] = query_id

    if address["country_code"] == "RU" and address["city"].lower() == "nalchik":
        answer["ok"] = True
        answer["shipping_options"] = SHIPPING_OPTIONS

        return answer

    answer["ok"] = False
    answer["error_message"] = "Delivery available only in Nalchik"

    return answer


def answer_pre_checkout_query(data):
    query_id = data["pre_checkout_query"]["id"]

    answer = {
        "pre_checkout_query_id": query_id,
        "ok": True
    }

    return answer


def save_successful_payment(item, data):
    shipping_options_amount = 0
    for price in SHIPPING_OPTIONS:
        if price["id"] == data["shipping_option_id"]:
            shipping_options_amount = str(int(price["prices"][0]["amount"])/100)

    item.total_amount = str(int(data["total_amount"])/100)
    item.shipping_options_amount = shipping_options_amount
    item.phone = data["order_info"]["phone_number"]
    item.country_code = data["order_info"]["shipping_address"]["country_code"]
    item.state = data["order_info"]["shipping_address"]["state"]
    item.city = data["order_info"]["shipping_address"]["city"]
    item.street_line1 = data["order_info"]["shipping_address"]["street_line1"]
    item.street_line2 = data["order_info"]["shipping_address"]["street_line2"]
    item.post_code = data["order_info"]["shipping_address"]["post_code"]
    item.provider_payment_charge_id = data["provider_payment_charge_id"]
    item.is_paid = True

    item.save()

    return item