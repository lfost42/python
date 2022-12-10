"""
Produces random data for users through the user microservice endpoints. 
"""
import requests
from utils import random_user_id, get_header
from logging_handler import logger
import config


def create_admin_login():
    """Creates an administrator login account to provide access to
    the applications endpoint in the underwriter microservice.

    Returns:
        json: a response object.
    """
    url = config.user_registration_endpoint
    first_name, middle_name, last_name, email=random_user_id()
    admin_data = {
        "username" : config.admin_username,
        "password" : config.admin_password,
        "role" : "admin",
        "firstName" : first_name,
        "lastName" : last_name,
        "email" : config.admin_email,
        "phone" : config.admin_phone
    }
    head = {'Content-Type': 'application/json'}
    response = requests.post(url, json=admin_data, headers=head)

    if response.status_code == 201:
        logger.debug(f"{response.status_code}: Created admin user")
        return response    
    logger.error(f"{response.status_code}: Admin not created.")

