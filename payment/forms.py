from django import forms
from . import models


class ProgramForm(forms.ModelForm):
    class Meta:
        model = models.Program
        fields = [
            "budget",
            "end_date",
            "name",
            "start_date",
        ]


class PaymentForm(forms.ModelForm):
    class Meta:
        model = models.Payment
        fields = [
            "quantity",
            "head_of_household",
            "household",
        ]
