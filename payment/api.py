from rest_framework import viewsets, permissions

from . import serializers
from . import models


class ProgramViewSet(viewsets.ModelViewSet):
    """ViewSet for the Program class"""

    queryset = models.Program.objects.all()
    serializer_class = serializers.ProgramSerializer
    permission_classes = [permissions.IsAuthenticated]


class PaymentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Payment class"""

    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
