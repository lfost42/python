"""
Test the upload, reading, and moving of excel files.
"""
import os
from werkzeug.datastructures import FileStorage
from openpyxl import Workbook
from file_handler import check_file, read_file, archive_file, error_file

def test_check_file_is_successful():
    """
    GIVEN a file for uplaod
    WHEN a file uploaded is an excel file, at
        least 7 characters, and is not a duplicate
    THEN check that 1 is returned.
    """
    with open("tests/test_samples/expedia_report_monthly_march_2018.xlsx", "rb") as test_file:
        file = FileStorage(
        stream = test_file,
        filename="expedia_report_monthly_march_2018.xlsx",
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
        return_val = check_file(file)
        print(return_val)
        assert return_val == 1

def test_check_file_is_not_excel():
    """
    GIVEN a file for upload
    WHEN a file is not an excel file
    THEN check that 'incorrect filetype' is returned
    """
    with open("tests/test_samples/file.jpg", "rb") as test_file:
        file = FileStorage(
        stream = test_file,
        filename="file.jpg",
        content_type="image/jpeg",
    )
        assert check_file(file) == 'incorrect filetype'

def test_check_file_name_is_too_short():
    """
    GIVEN a file for upload
    WHEN a file is received for upload
    THEN check that 'file name too short' is returned.
    """
    with open("tests/test_samples/short.xlsx", "rb") as test_file:
        file = FileStorage(
        stream = test_file,
        filename="short.xlsx",
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
        assert check_file(file) == 'file name too short'

def test_check_file_is_duplicate():
    """
    GIVEN a file for upload
    WHEN a file is received for upload and is a duplicate
    THEN check that 'duplicate file' is returned.
    """
    with open("tests/test_samples/duplicate.xlsx", "rb") as test_file:
        file = FileStorage(
        stream = test_file,
        filename="duplicate.xlsx",
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
        assert check_file(file) == 'duplicate file'

def test_read_file_raises_exception():
    """
    GIVEN a file for upload
    WHEN a file is received that does not contain a workbook
    THEN check that -1 is returned.
    """
    with open("tests/test_samples/argumentexception.xlxs", "rb") as test_file:
        file = FileStorage(
        stream = test_file,
        filename="argumentexception.xlxs",
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
        assert read_file(file) == -1

def test_read_file_loads_workbook():
    """
    GIVEN a file for upload
    WHEN a file is received that contains a workbook
    THEN check that 1 is returned.
    """
    with open("tests/test_samples/expedia_report_monthly_march_2018.xlsx", "rb") as test_file:
        file = FileStorage(
        stream = test_file,
        filename="expedia_report_monthly_march_2018.xlsx",
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
        assert isinstance(read_file(file), Workbook)

def test_archive_file_moves_file_to_archived():
    """
    GIVEN a file for upload
    WHEN a the destination folder exists
    THEN the file is moved into the archived folder
    """
    with open("tests/test_samples/file.jpg", "rb") as test_file:
        file = FileStorage(
        stream = test_file,
        filename="file.jpg",
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
        assert archive_file(file) == 1
        os.remove(f'files/archived/{file.filename}')

def test_error_file_moves_file_to_error_folder():
    """
    GIVEN a file for upload
    WHEN a the destination folder exists
    THEN the file is moved into the error folder
    """
    with open("tests/test_samples/file.jpg", "rb") as test_file:
        file = FileStorage(
        stream = test_file,
        filename="file.jpg",
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
        assert error_file(file) == 1
