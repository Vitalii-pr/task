import pytest
from rest_framework import status


@pytest.mark.django_db
def test_register_user(client):
    payload = dict(
            name='vitalii',
            email='qwerty@gmail.com',
            password='hellow',
    )

    response = client.post('/api/auth/register', data=payload)

    data = response.data

    assert data['email'] == payload['email']
    assert 'password' not in data


@pytest.mark.django_db
def test_login_user(user, client):
    response = client.post('/api/auth/login', dict(email='test@i.ua', password='simple_password'))

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_login_user_fail(client):
    response = client.post('/api/auth/login', dict(email='somerandomvalues@i.ua', password='hell'))

    assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.django_db
def test_superuser_login(superuser,client):
    response = client.post('/api/auth/login', dict(email='super_test@i.ua', password='simple_password'))
    assert response.status_code == status.HTTP_200_OK



@pytest.mark.django_db
def test_list_users(superuser_access, client):

    response = client.get('/api/auth/all',  HTTP_AUTHORIZATION=f'Bearer {superuser_access}')

    assert response.status_code == status.HTTP_200_OK









