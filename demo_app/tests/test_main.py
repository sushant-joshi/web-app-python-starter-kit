from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

## Test cases


# Test case 1: Test the endpoint /hello with a valid name
def test_say_hello():
    response = client.get("/hello?name=John")
    assert response.status_code == 200  # Check if the response is 200 OK
    assert response.json() == {"message": "Hello John"}

    response = client.get("/hello?name=Alice")
    assert response.status_code == 200  # Check if the response is 200 OK
    assert response.json() == {"message": "Hello Alice"}


# # Test case 2: Test the endpoint /hello with an invalid name
# def test_invalid_query_param():
#     response = client.get("/hello?nameee=2112")
#     assert (
#         response.status_code == 422
#     )  # Missing valid query parameter 'name' should raise http 422 Unprocessable Entity
#     assert response.json() == {
#         "detail": [
#             {
#                 "loc": ["query", "name"],
#                 "msg": "field required",
#                 "type": "value_error.missing",
#             }
#         ]
#     }


# # Test case 3: Test the endpoint /hello with a missing name
# def test_missing_name():
#     response = client.get("/hello")
#     assert (
#         response.status_code == 422
#     )  # Required parameter missing should raise http 422 Unprocessable Entity
#     assert response.json() == {
#         "detail": [
#             {
#                 "loc": ["query", "name"],
#                 "msg": "field required",
#                 "type": "value_error.missing",
#             }
#         ]
#     }


# Test case 4: Test the endpoint /hello with an empty name
def test_empty_name():
    response = client.get("/hello?name=")
    assert response.status_code == 200  # Empty value for name should return http 200 OK
    assert response.json() == {"message": "Hello "}


# Test case 5: Test the endpoint /hello with a name containing special characters
def test_special_characters():
    response = client.get("/hello?name=%20%24%25%40%21%23%5E")
    assert (
        response.status_code == 200
    )  # API should handle special characters, return http 200 OK
    assert response.json() == {"message": "Hello  $%@!#^"}


# Test case 6: Test the endpoint /hello with a name containing multiple names
def test_multiple_names():
    response = client.get("/hello?name=John&name=Alice&name=Bob")
    assert (
        response.status_code == 200
    )  # API should handle multiple names, return http 200 OK
    assert (
        response.json() == {"message": "Hello John"}
        or response.json() == {"message": "Hello Alice"}
        or response.json() == {"message": "Hello Bob"}
    )


# Test case 7: Test the endpoint / with an invalid endpoint
def test_hello_invalid_endpoint():
    response = client.get("/")
    assert response.status_code == 404  # Invalid endpoint should raise 404 Not Found
    assert response.json() == {"detail": "Not Found"}


# Test case 8: Test the endpoint /docs
def test_docs():
    response = client.get("/docs")
    assert response.status_code == 200  # Assert Http status code is 200 OK


# Test case 9: Test the endpoint /openapi.json
def test_openapi_json():
    response = client.get("/openapi.json")
    assert response.status_code == 200  ## Assert Http status code is 200 OK
    assert response.json()["info"]["title"] == "FastAPI"


# Test case 10: Test additional query parameters
def test_additional_query_parameters():
    response = client.get("/hello?name=John&age=30&country=USA")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello John"}


# Test case 11: Test non-existent endpoint
def test_nonexistent_endpoint():
    response = client.get("/invalid")
    assert (
        response.status_code == 404
    )  # Non-implemented endpoint should raise 404 Not Found
    assert response.json() == {"detail": "Not Found"}


# Test case 12: Test case-insensitive name
def test_case_insensitive_name():
    response = client.get("/hello?name=jOHN")
    assert (
        response.status_code == 200
    )  # API should handle case-insensitive names, return http 200 OK
    assert response.json() == {"message": "Hello jOHN"}


# Test case 13: Test unicode name
def test_unicode_name():
    response = client.get("/hello?name=日本語")
    assert (
        response.status_code == 200
    )  # API should handle unicode names, return http 200 OK
    assert response.json() == {"message": "Hello 日本語"}


# Test case 14: Test endpoint /hello with a name containing numbers
def test_name_with_numbers():
    response = client.get("/hello?name=2112")
    assert (
        response.status_code == 200
    )  # API should handle names containing numbers, return http 200 OK
    assert response.json() == {"message": "Hello 2112"}
