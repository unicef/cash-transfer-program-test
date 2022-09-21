from rest_framework import serializers

from . import models


class IndividualSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Individual
        fields = [
            "created",
            "last_updated",
            "birth_date",
        ]

class IndividualRoleInHouseholdSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.IndividualRoleInHousehold
        fields = [
            "last_updated",
            "role",
            "created",
        ]

class HouseholdSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Household
        fields = [
            "country",
            "created",
            "last_updated",
        ]

class BankInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BankInfo
        fields = [
            "created",
            "last_updated",
        ]
