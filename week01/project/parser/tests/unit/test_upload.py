"""
Tests all upload methods.
"""
from werkzeug.datastructures import FileStorage

def test_check_file(test_client):
    """
    GIVEN a sample file from test_samples
    WHEN a well formatted filename and data is submitted
    THEN check that a report generates and successfully loads.
    """
    file = FileStorage(
        stream=open("tests/test_samples/expedia_report_monthly_march_2018.xlsx", "rb"),
        filename="duplicate.xlsx",
        content_type="tests/test_samples/duplicate.xlsx",
    )
    response = test_client.post(
        '/',
        data = dict(
            file=file,
        ),
        follow_redirects=True,
        content_type='multipart/form-data',
    )
