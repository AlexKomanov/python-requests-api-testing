import requests 
from assertpy import assert_that
from configurations import base_url

def test_user_creation():
    
    name = "Alexander"
    job = "QA Automation"
    
    name_entry = {"name": name}
    job_entry = {"job": job}
    
    # creation_user_data = { **name_entry, **job_entry }
    creation_user_data = name_entry|job_entry
    
    response = requests.post(
        url=f"{base_url}/api/users",
        json=creation_user_data
    )
    
    assert_that(response.status_code).is_equal_to(201)
    assert_that(response.ok).is_equal_to(True)
    assert_that(response.reason).is_equal_to("Created")
    json_response = response.json()
    
    assert_that(json_response["name"]).is_equal_to(name)
    assert_that(json_response["job"]).is_equal_to(job)
    assert_that(json_response).contains_entry(name_entry)
    assert_that(json_response).contains_entry(job_entry)