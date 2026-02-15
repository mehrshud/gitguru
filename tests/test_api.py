import pytest
from unittest.mock import patch
from api import api_request

@pytest.fixture
def setup_teardown():
    # setup
    yield
    # teardown

def test_api_request_success(setup_teardown):
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        assert api_request('url') == 200

def test_api_request_failure(setup_teardown):
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404
        assert api_request('url') == 404

def test_api_request_exception(setup_teardown):
    with patch('requests.get') as mock_get:
        mock_get.side_effect = Exception('Test exception')
        with pytest.raises(Exception):
            api_request('url')

def test_api_request_empty_url(setup_teardown):
    with pytest.raises(ValueError):
        api_request('')

def test_api_request_invalid_url(setup_teardown):
    with pytest.raises(ValueError):
        api_request('invalid_url')
