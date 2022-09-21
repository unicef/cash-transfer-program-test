import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_Individual_list_view():
    instance1 = test_helpers.create_household_Individual()
    instance2 = test_helpers.create_household_Individual()
    client = Client()
    url = reverse("household_Individual_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Individual_create_view():
    household = test_helpers.create_household_Household()
    client = Client()
    url = reverse("household_Individual_create")
    data = {
        "birth_date": datetime.now(),
        "household": household.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Individual_detail_view():
    client = Client()
    instance = test_helpers.create_household_Individual()
    url = reverse("household_Individual_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Individual_update_view():
    household = test_helpers.create_household_Household()
    client = Client()
    instance = test_helpers.create_household_Individual()
    url = reverse("household_Individual_update", args=[instance.pk, ])
    data = {
        "birth_date": datetime.now(),
        "household": household.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_IndividualRoleInHousehold_list_view():
    instance1 = test_helpers.create_household_IndividualRoleInHousehold()
    instance2 = test_helpers.create_household_IndividualRoleInHousehold()
    client = Client()
    url = reverse("household_IndividualRoleInHousehold_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_IndividualRoleInHousehold_create_view():
    individual = test_helpers.create_household_Individual()
    household = test_helpers.create_household_Household()
    client = Client()
    url = reverse("household_IndividualRoleInHousehold_create")
    data = {
        "role": "text",
        "individual": individual.pk,
        "household": household.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_IndividualRoleInHousehold_detail_view():
    client = Client()
    instance = test_helpers.create_household_IndividualRoleInHousehold()
    url = reverse("household_IndividualRoleInHousehold_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_IndividualRoleInHousehold_update_view():
    individual = test_helpers.create_household_Individual()
    household = test_helpers.create_household_Household()
    client = Client()
    instance = test_helpers.create_household_IndividualRoleInHousehold()
    url = reverse("household_IndividualRoleInHousehold_update", args=[instance.pk, ])
    data = {
        "role": "text",
        "individual": individual.pk,
        "household": household.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Household_list_view():
    instance1 = test_helpers.create_household_Household()
    instance2 = test_helpers.create_household_Household()
    client = Client()
    url = reverse("household_Household_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Household_create_view():
    programs = test_helpers.create_payment_Program()
    head_of_household = test_helpers.create_household_Individual()
    members = test_helpers.create_household_Individual()
    client = Client()
    url = reverse("household_Household_create")
    data = {
        "country": "text",
        "programs": programs.pk,
        "head_of_household": head_of_household.pk,
        "members": members.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Household_detail_view():
    client = Client()
    instance = test_helpers.create_household_Household()
    url = reverse("household_Household_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Household_update_view():
    programs = test_helpers.create_payment_Program()
    head_of_household = test_helpers.create_household_Individual()
    members = test_helpers.create_household_Individual()
    client = Client()
    instance = test_helpers.create_household_Household()
    url = reverse("household_Household_update", args=[instance.pk, ])
    data = {
        "country": "text",
        "programs": programs.pk,
        "head_of_household": head_of_household.pk,
        "members": members.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_BankInfo_list_view():
    instance1 = test_helpers.create_household_BankInfo()
    instance2 = test_helpers.create_household_BankInfo()
    client = Client()
    url = reverse("household_BankInfo_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_BankInfo_create_view():
    individual = test_helpers.create_household_Individual()
    client = Client()
    url = reverse("household_BankInfo_create")
    data = {
        "individual": individual.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_BankInfo_detail_view():
    client = Client()
    instance = test_helpers.create_household_BankInfo()
    url = reverse("household_BankInfo_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_BankInfo_update_view():
    individual = test_helpers.create_household_Individual()
    client = Client()
    instance = test_helpers.create_household_BankInfo()
    url = reverse("household_BankInfo_update", args=[instance.pk, ])
    data = {
        "individual": individual.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
