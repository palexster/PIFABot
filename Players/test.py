import json
import pytest
from main import app

@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass # databases and resourses have to be freed at the end. But so far we don't have anything

    request.addfinalizer(teardown)
    return test_client

#def post_json(client, url, json_dict):
#    """Send dictionary json_dict as a json to the specified url """
#    return client.post(url, data=json.dumps(json_dict), content_type='application/json')
#
#def json_of_response(response):
#    """Decode json from response"""
#    return json.loads(response.data.decode('utf8'))

def test_dummy(client):
    response = client.get('/api/players')
    assert response.status_code == 200
    #assert b'Hello, World!' in response.data

#def test_json(client):
#    response = post_json(client, '/add', {'key': 'value'})
#    assert response.status_code == 200
    #assert json_of_response(response) == {"answer": 'value' * 2}