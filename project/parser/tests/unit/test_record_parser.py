'''
Tests the parsing of worksheet data and summary methods.
'''
import pytest
from werkzeug.datastructures import FileStorage
from record_parser import summary_data

def test_missing_summary_worksheet():
    """
    GIVEN a file for upload
    WHEN a file is received that does not have a summary worksheet
    THEN check that -1 is returned.
    """
    with open("tests/test_samples/missing_ws_january_2018.xlsx", "rb") as test_file:
        file = FileStorage(
        stream = test_file,
        filename="missing_ws_january_2018.xlsx",
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
        assert summary_data(file) == -1

def test_bad_summary_data():
    """
    GIVEN a file for upload
    WHEN a file is received that has missing summary data
    THEN check that -1 is returned.
    """
    with pytest.raises(ValueError):
        with open("tests/test_samples/bad_summary_march_2018.xlsx", "rb") as test_file:
            file = FileStorage(
            stream = test_file,
            filename="bad_summary_march_2018.xlsx",
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
            summary_data(file)
