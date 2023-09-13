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

    def submit_ticket(tickets):
        ticket_creator_name = input("Enter your name: ")


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

        choice = input("Enter menu selection 0 - 5")

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