"""
Tests for web page functionality.
"""
import os
from werkzeug.datastructures import FileStorage

def test_index_page(test_client):
    """
    GIVEN an http request to the default route
    WHEN a response is received from the server
    THEN check that the index pages loads.
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Report Generator' in response.data
    assert b'Select a file to upload and process.' in response.data

def test_405_page(test_client):
    """
    GIVEN an error that does not enable the page to load.
    WHEN an exception occurs outside the bounds of
        general GET or POST processing.
    THEN check that the status is not allowed.
    """
    response = test_client.put('/')
    assert response.status_code == 405
    assert b"405 Method Not Allowed" in response.data

def test_report_page(test_client):
    """
    GIVEN a sample file from the test_samples folder
    WHEN a well formatted filename and data is submitted
    THEN check that a report generates and successfully loads.
    """
    with open("tests/test_samples/expedia_report_monthly_march_2018.xlsx", "rb") as test_file:
        file = FileStorage(
        stream=test_file,
        filename="expedia_report_monthly_march_2018.xlsx",
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
        response = test_client.post(
            '/',
            data = dict(
                file=file,
            ),
            follow_redirects=True,
            content_type='multipart/form-data',
        )
        assert response.status_code == 200
        assert b'Upload Results' in response.data
        assert b'processed and moved to archived.' in response.data
        assert b'Summary Data' in response.data
        assert b'VOC Data' in response.data
        
        os.remove(f'files/archived/{file.filename}')

def test_422_bad_file_year(test_client):
    """
    GIVEN a sample file from the test_samples folder
    WHEN a file that does not include a 4 digit number (i.e., year)
    THEN check that the status is not processable.
    """
    with open("tests/test_samples/bad_file_date_march_20.xlsx", "rb") as test_file:
        file = FileStorage(
        stream = test_file,
        filename="bad_file_date_march_20.xlsx",
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
        response = test_client.post(
            '/',
            data = dict(
                file=file,
            ),
            follow_redirects=True,
            content_type='multipart/form-data',
        )

    assert response.status_code == 422
    assert b'HTTP 422 Unprocessable Entity' in response.data
    assert b'Please try again' in response.data

# def test_422_missing_summary_worksheet(test_client):
#     """
#     GIVEN a sample file from the test_samples folder
#     WHEN a file a missing summary worksheet is submitted
#     THEN check that the status is not processable.
#     """

# def test_422_missing_voc_worksheet(test_client):
#     """
#     GIVEN a sample file from the test_samples folder
#     WHEN a file with a missing voc worksheet is submitted
#     THEN check that the status is not processable.
#     """

# def test_422_unable_to_find_summary_date(test_client):
#     """
#     GIVEN a sample file from the test_samples folder
#     WHEN a file with a non-matching summary date
#     THEN check that the status is not processable.
#     """

# def test_unable_to_find_voc_date(test_client):
#     """
#     GIVEN a sample file from the test_samples folder
#     WHEN a file with a non-matching voc date
#     THEN check that the status is not processable.
#     """
