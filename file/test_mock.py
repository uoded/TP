from unittest.mock import patch
from mock import fetch_data

@patch("requests.get")
def test_fetch_data(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"key": "value"}
    
    result = fetch_data("http://example.com")
    
    assert result == {"key": "value"}
    mock_get.assert_called_once_with("http://example.com")
