# Need for this project:
# Email validation and verification
# Student id validation
# Password length check
# Answer data validation

def validEmail(email):
    import re

    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9]+(\.[A-Z|a-z]{2,})+')

    if re.fullmatch(regex, email):
        return True
    else:
        return False

def verifyEmail(email):

