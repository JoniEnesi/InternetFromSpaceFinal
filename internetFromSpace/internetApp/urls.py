from django.urls import path
from . import views

urlpatterns = [
    path("", views.homeFun, name="home"),
    path("about/", views.aboutFun, name="about"),
    path("How_it_works/", views.worksFun, name="works"),
    path("contact/", views.contactFun, name="contact"),
    path("price", views.priceFun, name="price"),
    path("singup", views.singupFun, name="singup"),
    path("logout", views.logout, name="logout"),
    path("register", views.registerFun, name="register"),
    path("internet", views.internetFun, name="internet"),
    path("innvation", views.innovationFun, name="innovation"),
    path("cyber", views.cyberFun, name="cyber"),
    path("product/<slug:slug>/", views.priceProduct, name="product"),
    path("product_business/<slug:slug>/", views.priceProductBusiness, name="productBusiness"),
    path("paypal-reverse", views.paypal_reverse, name="paypal-reverse"),
    path("paypal-cancel", views.paypal_cancel, name="paypal-cancel"),
    path("pay/<slug:slug>/", views.payFun, name="pay"),
]