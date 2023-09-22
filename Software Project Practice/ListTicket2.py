class Ticket:
    def __init__(self, ticket_number, name, email, description):
        self.ticket_number = ticket_number
        self.name = name
        self.email = email
        self.description = description

    def __str__(self):
        return f"Ticket Number: {self.ticket_number}\nName: {self.name}\nEmail: {self.email}\nDescription: {self.description}\n"
    
def is_valid_email(email):
    return "@" in email and "." in email  

def submit_ticket(ticket_list):
    ticket_number = len(ticket_list) + 1
    name = input("Enter your name: ")

    # Validate email input
    while True:
        email = input("Enter your email address: ")
        if is_valid_email(email):
            break
        else:
            print("Invalid email input. Please enter a valid email address.")

    description = input("Enter a description for the new ticket: ")
    new_ticket = Ticket(ticket_number, name, email, description)
    ticket_list.append(new_ticket)
    print (f"Ticket #{ticket_number} has been submitted.\n")

    
def main():
    # Create an empty list to store Ticket objects
    ticket_list = []

    while True:
        print("Menu:")
        print("0. Exit")
        print("1. Submit New Ticket")
        print("2. Display List of Tickets")

        choice = input("Enter your choice (0-2): ")

        if choice == '0':
            print ("Goodbye")
            break
        elif choice == '1':
            submit_ticket(ticket_list)
        elif choice == '2':
            print("List of Tickets:\n")
            for ticket in ticket_list:
                print(ticket)
        else:
            print("Invalid choice. Please enter a valid option (0-2).")

if __name__ == "__main__":
    main()