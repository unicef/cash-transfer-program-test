from rest_framework import serializers

from . import models


class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Program
        fields = [
            "budget",
            "end_date",
            "name",
            "last_updated",
            "created",
            "start_date",
        ]

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Payment
        fields = [
            "quantity",
            "last_updated",
            "created",
        ]
