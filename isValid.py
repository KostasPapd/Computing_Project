"""
GitHub repository:: https://github.com/KostasPapd/Computing_Project
Email verification website: https://app.kickbox.com/accounts/GelrCwkY/verify/api
API key: test_2b2aef53aee36dba0ce05a17fdf6c20e0b772674edb1218e7a5972c5aa369d2c

Need for this project:
Email validation and verification
Username validation
Password length check
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

def verifyPasword(pas):
    if len(pas) < 8:
        return False
    else:
        for i in range(len(pas)):
            if pas[i].isupper():
                return True
            else:
                return False
# add number checker
