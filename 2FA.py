"""
https://www.geeksforgeeks.org/two-factor-authentication-using-google-authenticator-in-python/
"""

import time
import pyotp
import qrcode

key = "GeeksforGeeksIsBestForEverything"

uri = pyotp.totp.TOTP(key).provisioning_uri(
	name='Test',
	issuer_name='ThePhysicsLab')

print(uri)


# Qr code generation step
qrcode.make(uri).save("qr.png")

"""Verifying stage starts"""

totp = pyotp.TOTP(key)

# verifying the code
while True:
    print(totp.verify(input(("Enter the Code : "))))
