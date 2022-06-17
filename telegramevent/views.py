# import json
import requests

from django.conf import settings

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from telegramevent import handler

from order.models import Order


ANSWER_SHIPPING_QUERY = "/answerShippingQuery"
ANSWER_PRE_CHECKOUT_QUERY = "/answerPreCheckoutQuery"
SEND_MESSAGE = "/sendMessage"

URL = settings.TELEGRAM_BOT_URL

@api_view(['POST', 'GET'])
def event_handler(request):
    data = request.data

#    with open('telequery.json', 'a', encoding="utf-8") as file:
#        json.dump(data, file, indent=2, ensure_ascii=False)

    if "shipping_query" in data:
        answer = handler.answer_shipping_query(data)
        requests.post(url=f"{URL}{ANSWER_SHIPPING_QUERY}", json=answer)

    elif "pre_checkout_query" in data:
        answer = handler.answer_pre_checkout_query(data)
        requests.post(url=f"{URL}{ANSWER_PRE_CHECKOUT_QUERY}", json=answer)

    elif "successful_payment" in data.get("message"):
        successful_payment = data["message"]["successful_payment"]
        order = Order.objects.filter(payload=int(successful_payment["invoice_payload"]))[0]
        if order:
            handler.save_successful_payment(order, successful_payment)

    elif "text" in data.get("message"):
        if "/start" == data["message"]["text"]:
            message = handler.get_message(data, settings.WEB_APP)
            requests.post(url=f"{URL}{SEND_MESSAGE}", json=message)

    return Response(status=status.HTTP_200_OK)