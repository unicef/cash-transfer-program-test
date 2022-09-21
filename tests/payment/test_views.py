import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_Program_list_view():
    instance1 = test_helpers.create_payment_Program()
    instance2 = test_helpers.create_payment_Program()
    client = Client()
    url = reverse("payment_Program_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Program_create_view():
    client = Client()
    url = reverse("payment_Program_create")
    data = {
        "budget": 1.0,
        "end_date": datetime.now(),
        "name": "text",
        "start_date": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Program_detail_view():
    client = Client()
    instance = test_helpers.create_payment_Program()
    url = reverse("payment_Program_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Program_update_view():
    client = Client()
    instance = test_helpers.create_payment_Program()
    url = reverse("payment_Program_update", args=[instance.pk, ])
    data = {
        "budget": 1.0,
        "end_date": datetime.now(),
        "name": "text",
        "start_date": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Payment_list_view():
    instance1 = test_helpers.create_payment_Payment()
    instance2 = test_helpers.create_payment_Payment()
    client = Client()
    url = reverse("payment_Payment_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Payment_create_view():
    head_of_household = test_helpers.create_household_Individual()
    household = test_helpers.create_household_Household()
    client = Client()
    url = reverse("payment_Payment_create")
    data = {
        "quantity": 1.0,
        "head_of_household": head_of_household.pk,
        "household": household.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Payment_detail_view():
    client = Client()
    instance = test_helpers.create_payment_Payment()
    url = reverse("payment_Payment_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Payment_update_view():
    head_of_household = test_helpers.create_household_Individual()
    household = test_helpers.create_household_Household()
    client = Client()
    instance = test_helpers.create_payment_Payment()
    url = reverse("payment_Payment_update", args=[instance.pk, ])
    data = {
        "quantity": 1.0,
        "head_of_household": head_of_household.pk,
        "household": household.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
