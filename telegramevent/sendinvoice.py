import requests

from django.conf import settings


SEND_INVOICE = "/sendInvoice"

URL = settings.TELEGRAM_BOT_URL

PROVIDER_TOKEN = settings.PROVIDER_TOKEN

def set_label_price(items):
    data = []
    for item in items:
        label_price = {}
        label_price['label'] = item.product.name + " x" + str(item.quantity)
        label_price['amount'] = int(item.price * item.quantity * 100)
        data.append(label_price)

    return data


def get_invoice(order):
    invoice = {}
    invoice["chat_id"] = order.costumer_id
    invoice["title"] = "Order #" + str(order.id)
    invoice["description"] = "Perfect lunch from Durger Duck"
    invoice["provider_token"] = PROVIDER_TOKEN
    invoice["payload"] = int(f'{order.costumer_id}{order.id}')
    invoice["currency"] = "USD"
    invoice["prices"] = set_label_price(order.items.all())
    invoice["photo_url"] = "https://djabrail.pythonanywhere.com/media/product/10-103137_fast-food-clipart-png.png"
    invoice["photo_width"] = 500
    invoice["photo_height"] = 281
    invoice["start_parameter"] = "PAY"
    invoice["need_phone_number"] = True
    invoice["need_shipping_address"] = True
    invoice["is_flexible"] = True

    return invoice



def send_invoice(invoice):
    r = requests.post(url=f"{URL}{SEND_INVOICE}", json=invoice)
    return r.json()