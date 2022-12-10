"""
Main application module. 
"""
import config
from producer_applicant import create_admin_user, create_applicant, get_applicants


def main():
    create_admin_user()
    create_applicant(config.num_applicants)
    get_applicants()


if __name__ == '__main__':
    main()
