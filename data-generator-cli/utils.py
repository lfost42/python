"""
Helper methods. 
"""
import string
import requests
import random
from faker import Faker
import config
from logging_handler import logger


fake = Faker()


def random_num(n: int) -> int:
    """A random number generator that passes in the number of digits as a parameter.

    Args:
        n (int): number of digits for the number needed.

    Returns:
        int: A random number with the required number of digits.
    """
    return random.randint(10 ** (n - 1), 10 ** n - 1)


def random_user_id():
    """A random name generator for first, middle, and last names. Interpolates
    email address using first name, middle initial, and last name. 

    Returns:
        string: Random first, middle, last names with email address.  
    """
    first_name = fake.first_name()
    middle_name = fake.first_name()
    last_name = fake.last_name()
    email = f"{first_name.lower()}.{middle_name[0].lower()}.{last_name.lower()}@email.com"
    # logger.info(email)
    return first_name, middle_name, last_name, email


def random_user_info():
    """Generates random user information for Social security number,
    drivers license, phone number, income, and street address.

    Returns:
        string: Social security number, drivers license, phone
        number, income, and street address. 
    """
    social_security = f"{random_num(3)}-{random_num(2)}-{random_num(4)}"
    drivers_license = f"{random.choice(string.ascii_uppercase)}-{random_num(7)}"
    phone_number = f"{random_num(3)} {random_num(3)} {random_num(4)}"
    income = random_num(6)
    address = fake.street_address()
    return social_security, drivers_license, phone_number, income, address

def get_header():
    """Retrieves the authorization header when the admin_login
    user login data is passed to the login endpoint in the user microservice.

    Returns:
        string: An authorization header from the admin_login user. 
    """
    url = config.login_endpoint
    data = {
        "username" : config.admin_username,
        "password" : config.admin_password
        }
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        logger.info("Get header succeeded.")
        return {
            "Authorization" : response.headers["Authorization"]
        }
    logger.error(f"{response.status_code}: Header not saved")
