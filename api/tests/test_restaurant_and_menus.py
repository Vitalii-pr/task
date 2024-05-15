import pytest
from rest_framework import status
from api.tests.test_user import test_superuser_login
from api.restaurants.models import Restaurant


@pytest.mark.django_db
def test_restaurant_create(client, superuser_access):

    response = client.post('/api/restaurants/', dict(name='Restaurant', address='some address'), HTTP_AUTHORIZATION=f'Bearer {superuser_access}')
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_restaurant_create_fail(client, user_access):

    response = client.post('/api/restaurants/', dict(name='Restaurant', address='some address'), HTTP_AUTHORIZATION=f'Bearer {user_access}')
    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
def test_restaurant_admin_add(client, superuser_access, user, restaurant):

    response = client.post(f'/api/restaurants/{restaurant.id}/add_restaurant_admin/?user_id={user.id}', dict(name='Restaurant', address='some address'), HTTP_AUTHORIZATION=f'Bearer {superuser_access}')
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_restaurant_admin_add_fail(client, superuser, user_access, restaurant):

    response = client.post(f'/api/restaurants/{restaurant.id}/add_restaurant_admin/?user_id={superuser.id}', dict(name='Restaurant', address='some address'), HTTP_AUTHORIZATION=f'Bearer {user_access}')
    assert response.status_code == status.HTTP_403_FORBIDDEN






