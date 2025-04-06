from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from payment.models import Payment
from .serializers import AcceptPaymentSerializer
from permissions.is_manager import IsManager


class AcceptPaymentAPIView(APIView):
    permission_classes = [IsManager]
    
    def post(self, request, pk):
        try:
            payment = Payment.objects.accept_payment(pk)
            serializer = AcceptPaymentSerializer(payment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Payment.DoesNotExist:
            return Response({"detail": "Payment not found."}, status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
