from services.user import UserService

def test_it_responds_with_an_access_token(client):
    new_user = { 'username': 'lexie', 'password': 'password' }
    UserService.create(new_user)
    response = client.post('/api/auth/sign-in', json=new_user)

    assert type(response.json['data']) is str
    assert response.json['message'] == "Sign-in successful!"
    assert response.json['status'] == 200
