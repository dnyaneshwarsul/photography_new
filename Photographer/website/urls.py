from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('category/', views.category, name="category"),
    path('photography/', views.photography, name="photography"),
    path('gallery/', views.gallery, name="gallery"),
    path('contact/', views.contact, name="contact"),
    path("booking_form/", views.booking_form, name="booking_form"),
    path("check-date-availability/", views.check_date_availability, name="check_date_availability"),
    path("pay-remaining/<int:id>/", views.pay_remaining, name="pay_remaining"),
    path("api/create-razorpay-order/", views.create_razorpay_order, name="create_razorpay_order"),
    path("customer-login/", views.customer_login, name="customer_login"),
    path("my-bookings/", views.my_bookings, name="my_bookings"),
    path("customer-logout/", views.customer_logout, name="customer_logout"),
    path("forgot-password/", views.forgot_password, name="forgot_password"),
    path("download-pdf-receipt/<int:id>/", views.download_pdf_receipt, name="download_pdf_receipt"),
]