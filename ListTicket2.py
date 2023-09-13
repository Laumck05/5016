class Ticket:
    def __init__(self, ticket_number, description):
        self.ticket_number = ticket_number
        self.description = description

    def __str__(self):
        return f"Ticket Number: {self.ticket_number}\nDescription: {self.description}\n"
    
def main():
    # Create a list of ticket objects
    ticket_list = []

    #Add some tickets to the list
    ticket1 = Ticket(1, "Issue with email")
    ticket2 = Ticket(2, "Network connectivity problem")
    ticket3 = Ticket(3, "Software installation request")

    ticket_list.append(ticket1)
    ticket_list.append(ticket2)
    ticket_list.append(ticket3)

    #Display the list of tickets
    print("List of Tickets:\n")
    for ticket in ticket_list:
        print(ticket)

if __name__ == "__main__":
    main()