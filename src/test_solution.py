import pytest, os, sys, tempfile, mock, json
from flask import Flask


@pytest.fixture
def client():
    with mock.patch('flask.Flask', lambda x: Flask(x)):
        from app import app
        db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        with app.test_client() as client:
            yield client
        os.close(db_fd)
        os.unlink(app.config['DATABASE'])


@pytest.mark.it("The Family structure must be initialized with the 3 members specified in the instructions")
def test_first_three(client):
    response = client.get('/members')
    members = json.loads(response.data)
    assert len(members) == 3, "The Family structure must be initialized with the 3 members specified in the instructions"


@pytest.mark.it("Implement the POST /members method to add a new member")
def test_add_implementation(client):
    response = client.post('/members', json={
        "first_name": "Tommy",
        "age": 23,
        "lucky_numbers": [34, 65, 23, 4, 6]
    })
    assert response.status_code == 200, "Implement the POST /members method to add a new member"


@pytest.mark.it("The POST /members method should return something, NOT EMPTY")
def test_add_empty_response_body(client):
    response = client.post('/members', json={
        "first_name": "Sandra",
        "age": 12,
        "lucky_numbers": [12, 34, 33, 45, 32, 12]
    })
    assert response.data != b"", "The POST /members method should return something, NOT EMPTY"


@pytest.mark.it("Implement the GET /members method")
def test_get_members_exist(client):
    response = client.get('/members')
    assert response.status_code == 200


@pytest.mark.it("The GET /members method should return a list")
def test_get_members_returns_list(client):
    response = client.get('/members')
    data = json.loads(response.data)
    assert isinstance(data, list), "The GET /members method should return a list"


@pytest.mark.it("We added two members using POST /members, so calling GET /members should return a list of length == 5")
def test_get_members_returns_list_of_five(client):
    response = client.get('/members')
    members = json.loads(response.data)
    assert len(members) == 5, "We added two members using POST /members, so calling GET /members should return a list of length == 5"


@pytest.mark.it("The GET /members/<int:id> method should exist")
def test_get_single_member_implemented(client):
    post_response = client.post('/members', json={
        "first_name": "Tommy",
        "age": 23,
        "lucky_numbers": [1, 2, 3]
    })
    tommy = json.loads(post_response.data)
    get_response = client.get(f"/members/{tommy['id']}")
    assert get_response.status_code == 200, "The GET /members/<int:id> method should exist"


@pytest.mark.it("The GET /members/<int:id> method should return a single family member in dictionary format")
def test_get_single_member_returns_dict(client):
    post_response = client.post('/members', json={
        "first_name": "Tommy",
        "age": 23,
        "lucky_numbers": [1, 2, 3]
    })
    tommy = json.loads(post_response.data)
    get_response = client.get(f"/members/{tommy['id']}")
    data = json.loads(get_response.data)
    assert data is not None, "The GET /members/<int:id> method should return a single family member in dictionary format"
    assert isinstance(data, dict), "The GET /members/<int:id> method should return a single family member in dictionary format"


@pytest.mark.it("The dictionary returned by GET /members/<int:id> should contain the keys: [first_name, id, age, lucky_numbers]")
def test_get_single_member_has_keys(client):
    post_response = client.post('/members', json={
        "first_name": "Tommy",
        "age": 23,
        "lucky_numbers": [1, 2, 3]
    })
    tommy = json.loads(post_response.data)
    response = client.get(f"/members/{tommy['id']}")
    data = json.loads(response.data)

    assert data is not None, "The dictionary returned by GET /members/<int:id> should contain the keys: [first_name, id, age, lucky_numbers]"
    assert "first_name" in data, "The dictionary returned by GET /members/<int:id> should contain the keys: [first_name, id, age, lucky_numbers]"
    assert "id" in data, "The dictionary returned by GET /members/<int:id> should contain the keys: [first_name, id, age, lucky_numbers]"
    assert "age" in data
    assert "lucky_numbers" in data


@pytest.mark.it("The GET /members/<id> method should return Tommy")
def test_get_first_member_tommy(client):
    post_response = client.post('/members', json={
        "first_name": "Tommy",
        "age": 23,
        "lucky_numbers": [1]
    })
    tommy = json.loads(post_response.data)
    response = client.get(f"/members/{tommy['id']}")
    data = json.loads(response.data)
    assert data["first_name"] == "Tommy", "The GET /members/<id> method should return Tommy"


@pytest.mark.it("Implement the DELETE /members/<int:id> method to delete a family member")
def test_delete_member(client):
    post_response = client.post('/members', json={
        "first_name": "Tommy",
        "age": 23,
        "lucky_numbers": [1, 2, 3]
    })
    tommy = json.loads(post_response.data)
    delete_response = client.delete(f"/members/{tommy['id']}")
    assert delete_response.status_code == 200, "Implement the DELETE /members/<int:id> method to delete a family member"


@pytest.mark.it("The DELETE /members/<id> method should return a dictionary with the 'done' key")
def test_delete_response(client):
    post_response = client.post('/members', json={
        "first_name": "Tommy",
        "age": 23,
        "lucky_numbers": [1, 2, 3]
    })
    tommy = json.loads(post_response.data)
    delete_response = client.delete(f"/members/{tommy['id']}")
    assert delete_response.json["done"] == True, "The DELETE /members/<id> method should return a dictionary with the 'done' key"

