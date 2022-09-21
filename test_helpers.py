import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from household import models as household_models
from payment import models as payment_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_household_Individual(**kwargs):
    defaults = {}
    defaults["birth_date"] = datetime.now()
    if "household" not in kwargs:
        defaults["household"] = create_household_Household()
    defaults.update(**kwargs)
    return household_models.Individual.objects.create(**defaults)
def create_household_IndividualRoleInHousehold(**kwargs):
    defaults = {}
    defaults["role"] = ""
    if "individual" not in kwargs:
        defaults["individual"] = create_household_Individual()
    if "household" not in kwargs:
        defaults["household"] = create_household_Household()
    defaults.update(**kwargs)
    return household_models.IndividualRoleInHousehold.objects.create(**defaults)
def create_household_Household(**kwargs):
    defaults = {}
    defaults["country"] = ""
    if "programs" not in kwargs:
        defaults["programs"] = create_payment_Program()
    if "head_of_household" not in kwargs:
        defaults["head_of_household"] = create_household_Individual()
    if "members" not in kwargs:
        defaults["members"] = create_household_Individual()
    defaults.update(**kwargs)
    return household_models.Household.objects.create(**defaults)
def create_household_BankInfo(**kwargs):
    defaults = {}
    if "individual" not in kwargs:
        defaults["individual"] = create_household_Individual()
    defaults.update(**kwargs)
    return household_models.BankInfo.objects.create(**defaults)
def create_payment_Program(**kwargs):
    defaults = {}
    defaults["budget"] = ""
    defaults["end_date"] = datetime.now()
    defaults["name"] = ""
    defaults["start_date"] = datetime.now()
    defaults.update(**kwargs)
    return payment_models.Program.objects.create(**defaults)
def create_payment_Payment(**kwargs):
    defaults = {}
    defaults["quantity"] = ""
    if "head_of_household" not in kwargs:
        defaults["head_of_household"] = create_household_Individual()
    if "household" not in kwargs:
        defaults["household"] = create_household_Household()
    defaults.update(**kwargs)
    return payment_models.Payment.objects.create(**defaults)
