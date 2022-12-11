"""
Main application module. 
"""
import config
from producer_applicant import create_applicant, get_applicants
from producer_user import create_admin_login


def main():
    if config.create_admin == True:
        create_admin_login()
    if config.create_applicant == True:
        create_applicant()
    if config.get_applicants == True:
        get_applicants()


if __name__ == '__main__':
    main()
