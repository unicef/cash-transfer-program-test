from django.contrib import admin
from django import forms

from . import models


class IndividualAdminForm(forms.ModelForm):

    class Meta:
        model = models.Individual
        fields = "__all__"


class IndividualAdmin(admin.ModelAdmin):
    form = IndividualAdminForm
    list_display = [
        "created",
        "last_updated",
        "birth_date",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        "birth_date",
    ]


class IndividualRoleInHouseholdAdminForm(forms.ModelForm):

    class Meta:
        model = models.IndividualRoleInHousehold
        fields = "__all__"


class IndividualRoleInHouseholdAdmin(admin.ModelAdmin):
    form = IndividualRoleInHouseholdAdminForm
    list_display = [
        "last_updated",
        "role",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "role",
        "created",
    ]


class HouseholdAdminForm(forms.ModelForm):

    class Meta:
        model = models.Household
        fields = "__all__"


class HouseholdAdmin(admin.ModelAdmin):
    form = HouseholdAdminForm
    list_display = [
        "country",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "country",
        "created",
        "last_updated",
    ]


class BankInfoAdminForm(forms.ModelForm):

    class Meta:
        model = models.BankInfo
        fields = "__all__"


class BankInfoAdmin(admin.ModelAdmin):
    form = BankInfoAdminForm
    list_display = [
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


admin.site.register(models.Individual, IndividualAdmin)
admin.site.register(models.IndividualRoleInHousehold, IndividualRoleInHouseholdAdmin)
admin.site.register(models.Household, HouseholdAdmin)
admin.site.register(models.BankInfo, BankInfoAdmin)
