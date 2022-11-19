
def test_index_page(test_client):

    response = test_client.get('/')
    assert response.status_code == 200
    assert b'This is my Flask Application' in response.data
    assert b'From SmoothStack' in response.data


def test_about_page(test_client):

    response = test_client.get('/about')
    assert response.status_code == 200
    assert b'This website adds Students to the Database' in response.data
        

def test_add__student_page(test_client):

    response = test_client.get('/add_student')
    assert response.status_code == 200
    assert b'Student Name:' in response.data
    assert b'Student Id:' in response.data
    assert b'Date of Birth:' in response.data
    assert b'Address:' in response.data
    assert b'State:' in response.data
    assert b'Zip Code:' in response.data

def test_post_add_student_page(test_client):

    response = test_client.post('/add_student',
                                data = {
                                    'student_name': 'John Smith',
                                    'student_id': '1111',
                                    'date_of_birth': '1996-11-18',
                                    'address': '23 Alameda St',
                                    'state': 'CA',
                                    'zip_code': '16802'
                                }
                            )
    assert response.status_code == 500
    assert b'John Smith' in response.data

def test_post_add_student_page_invalid_student_id(test_client):

    response = test_client.post('/add_student',
                                data = {
                                    'student_name': 'John Smith',
                                    'student_id': 'aaaa',
                                    'date_of_birth': '1996-11-18',
                                    'address': '23 Alameda St',
                                    'state': 'CA',
                                    'zip_code': '16802'
                                }
                            )
    assert response.status_code == 200
    assert b'1 validation error for StudentModel' in response.data
    assert b'student_id' in response.data
    assert b'value is not a valid integer' in response.data


        
        
