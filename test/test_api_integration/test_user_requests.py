import pytest
from unittest.mock import patch
from src.api_integration.user_request import User


class TestUser():

    @patch("requests.get")
    def test_get_user_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value= {"id": 1, "name":"Miguel"}

        user = User().get_user("http://api.demo.com/public/v2", 1)
        assert user == {"id": 1, "name": "Miguel"}

    @patch("requests.get")
    def test_get_user_error(self, mock_get):
        mock_get.return_value.status_code = 400

        with pytest.raises(ValueError):
            user = User()
            user.get_user("http://api.demo.com/public/v2", 2)