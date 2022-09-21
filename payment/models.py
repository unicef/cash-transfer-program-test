from django.db import models
from django.urls import reverse


class Program(models.Model):

    # Fields
    budget = models.DecimalField(max_digits=16, decimal_places=2)
    end_date = models.DateField(db_index=True)
    name = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    start_date = models.DateField(db_index=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("payment_Program_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("payment_Program_update", args=(self.pk,))


class Payment(models.Model):

    # Relationships
    head_of_household = models.ForeignKey("household.Individual", on_delete=models.CASCADE, related_name="payments", null=True)
    household = models.ForeignKey("household.Household", on_delete=models.CASCADE, related_name="payments",   null=True)

    # Fields
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("payment_Payment_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("payment_Payment_update", args=(self.pk,))
