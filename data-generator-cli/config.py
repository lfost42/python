"""
Configuration variables for each data generator.
"""

"""
Create Admin Variables. Create an admin user if one does not exist.
Required to run create_applicant method.
"""
create_admin = True
admin_username = "administrator"
admin_password = "P@ssword1"
admin_email = "admin.login@smoothstack.com"
admin_phone = "555 555 5555"
user_registration_endpoint = "http://localhost:8070/users/registration"
login_endpoint = "http://localhost:8070/login"

"""
Create Applicant variables. Set number of applicants to create. 
get_applicants checks whether applicants were populated in the database. 
"""
create_applicant = True
num_applicants = 1
applicants_endpoint = "http://localhost:8071/applicants"

get_applicants = False
get_users_endpoint = "http://localhost:8070/users"