import re
import kickbox

def validEmail(email):
    """Validates the email address using regex"""
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9]+(\.[A-Z|a-z]{2,})+')

    if re.fullmatch(regex, email):
        return True
    else:
        return False


def verifyEmail(email):
    """Verifies the email address using the kickbox API"""
    client = kickbox.Client("live_ea4e6cd2f6835c4d2eede753063f312640099fb57d77a078a8ee802949945514")  # Passes the API key to the client
    kick = client.kickbox()
    res = kick.verify(email) # Verifies the email address

    if res.body['result'] == "deliverable" or res.body['result'] == "risky":
        return True
    else:
        return False

def validatePassword(pas):
    """Validates the password using regex"""
    if re.fullmatch(r'[A-Za-z0-9!@_&]{8,20}', pas):  # Sets what characters are allowed and required in the password
        # Checks if all the required characters are in the password
        if not any(char.isupper() for char in pas):
            return False
        elif not any(char.islower() for char in pas):
            return False
        elif not any(char.isdigit() for char in pas):
            return False
        elif not any(char in '!@_&' for char in pas):
            return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    # Testing
    # print(validatePassword("password"))
    # print(validEmail("b32908@sfc.potteries.ac.uk"))
    print(verifyEmail("b32908@uk.com"))
    pass
