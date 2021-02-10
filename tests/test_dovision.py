import pytest
from django.test import Client


@pytest.mark.django_db
def test_django_view(client: Client):

    # Run function
    resp = client.get('/')

    # Test output
    assert resp.status_code == 200
