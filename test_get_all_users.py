import requests
from assertpy import assert_that
from configurations import base_url
import pytest


@pytest.mark.sanity()
def test_get_all_users_status_code_and_ok():
    response = requests.get(f"{base_url}/api/users", params={"page": "2"})
    assert response.status_code == 200
    assert_that(response.status_code).is_equal_to(200)
    assert response.ok == True
    assert_that(response.ok).is_true()
    

@pytest.mark.sanity()
@pytest.mark.regression()
def test_get_all_users_existing_keys():
    response = requests.get(f"{base_url}/api/users", params={"page": "2"})
    json_response = response.json()

    assert "total_pages" in json_response.keys()
    assert_that(json_response).contains_key("total_pages")
    assert_that(json_response).contains_key("data")
    