from django.dispatch import receiver
from paypal.standard.ipn.signals import valid_ipn_received

from .models import *

@receiver(valid_ipn_received)
def valid_ipn_signal(sender,  **kwargs):
    print('Ipn valid')
    ipn = sender
    if ipn.payment_status == 'Completed':
        if ipn.receiver_email != "sb-rwelo26642530@business.example.com":
            print('Invalid receiver email:', ipn.receiver_email)
            return
        if ipn.receiver_email == "sb-rwelo26642530@business.example.com":
            my_pk = ipn.item_name
            reservations = Reservation.objects.filter(reservation_paket__slug=my_pk)
            for reservation in reservations:
                    reservation.is_paid = True
                    reservation.save()



@receiver(valid_ipn_received)
def valid_ipn_signal(sender,  **kwargs):
    print('Ipn valid')
    ipn = sender
    if ipn.payment_status == 'Completed':
        if ipn.receiver_email != "sb-rwelo26642530@business.example.com":
            print('Invalid receiver email:', ipn.receiver_email)
            return
        if ipn.receiver_email == "sb-rwelo26642530@business.example.com":
            my_pk = ipn.item_name
            reservations = Reservation.objects.filter(reservation_paketBusiness__slug=my_pk)
            for reservation in reservations:
                reservation.is_paid = True
                reservation.save()