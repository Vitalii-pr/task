import pytest
from api.accounts import models as accounts_models
from api.restaurants import models as restaurant_models
from rest_framework.test import APIClient


@pytest.fixture()
def client():
    return APIClient()

@pytest.fixture()
def user():
    user = accounts_models.UserProfile.objects.create_user(email='test@i.ua', name='vitya', password='simple_password')
    return user


@pytest.fixture()
def superuser():
    s_user = accounts_models.UserProfile.objects.create_superuser(email='super_test@i.ua', name='s_user', password='simple_password')
    return s_user


@pytest.fixture()
def superuser_access(superuser, client):
    response = client.post('/api/auth/login', {'email': 'super_test@i.ua', 'password': 'simple_password'})
    return response.data['access']


@pytest.fixture()
def user_access(user, client):
    response = client.post('/api/auth/login', {'email': 'test@i.ua', 'password': 'simple_password'})
    return response.data['access']


@pytest.fixture()
def restaurant():
    test_restaurant = restaurant_models.Restaurant.objects.create(name='test_restaurant', address='test')
    return test_restaurant









