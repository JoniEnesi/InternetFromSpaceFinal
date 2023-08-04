from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Price(models.Model):
    internet_id = models.AutoField(primary_key=True)
    internet_title = models.CharField(max_length=60, null=True, blank=True)
    internet_model = models.CharField(max_length=60, null=True, blank=True)
    internet_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # 199.99
    download_speed = models.CharField(max_length=60, null=True, blank=True)
    upload_speed = models.CharField(max_length=60, null=True, blank=True)
    data_cap = models.CharField(max_length=60, null=True, blank=True)
    contract = models.CharField(max_length=60, null=True, blank=True)
    setup_cost = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return f'{self.internet_title}'

class PriceBusiness(models.Model):
    internet1_id = models.AutoField(primary_key=True)
    internet1_title = models.CharField(max_length=60, null=True, blank=True)
    internet1_model = models.CharField(max_length=60, null=True, blank=True)
    internet1_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # 199.99
    download1_speed = models.CharField(max_length=60, null=True, blank=True)
    upload1_speed = models.CharField(max_length=60, null=True, blank=True)
    data1_cap = models.CharField(max_length=60, null=True, blank=True)
    contract1 = models.CharField(max_length=60, null=True, blank=True)
    setup1_cost = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return f'{self.internet1_title}'


class Message(models.Model):
    message_name = models.CharField(max_length=60, null=True, blank=True)
    message_surname = models.CharField(max_length=60, null=True, blank=True)
    message_email = models.EmailField(null=True, blank=True)
    message_comment = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.message_name} - {self.message_surname}"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    reservation_name = models.CharField(max_length=60, null=True, blank=True)
    reservation_lastname = models.CharField(max_length=60, null=True, blank=True)
    reservation_email = models.EmailField(null=True, blank=True)
    reservation_phone = models.BigIntegerField(null=True, blank=True)
    reservation_address = models.CharField(max_length=100, null=True, blank=True)
    reservation_street = models.CharField(max_length=100, null=True, blank=True)
    reservation_paket = models.ForeignKey(Price, on_delete=models.CASCADE, null=True, blank=True)
    reservation_paketBusiness = models.ForeignKey(PriceBusiness, on_delete=models.CASCADE, null=True, blank=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.reservation_name} - {self.reservation_lastname} - {self.reservation_paket} - {self.reservation_paketBusiness}"


    class Order (models.Model):
        pass