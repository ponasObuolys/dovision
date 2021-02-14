import pytest
from django.contrib.auth.models import User
from django.test import Client
import uuid


@pytest.mark.django_db
def test_django_view(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200

@pytest.fixture
def test_password():
    return 'strong-test-pass'

@pytest.fixture
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs['password'] = test_password
        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)
    return make_user

@pytest.mark.django_db
def test_user_create():
  User.objects.create_user('useris', 'useris@gmail.com', 'slaptazodis')
  assert User.objects.count() == 1

def test_login(client, django_user_model):
    username = "useris"
    password = "slaptazodis"
    user = django_user_model.objects.create_user(username=username, password=password)
    client.force_login(user)

def test_an_admin_view(admin_client):
    response = admin_client.get('/admin/')
    assert response.status_code == 200
