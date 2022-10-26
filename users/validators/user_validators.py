from datetime import date

from dateutil.relativedelta import relativedelta
from rest_framework import serializers

from HW_27.settings import USER_MIN_AGE


def check_birth_date(value):
    delta = relativedelta(date.today(), value)
    if delta.years < USER_MIN_AGE:
        raise serializers.ValidationError("The user's age cannot be less than 9 years")


def check_email(value: str):
    if value.endswith('rambler.ru'):
        raise serializers.ValidationError('Email cannot contains a domain rambler.ru')

