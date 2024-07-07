import requests
from assertpy import assert_that
from cerberus import Validator
from configurations import base_url
import pytest

@pytest.mark.sanity()
def test_register_user_schema_structure():
 
    schema = {
        "id": {"type": "number"},
        "token": {"type": "string"}
        # "email": {"type": "string"}
        }
    
    validator = Validator(schema, require_all=True)
    
    register_user_data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
        }
    
    response = requests.post(
        url=f"{base_url}/api/register",
        json=register_user_data
        )
    
    if response.status_code == 200:
        is_valid = validator.validate(response.json())
        assert_that(is_valid, description=validator.errors).is_true()
        

{
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": f"{base_url}/img/faces/2-image.jpg"
    },
    "support": {
        "url": f"{base_url}/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}

def test_get_user_schema_structure():
    
    schema = {
        "data": {
            "type": "dict",
            "schema": {
                "id": {"type": "number"},
                "email": {"type": "string"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "avatar": {"type": "string"}
                }
            },
        "support": {
            "type": "dict",
            "schema": {
                "url": {"type": "string"},
                "text": {"type": "string"}
            }
        }
    }
    
    validator = Validator(schema, require_all=True)
    response = requests.get(f"{base_url}/api/users/2")
    if response.status_code == 200:
        is_valid = validator.validate(response.json())
        assert_that(is_valid, description=validator.errors).is_true()
    