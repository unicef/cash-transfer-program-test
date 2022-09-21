from django import forms
from . import models


class IndividualForm(forms.ModelForm):
    class Meta:
        model = models.Individual
        fields = [
            "birth_date",
            "household",
        ]


class IndividualRoleInHouseholdForm(forms.ModelForm):
    class Meta:
        model = models.IndividualRoleInHousehold
        fields = [
            "role",
            "individual",
            "household",
        ]


class HouseholdForm(forms.ModelForm):
    class Meta:
        model = models.Household
        fields = [
            "country",
            "programs",
            "head_of_household",
            "members",
        ]


class BankInfoForm(forms.ModelForm):
    class Meta:
        model = models.BankInfo
        fields = [
            "individual",
        ]
