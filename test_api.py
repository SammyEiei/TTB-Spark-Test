import pytest
import requests

BASE_URL = "https://reqres.in/api/users"
HEADERS = {"x-api-key": "REDACTED"}


class TestGetUserProfile:
    """Test suite for reqres.in GET user profile API."""

    def test_get_user_profile_success(self):
        """TC-01: Verify get user profile returns correct data for existing user."""
        response = requests.get(f"{BASE_URL}/12", headers=HEADERS)

        # 1. Verify status code 200
        assert response.status_code == 200

        # 2. Compare response body with expected data
        data = response.json()["data"]
        assert data["id"] == 12
        assert data["email"] == "rachel.howell@reqres.in"
        assert data["first_name"] == "Rachel"
        assert data["last_name"] == "Howell"
        assert data["avatar"] == "https://reqres.in/img/faces/12-image.jpg"

    def test_get_user_profile_not_found(self):
        """TC-02: Verify get user profile returns 404 for non-existing user."""
        response = requests.get(f"{BASE_URL}/1234", headers=HEADERS)

        # 1. Verify status code 404
        assert response.status_code == 404

        # 2. Response body should be {}
        assert response.json() == {}
