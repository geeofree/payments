from services.user import UserService

def test_it_responds_with_an_access_token(client):
    """
    The sign-in endpoint should return an access token when 
    making a request with valid credentials.

    1. It should return a token string in the `data` field.
    2. It should have a `message` with "Sign-in successful!"
    3. It should have a response status code of 200.
    """
    new_user = { 'username': 'lexie', 'password': 'password' }
    UserService.create(new_user)

    response = client.post('/api/auth/sign-in', json=new_user)

    assert type(response.json['data']) is str
    assert response.json['message'] == "Sign-in successful!"
    assert response.json['status'] == 200
    assert response.status_code == 200


def test_that_username_and_password_fields_are_required(client):
    """
    The sign-in endpoint should respond with validation errors 
    when the username and password are not provided in the JSON
    payload.

    1. It should return a status code of 406
    2. It should return with a message: "Validation error."
    3. It should state that username and password fields are required 
       in the JSON payload.
    """
    new_user = { 'username': 'lexie', 'password': 'password' }
    UserService.create(new_user)

    response = client.post('/api/auth/sign-in', json={})

    assert response.json['status'] == 406
    assert response.json['message'] == "Validation error."

    assert type(response.json['data']) is dict
    assert type(response.json['data']['username']) is list
    assert type(response.json['data']['password']) is list

    assert len(response.json['data']['username']) == 1
    assert len(response.json['data']['password']) == 1

    assert response.json['data']['username'][0] == "required field"
    assert response.json['data']['password'][0] == "required field"


def test_that_username_and_password_fields_are_strings(client):
    """
    The sign-in endpoint should respond with validation errors 
    when the username and password are not provided with string 
    values in the JSON payload.

    1. It should return a status code of 406
    2. It should return with a message: "Validation error."
    3. It should state that username and password fields must be
       string values in the JSON payload.
    """
    new_user = { 'username': 'lexie', 'password': 'password' }
    UserService.create(new_user)

    response = client.post('/api/auth/sign-in', json={ 'username': 1, 'password': True })

    assert response.json['status'] == 406
    assert response.json['message'] == "Validation error."

    assert type(response.json['data']) is dict
    assert type(response.json['data']['username']) is list
    assert type(response.json['data']['password']) is list

    assert len(response.json['data']['username']) == 1
    assert len(response.json['data']['password']) == 1

    assert response.json['data']['username'][0] == "must be of string type"
    assert response.json['data']['password'][0] == "must be of string type"
