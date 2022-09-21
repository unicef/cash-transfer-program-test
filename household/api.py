from rest_framework import viewsets, permissions

from . import serializers
from . import models


class IndividualViewSet(viewsets.ModelViewSet):
    """ViewSet for the Individual class"""

    queryset = models.Individual.objects.all()
    serializer_class = serializers.IndividualSerializer
    permission_classes = [permissions.IsAuthenticated]


class IndividualRoleInHouseholdViewSet(viewsets.ModelViewSet):
    """ViewSet for the IndividualRoleInHousehold class"""

    queryset = models.IndividualRoleInHousehold.objects.all()
    serializer_class = serializers.IndividualRoleInHouseholdSerializer
    permission_classes = [permissions.IsAuthenticated]


class HouseholdViewSet(viewsets.ModelViewSet):
    """ViewSet for the Household class"""

    queryset = models.Household.objects.all()
    serializer_class = serializers.HouseholdSerializer
    permission_classes = [permissions.IsAuthenticated]


class BankInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the BankInfo class"""

    queryset = models.BankInfo.objects.all()
    serializer_class = serializers.BankInfoSerializer
    permission_classes = [permissions.IsAuthenticated]
