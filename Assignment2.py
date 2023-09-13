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
        return "Ticket Number: {self.ticket_number}" \
               "Ticket Creator: {self.ticket_creator_name}" \
               "Staff ID: {self.staff_id}" \
               "Email Address: {self.contact_email}" \
               "Description: {self.description}" \
               "Response: {self.response}" \
               "Ticket Status: {self.status}" \
               

def submit_ticket(tickets):
    ticket_creator_name = input("Enter your name: ")
    staff_id = input("Enter your Staff ID: ")
    contact_email = input("Enter your contact email: ")
    description = input("Enter a description of the issue: ")
    ticket = Ticket(ticket_creator_name, staff_id, contact_email, description)
    tickets.append(ticket)
    print(f"Ticket # has been submitted.\n")

def show_all_tickets(tickets):
    for ticket in tickets:
        print(ticket)

def respond_to_ticket(tickets):
    ticket_number = int(input("Enter the ticket number to respond to: "))
    for ticket in tickets:
        if ticket.ticket_number == ticket_number:
            response = input("Enter your response: ")
            ticket.provide_response(response)
            print("Ticket # has been responded to and closed.")
            return
        print("Ticket # has not been found")

    def main():
        tickets = []

    while True:
        print("Helpdesk Ticketing System")
        print("Select from the following options:")
        print("0. Exit")
        print("1. Submit helpdesk ticket")
        print("2. Show all tickets")
        print("3. Respond to ticket by number")
        print("4. Re-open received ticket")
        print("5. Display ticket state")

        choice = input("Enter menu selection 0 - 5: ")

        if choice == "0":
            break
        elif choice == "1":
            submit_ticket(tickets)
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