import pyotp
import random
import smtplib
from email.mime.text import MIMEText

class MFA:
    def __init__(self, user_email):
        self.user_email = user_email
        self.secret = pyotp.random_base32()

    def generate_totp(self):
        totp = pyotp.TOTP(self.secret)
        return totp.now()

    def verify_totp(self, user_input):
        totp = pyotp.TOTP(self.secret)
        return totp.verify(user_input)

    def send_sms_code(self, phone_number):
        code = random.randint(100000, 999999)
        print(f"Simulating SMS to {phone_number}: Your code is {code}")  # Simulate SMS
        return code

    def send_email_code(self):
        code = random.randint(100000, 999999)
        msg = MIMEText(f"Your MFA code is: {code}")
        msg['Subject'] = 'Your MFA Code'
        msg['From'] = 'no-reply@example.com'
        msg['To'] = self.user_email

        # Simulate email sending
        print(f"Simulating Email to {self.user_email}: Your code is {code}")
        return code

if __name__ == "__main__":
    user_email = input("Enter your email: ")
    phone_number = input("Enter your phone number: ")
    mfa = MFA(user_email)

    # TOTP Verification
    print("\n--- TOTP Authentication ---")
    totp_code = mfa.generate_totp()
    print(f"Generated TOTP: {totp_code}")  # In real use, show this in an authenticator app
    user_totp = input("Enter the TOTP code: ")
    print("TOTP Verified:" if mfa.verify_totp(user_totp) else "TOTP Verification Failed")

    # SMS Verification
    print("\n--- SMS Authentication ---")
    sms_code = mfa.send_sms_code(phone_number)
    user_sms = input("Enter the SMS code: ")
    print("SMS Verified:" if str(sms_code) == user_sms else "SMS Verification Failed")

    # Email Verification
    print("\n--- Email Authentication ---")
    email_code = mfa.send_email_code()
    user_email_code = input("Enter the Email code: ")
    print("Email Verified:" if str(email_code) == user_email_code else "Email Verification Failed")
