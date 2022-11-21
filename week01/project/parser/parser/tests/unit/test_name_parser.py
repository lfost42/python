"""
Tests for name parsing methods.
"""
from werkzeug.datastructures import FileStorage
from name_parser import check_month

def test_check_month_unable_to_parse():
    """
    GIVEN a file for upload
    WHEN a file is received that does not have a parsable month
    THEN check that -1 is returned. 
    """
    with open("tests/test_samples/missing_month_uary_2018.xlsx", "rb") as test_file:
        file = FileStorage(
        stream = test_file,
        filename="argumentexception.xlxs",
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
        assert check_month(file) == -1