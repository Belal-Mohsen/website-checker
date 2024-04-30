import pytest
import requests
from click.testing import CliRunner
from unittest.mock import Mock
from check_sites.main import check_sites


@pytest.fixture
def mock_requests_get(mocker):
    return mocker.patch('requests.get')


def test_site_up(mock_requests_get):
    mock_response = Mock(status_code=200)
    mock_response.elapsed.total_seconds.return_value = 0.123
    mock_requests_get.return_value = mock_response
    runner = CliRunner()
    result = runner.invoke(check_sites, ['http://example.com'])
    assert result.exit_code == 0
    assert "http://example.com is up. Response time: 0.123 seconds" in result.output


def test_site_down(mock_requests_get):
    mock_response = Mock(status_code=404)
    mock_requests_get.return_value = mock_response
    runner = CliRunner()
    result = runner.invoke(check_sites, ['http://example.com'])
    assert result.exit_code == 0
    assert "http://example.com is down. Status Code: 404" in result.output


def test_site_error(mock_requests_get):
    mock_requests_get.side_effect = requests.RequestException("Network Error")
    runner = CliRunner()
    result = runner.invoke(check_sites, ['http://example.com'])
    assert result.exit_code == 0
    assert "http://example.com is down. Error: Network Error" in result.output
