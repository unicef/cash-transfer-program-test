from django.contrib import admin
from django import forms

from . import models


class ProgramAdminForm(forms.ModelForm):

    class Meta:
        model = models.Program
        fields = "__all__"


class ProgramAdmin(admin.ModelAdmin):
    form = ProgramAdminForm
    list_display = [
        "budget",
        "end_date",
        "name",
        "last_updated",
        "created",
        "start_date",
    ]
    readonly_fields = [
        "budget",
        "end_date",
        "name",
        "last_updated",
        "created",
        "start_date",
    ]


class PaymentAdminForm(forms.ModelForm):

    class Meta:
        model = models.Payment
        fields = "__all__"


class PaymentAdmin(admin.ModelAdmin):
    form = PaymentAdminForm
    list_display = [
        "quantity",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "quantity",
        "last_updated",
        "created",
    ]


admin.site.register(models.Program, ProgramAdmin)
admin.site.register(models.Payment, PaymentAdmin)
