"""
Produces random data for applicant through the underwriter microservice endpoints. 
"""
import config
import requests
from logging_handler import logger
from utils import random_user_id, random_user_info
from producer_user import get_header


def create_applicant(num_applicants):
    URL = config.applicants_endpoint
    first_name, middle_name, last_name, email = random_user_id()
    social_security, drivers_license, phone_number, income, address = random_user_info()
    
    for _ in range(num_applicants):
        data = {
            "firstName": first_name,
            "middleName": middle_name,
            "lastName": last_name,
            "dateOfBirth": "1991-07-09",
            "gender": "UNSPECIFIED",
            "email": email,
            "phone": phone_number,
            "socialSecurity": social_security,
            "driversLicense": drivers_license,
            "income": income,
            "address": address,
            "city": "McLean",
            "state": "Virginia",
            "zipcode": "22102",
            "mailingAddress": address,
            "mailingCity": "McLean",
            "mailingState": "Virginia",
            "mailingZipcode": "22102"
        }
        
        response = requests.post(URL, json = data, headers=get_header())
        
        if response.status_code == 201:
            logger.debug(f"{response.status_code}: Create applicant {last_name}, {first_name} successful.")
            return response
        logger.error(f"{response.status_code}: Create applicant failed.")


def get_applicants():
    URL = config.applicants_endpoint
    response = requests.get(
        URL, headers=get_header()
    )
    if response.status_code == 200:
        logger.info("\n".join([r['email'] for r in response.json()['content']]))
        return response
    logger.error(f"{response.status_code}: Could not get applicants")
