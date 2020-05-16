import pytest, os, sys, tempfile, mock, json
from flask import Flask

@pytest.fixture
def client():
    with mock.patch('flask.Flask', lambda x: Flask(x)):
        from app import app
        db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True

        with app.test_client() as client:
            # with app.app_context():
            #     app.init_db()
            yield client

        os.close(db_fd)
        os.unlink(app.config['DATABASE'])
	
@pytest.mark.it("The Family structure has to be initialized with the 3 members specified in the instructions")
def test_first_three(client):
    response = client.get('/members')
    members = json.loads(response.data)
    assert len(members) == 3

@pytest.mark.it("Implement method POST /member to add a new member")
def test_add_implementation(client):
    response = client.post('/member', json={
		"first_name": "Tommy",
        "id": 3443,
		"age": 23,
		"lucky_numbers": [34,65,23,4,6]
	})
    assert response.status_code == 200

@pytest.mark.it("Method POST /member should return an EMPTY response body")
def test_add_empty_reponse_body(client):
    response = client.post('/member', json={
		"first_name": "Sandra",
		"age": 12,
        "id": 4446,
		"lucky_numbers": [12,34,33,45,32,12]
	})
    assert response.data != b""

@pytest.mark.it("Implement method GET /members")
def test_get_members_exist(client):
    response = client.get('/members')
    assert response.status_code == 200

@pytest.mark.it("Method GET /members should return a list")
def test_get_members_returns_list(client):
    response = client.get('/members')
    data = json.loads(response.data)
    assert isinstance(data, list)

@pytest.mark.it("We added two members using POST /member, when calling the GET /members should get a list of length == 5")
def test_get_members_returns_list_of_five(client):
    response = client.get('/members')
    members = json.loads(response.data)
    assert len(members) == 5

@pytest.mark.it("Method GET /member/<int:id> should exist")
def test_get_single_member_implemented(client):
    response = client.get('/member/3443')
    assert response.status_code == 200

@pytest.mark.it("Method GET /member/<int:id> should return a one single family member in a dictionary format")
def test_get_single_member_returns_dict(client):
    response = client.get('/member/3443')
    data = json.loads(response.data)
    assert data is not None
    assert isinstance(data, dict)

@pytest.mark.it("The dictionary returned by GET /member/<int:id> should contain one family member with the keys [name, id, age, lucky_numbers]")
def test_get_single_member_has_keys(client):
    response = client.get('/member/3443')
    data = json.loads(response.data)

    assert data is not None
    assert "first_name" in data
    assert "id" in data
    assert "age" in data
    assert "lucky_numbers" in data

@pytest.mark.it("Method GET /member/3443 should return Tommy")
def test_get_first_member_tommy(client):
    response = client.get('/member/3443')
    data = json.loads(response.data)
    assert data is not None
    assert "first_name" in data
    assert data["first_name"] == "Tommy"

@pytest.mark.it("Implement method DELETE /member/<int:id> to delete a family member")
def test_delete_member(client):
    response = client.delete('/member/3443')
    assert response.status_code == 200

@pytest.mark.it("Method DELETE /member/3443 should return dictionary with 'done' key")
def test_delete_response(client):
    client.post('/member', json={
		"first_name": "Tommy",
        "id": 3443,
		"age": 23,
		"lucky_numbers": [34,65,23,4,6]
	})
    response = client.delete('/member/3443')
    assert response.json["done"] == True

@pytest.mark.it("After deleting the member 3443 we called GET /members and it should return a list with 4 members")
def test_get_members_returns_list_of_four(client):
    response = client.get('/members')
    members = json.loads(response.data)
    assert len(members) == 4
