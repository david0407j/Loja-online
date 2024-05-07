import pytest

from loja.base.models import User


@pytest.fixture
def user_joao(db):
    joao = User.objects.create(first_name='João', email='joao@example.com')
    return joao


@pytest.fixture
def logged_jon(client, user_joao):
    client.force_login(user_joao)
    return user_joao
