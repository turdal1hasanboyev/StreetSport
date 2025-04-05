from django.urls import path

from .api.AcceptPayment.views import AcceptPaymentAPIView


urlpatterns = [
    path('payments/accept/<int:pk>/', AcceptPaymentAPIView.as_view(), name='accept_payment'),
]
