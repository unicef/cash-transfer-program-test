from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class IndividualListView(generic.ListView):
    model = models.Individual
    form_class = forms.IndividualForm


class IndividualCreateView(generic.CreateView):
    model = models.Individual
    form_class = forms.IndividualForm


class IndividualDetailView(generic.DetailView):
    model = models.Individual
    form_class = forms.IndividualForm


class IndividualUpdateView(generic.UpdateView):
    model = models.Individual
    form_class = forms.IndividualForm
    pk_url_kwarg = "pk"


class IndividualDeleteView(generic.DeleteView):
    model = models.Individual
    success_url = reverse_lazy("household_Individual_list")


class IndividualRoleInHouseholdListView(generic.ListView):
    model = models.IndividualRoleInHousehold
    form_class = forms.IndividualRoleInHouseholdForm


class IndividualRoleInHouseholdCreateView(generic.CreateView):
    model = models.IndividualRoleInHousehold
    form_class = forms.IndividualRoleInHouseholdForm


class IndividualRoleInHouseholdDetailView(generic.DetailView):
    model = models.IndividualRoleInHousehold
    form_class = forms.IndividualRoleInHouseholdForm


class IndividualRoleInHouseholdUpdateView(generic.UpdateView):
    model = models.IndividualRoleInHousehold
    form_class = forms.IndividualRoleInHouseholdForm
    pk_url_kwarg = "pk"


class IndividualRoleInHouseholdDeleteView(generic.DeleteView):
    model = models.IndividualRoleInHousehold
    success_url = reverse_lazy("household_IndividualRoleInHousehold_list")


class HouseholdListView(generic.ListView):
    model = models.Household
    form_class = forms.HouseholdForm


class HouseholdCreateView(generic.CreateView):
    model = models.Household
    form_class = forms.HouseholdForm


class HouseholdDetailView(generic.DetailView):
    model = models.Household
    form_class = forms.HouseholdForm


class HouseholdUpdateView(generic.UpdateView):
    model = models.Household
    form_class = forms.HouseholdForm
    pk_url_kwarg = "pk"


class HouseholdDeleteView(generic.DeleteView):
    model = models.Household
    success_url = reverse_lazy("household_Household_list")


class BankInfoListView(generic.ListView):
    model = models.BankInfo
    form_class = forms.BankInfoForm


class BankInfoCreateView(generic.CreateView):
    model = models.BankInfo
    form_class = forms.BankInfoForm


class BankInfoDetailView(generic.DetailView):
    model = models.BankInfo
    form_class = forms.BankInfoForm


class BankInfoUpdateView(generic.UpdateView):
    model = models.BankInfo
    form_class = forms.BankInfoForm
    pk_url_kwarg = "pk"


class BankInfoDeleteView(generic.DeleteView):
    model = models.BankInfo
    success_url = reverse_lazy("household_BankInfo_list")
