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

        choice = input("Enter a number 0 - 3 to select an option, or 'q' to quit.")

        if choice == '0':
            update_phone_number()
        elif choice == '1':
            update_email_address()
        elif choice == '2':
            update_address()
        elif choice == '3':
            request_call_back()
        elif choice == 'q':
            print("Thank you for using this service.")
            break
        
if __name__ == "__main__":
    main()
