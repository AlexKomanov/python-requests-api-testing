import requests 
from assertpy import assert_that

def test_user_deletion():
    response = requests.delete("https://reqres.in/api/users/2")
    
    assert_that(response.status_code).is_equal_to(204)
    assert_that(response.reason).is_equal_to_ignoring_case("no content")