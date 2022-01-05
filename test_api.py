import json
import jsonpath
import pytest
import requests

url = "https://reqres.in/api/users"


@pytest.mark.parametrize("a, b, res", [(10, 2, 5),
                                       (20, 10, 2),
                                       (30, -2, -15),
                                       (5, 2, 2.5)])
def test_division(a, b, res):
    assert a / b == res


def test_create_user():
    file = open("C://Users//sh.makhmudov//PycharmProjects//codes_test//createUser.json")
    json_input = file.read()
    request_json = json.loads(json_input)
    # make POST request
    response = requests.post(url, request_json)
    assert response.status_code == 201

