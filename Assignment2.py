import random
import string

class Ticket:
    counter = 1

    def __init__(self, ticket_creator_name, staff_id, contact_email, description):
        self.ticket_number = Ticket.counter + 2000
        self.ticket_creator_name = ticket_creator_name
        self.staff_id = staff_id
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"
        Ticket.counter += 1

    def provide_response(self, response):
        self.response = response
        self.status = "Closed"

    def reopen_ticket(self):
        self.status = "Reopened"

    def __str__(self):
        return f"Ticket Number: {self.ticket_number}\n" \
               f"Ticket Creator: {self.ticket_creator_name}\n" \
               f"Staff ID: {self.staff_id}\n" \
               f"Email Address: {self.contact_email}\n" \
               f"Description: {self.description}\n" \
               f"Response: {self.response}\n" \
               f"Ticket Status: {self.status}\n" 
               
def generate_random_password():
    # Generate a random password with 8 characters (uppercase, lowercase, digits)
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(8))
    return password

def submit_ticket(tickets):
    while True:
        ticket_creator_name = input("Enter your name: ")
        staff_id = input("Enter your Staff ID: ")
        contact_email = input("Enter your contact email: ")
        
        # Prompt the user to enter "password change" before entering the description
        description_prompt = "If you require a new password, type: password change\nEnter a description of the issue: "
        description = input(description_prompt)

        if "password change" in description.lower():
            new_password = generate_random_password()
            print(f"New password generated: {new_password}")
            response = f"New password generated: {new_password}"
            ticket = Ticket(ticket_creator_name, staff_id, contact_email, description)
            ticket.provide_response(response)
        else:
            ticket = Ticket(ticket_creator_name, staff_id, contact_email, description)
            tickets.append(ticket)
            print(f"Ticket #{ticket.ticket_number} has been submitted.\n")

        another_issue = input("Do you have another issue to submit? (Y/N): ").strip().lower()
        if another_issue != 'y':
            break

def show_all_tickets(tickets):
    for ticket in tickets:
        print(ticket)

def respond_to_ticket(tickets):
    while True:
        ticket_number = int(input("Enter the ticket number to respond to: "))

        found_ticket = None 
        for ticket in tickets:
            if ticket.ticket_number == ticket_number:
                found_ticket = ticket
                break

        if found_ticket:
            response = input("Enter your response: ")
            found_ticket.provide_response(response)
            print(f"Ticket #{ticket_number} has been responded to and closed.\n")
            break
        else:
            print(f"Ticket #{ticket_number} has not been found")

def reopen_received_ticket(tickets):
    while True:
        ticket_number = int(input("Enter the ticket number to reopen: "))
        found_ticket = None

        for ticket in tickets:
            if ticket.ticket_number == ticket_number:
                found_ticket = ticket
                break

        if found_ticket:
            if found_ticket.status == "Closed":
                found_ticket.reopen_ticket()
                print(f"Ticket #{ticket_number} has been reopened.\n")
                break
            else:
                print(f"Ticket #{ticket_number} cannot be reopened because it is not in a closed state.\n")
        else:
            print(f"Ticket #{ticket_number} not found.\n")

def display_ticket_state(tickets):
    print(f"Tickets Created: {len(tickets)}")
    print(f"Tickets Resolved: {len([ticket for ticket in tickets if ticket.status == 'Closed'])}")
    print(f"Tickets to Action: {len([ticket for ticket in tickets if ticket.status == 'Open'])}")

def main():
    tickets = []

    while True:
        print("Helpdesk Ticketing System")
        print("\n*******************************\n")
        print("Select from the following options:")
        print("0. Exit")
        print("1. Submit helpdesk ticket")
        print("2. Show all tickets")
        print("3. Respond to ticket by number")
        print("4. Re-open received ticket")
        print("5. Display ticket state")
        print("\n*******************************\n")

        choice = input("Enter menu selection 0 - 5: ")

        if choice == "0":
            break
        elif choice == "1":
            while True:
                submit_ticket(tickets)
                another_problem = input("Do you have another issue to submit? (Y/N): ").strip().lower()
                if another_problem !='y':
                    break
        elif choice == "2":
            show_all_tickets(tickets)
        elif choice == "3":
            respond_to_ticket(tickets)
        elif choice == "4":
            reopen_received_ticket(tickets)
        elif choice == "5":
            display_ticket_state(tickets)
        else:
            print("Invalid selection. Please choose a valid option.\n")

if __name__ == "__main__":
    main ()