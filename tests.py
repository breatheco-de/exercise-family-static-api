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

@pytest.mark.it("Implement method GET /members")
def test_get_members_exist(client):
    response = client.get('/members')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)

@pytest.mark.it("Method GET /members should return a list")
def test_get_members_returns_list(client):
    response = client.get('/members')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)

# @pytest.mark.it("Implement method GET todos")
# def test_simple_add(client):
#     response = client.post('/members', data=json.dumps({ "done": True, "label": "Sample Todo 2" }))
#     assert response.status_code == 200
#     data = json.loads(response.data)
#     assert isinstance(data, list)