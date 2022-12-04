from app import app

def test_index_page():

    with app.test_client() as client:
        response = client.get('/')

        assert response.status_code == 200
        assert b'This is my Flask Application' in response.data
        assert b'From Tesla' in response.data

        


