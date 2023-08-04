from django.dispatch import receiver
from paypal.standard.ipn.signals import valid_ipn_received

from .models import *

@receiver(valid_ipn_received)
def valid_ipn_signal(sender,  **kwargs):
    print('Ipn valid')
    ipn = sender
    if ipn.payment_status == 'Completed':
        try:
            my_pk = ipn.item_name
            reservation = Reservation.objects.get(reservation_paket__slug=my_pk)
            reservation.is_paid = True
            reservation.save()

        except Reservation.DoesNotExist:
            pass