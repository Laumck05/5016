def update_phone_number():
    phone_number = input("Enter your new phone number")
    print("Thank you for updating your phone number to: {phone_number}")

def update_email_address():
    email_address = input("Enter your new email address")
    print("Thank you for updating your email address to: {email_address}")

def update_address():
    address = input("Enter your new address")
    print("Thank you for updating your address to: {address}")

def request_call_back():
    print("Thank you for requesting a call back. We will be in touch soon")

def main():
    while True:
        print("Menu")
        print("0. Update phone number")
        print("1. Update email address")
        print("Update address")
        print("Request a call-back")