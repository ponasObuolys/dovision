from typing import List
from typing import Tuple

import pytest
from django.contrib.auth.models import User

from django.test import Client
from django.urls import reverse

from doVision.models import Task


@pytest.mark.django_db
def test_django_view(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200


def test_an_admin_view(admin_client: Client):
    response = admin_client.get('/admin/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_login(client: Client, django_user_model: User):
    django_user_model.objects.create_user(
        'test',
        'test@example.com',
        'secret',
    )
    resp = client.post('/accounts/login/', {
        'username': 'test',
        'password': 'secret',
    })
    assert resp.status_code == 302, resp.context['form'].errors.as_text()
    assert resp['location'] == reverse('TodoList')


def _list_tasks(tasks: List[Task]) -> List[Tuple[str, bool]]:
    return [(t.title, t.prior) for t in tasks]


@pytest.mark.django_db
def test_priority(client: Client):
    t1 = Task.objects.create(
        title='Task1',
        completed=False,
        prior=False,
    )

    t2 = Task.objects.create(
        title='Task2',
        completed=False,
        prior=False,
    )

    # Check task list
    resp = client.post(reverse('TodoList'))
    assert resp.status_code == 200
    assert _list_tasks(resp.context['tasks']) == [
        ('Task2', False),
        ('Task1', False),
    ]

    # Prioritize first task
    resp = client.get(reverse('prior', args=(t1.pk,)), follow=True)
    assert resp.status_code == 200
    assert _list_tasks(resp.context['tasks']) == [
        ('Task1', True),
        ('Task2', False),
    ]

    # Prioritize second task
    resp = client.get(reverse('prior', args=(t2.pk,)), follow=True)
    assert resp.status_code == 200
    assert _list_tasks(resp.context['tasks']) == [
        ('Task2', True),
        ('Task1', True),
    ]

    # Deprioritize first task
    resp = client.get(reverse('prior', args=(t1.pk,)), follow=True)
    assert resp.status_code == 200
    assert _list_tasks(resp.context['tasks']) == [
        ('Task2', True),
        ('Task1', False),
    ]
