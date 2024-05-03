"""
GitHub repository:: https://github.com/KostasPapd/Computing_Project
Email verification website: https://app.kickbox.com/accounts/GelrCwkY/verify/api
API key: test_2b2aef53aee36dba0ce05a17fdf6c20e0b772674edb1218e7a5972c5aa369d2c

Need for this project:
Email validation and verification - done
Username validation - done
Password validation - done

Do after database lesson:
Username verification (for logging in)
Password verification
Answer data validation

Use mySQL, find host for database
"""


def validEmail(email):
    import re

    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9]+(\.[A-Z|a-z]{2,})+')

    if re.fullmatch(regex, email):
        return True
    else:
        return False


def verifyEmail(email):
    import kickbox
    client = kickbox.Client("test_2b2aef53aee36dba0ce05a17fdf6c20e0b772674edb1218e7a5972c5aa369d2c")  # API key
    kick = client.kickbox()

    res = kick.verify(email)

    if res.body['result'] != "undeliverable":
        return True
    else:
        return False

def validatePassword(pas):
    import re

    if re.fullmatch(r'[A-Za-z0-9!@_&]{8,}', pas):  # Sets what characters are allowed and required in the password
        # Checks if all the required characters are in the password
        if not any(char.isupper() for char in pas):
            return False
        else:
            if not any(char.islower() for char in pas):
                return False
            else:
                if not any(char.isdigit() for char in pas):
                    return False
                else:
                    return True
    else:
        return False

def validateUsername(username):
    import re

    if re.fullmatch(r'[A-Za-z0-9!@_&]{5,}', username):  # Sets what characters are allowed in the username
        # The {5,} sets the minimum length of the username
        return True
    else:
        return False

