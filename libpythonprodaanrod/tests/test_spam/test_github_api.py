from unittest.mock import Mock

import pytest

from libpythonprodaanrod import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/58538350?v=4'
    resp_mock.json.return_value = {
        'login': 'daanrod', 'id': 58538350, 'node_id': 'MDQ6VXNlcjU4NTM4MzUw',
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpythonprodaanrod.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('daanrod')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('renzo')
    assert 'https://avatars.githubusercontent.com/u/402714?v=4' == url
