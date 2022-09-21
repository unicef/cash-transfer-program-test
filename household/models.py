from django.db import models
from django.urls import reverse


class Individual(models.Model):

    # Relationships
    household = models.ForeignKey("household.Household", on_delete=models.CASCADE, related_name="individuals", null=True, blank=True)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    birth_date = models.DateField(blank=True, null=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("household_Individual_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("household_Individual_update", args=(self.pk,))


class IndividualRoleInHousehold(models.Model):

    # Relationships
    individual = models.ForeignKey("household.Individual", on_delete=models.CASCADE, related_name="households_and_roles")
    household = models.ForeignKey("household.Household", on_delete=models.CASCADE, related_name="individuals_and_roles")

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    role = models.CharField(max_length=30, blank=True, choices=(("HEAD", "Head"),("SECOND", "Second"),("USELESS", "Non role"), ))
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("household_IndividualRoleInHousehold_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("household_IndividualRoleInHousehold_update", args=(self.pk,))


class Household(models.Model):

    # Relationships
    programs = models.ManyToManyField("payment.Program", related_name="households",  blank=True)
    head_of_household = models.OneToOneField("household.Individual", related_name="heading_household", on_delete=models.CASCADE)
    members = models.ManyToManyField("household.Individual", through="household.IndividualRoleInHousehold", related_name="household_members",)

    # Fields
    country = models.CharField(max_length=3)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("household_Household_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("household_Household_update", args=(self.pk,))


class BankInfo(models.Model):

    # Relationships
    individual = models.ForeignKey("household.Individual", on_delete=models.CASCADE, related_name="bank_infos",)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("household_BankInfo_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("household_BankInfo_update", args=(self.pk,))
