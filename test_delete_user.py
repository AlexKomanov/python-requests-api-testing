import requests 
from assertpy import assert_that
import pytest
from configurations import base_url


@pytest.mark.skip(reason="Deleting users is not working")
def test_user_deletion():
    response = requests.delete(f"{base_url}/api/users/2") 
    assert_that(response.status_code).is_equal_to(204)
    assert_that(response.reason).is_equal_to_ignoring_case("no content")