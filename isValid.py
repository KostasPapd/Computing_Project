import re
import kickbox

def validEmail(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9]+(\.[A-Z|a-z]{2,})+')

    if re.fullmatch(regex, email):
        return True
    else:
        return False


def verifyEmail(email):
    client = kickbox.Client("test_2b2aef53aee36dba0ce05a17fdf6c20e0b772674edb1218e7a5972c5aa369d2c")  # API key
    kick = client.kickbox()

    res = kick.verify(email)

    if res.body['result'] != "undeliverable":
        return True
    else:
        return False

def validatePassword(pas):
    if re.fullmatch(r'[A-Za-z0-9!@_&]{8,}', pas):  # Sets what characters are allowed and required in the password
        # Checks if all the required characters are in the password
        if not any(char.isupper() for char in pas):
            return False
        elif not any(char.islower() for char in pas):
            return False
        elif not any(char.isdigit() for char in pas):
            return False
        elif len(pas) < 8:
            return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    # Testing
    # print(validatePassword("password"))
    # print(validEmail("b32908@sfc.potteries.ac.uk"))
    # print(verifyEmail("b32908@sfc.potteries.ac.uk"))
    pass
