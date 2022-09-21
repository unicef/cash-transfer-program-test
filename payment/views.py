from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class ProgramListView(generic.ListView):
    model = models.Program
    form_class = forms.ProgramForm


class ProgramCreateView(generic.CreateView):
    model = models.Program
    form_class = forms.ProgramForm


class ProgramDetailView(generic.DetailView):
    model = models.Program
    form_class = forms.ProgramForm


class ProgramUpdateView(generic.UpdateView):
    model = models.Program
    form_class = forms.ProgramForm
    pk_url_kwarg = "pk"


class ProgramDeleteView(generic.DeleteView):
    model = models.Program
    success_url = reverse_lazy("payment_Program_list")


class PaymentListView(generic.ListView):
    model = models.Payment
    form_class = forms.PaymentForm


class PaymentCreateView(generic.CreateView):
    model = models.Payment
    form_class = forms.PaymentForm


class PaymentDetailView(generic.DetailView):
    model = models.Payment
    form_class = forms.PaymentForm


class PaymentUpdateView(generic.UpdateView):
    model = models.Payment
    form_class = forms.PaymentForm
    pk_url_kwarg = "pk"


class PaymentDeleteView(generic.DeleteView):
    model = models.Payment
    success_url = reverse_lazy("payment_Payment_list")
