# import json
from telegramevent.sendinvoice import get_invoice, send_invoice

from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import OrderSerializer


@api_view(['POST'])
def checkout_with_telegram(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        price_amount = sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])
        order = serializer.save(price_amount=price_amount)
        invoice = get_invoice(order)
        order.payload = invoice["payload"]
        order.save()

        send_invoice(invoice)
#        with open ('response.json', 'w') as file:
#            json.dump(send_invoice(invoice), file, indent=2)

        return Response(status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)