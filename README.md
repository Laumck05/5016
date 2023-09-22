# Software Project -  Helpdesk Ticketing System

## Overview

This Python script provides an implementation of a Helpdesk Ticketing System. The system allows staff members to submit Helpdesk tickets, including password change requests, and provides functionalities to respond to tickets, reopen them, and display ticket statistics.

## Functionality

### Ticket Class

- The `Ticket` class represents a helpdesk ticket and includes the following attributes:

  - Ticket number
  - Ticket creator name
  - Staff ID
  - Contact email
  - Description of the issue
  - Response from the IT department
  - Ticket status (open, closed, or reopened)

- The class includes methods to:

  - Provide a response to a ticket (closes the ticket)
  - Reopen a closed ticket

### Password Change

- The system handles password change requests:
  - If a ticket's description contains "Password Change," a new password is generated based on specific rules.
  - The new password is displayed, and the ticket is closed.
- The password is created by joining the first 2 characters of the staff ID number, followed by the first 3 characters of the ticket creator’s name.

### Submitting Tickets

- Users can submit tickets by providing necessary information, including staff ID, name, email, and a description of the issue.
- The system automatically assigns a unique ticket number.
- Password change requests are handled differently, as described above.

### Displaying Tickets

- Users can view all submitted tickets, including their details.
- Ticket details are displayed in the same structured format as they are submitted (name, staff ID, email, issue description, and ticket state)

### Responding to Tickets

- IT department members can respond to tickets by providing a note advising the action taken.
- After responding, the ticket is marked as closed, reducing the count of open tickets and increasing the count of closed tickets.

### Reopening Tickets

- IT department members can reopen closed tickets if needed.
- Reopening a ticket changes its status to "Reopened," reducing the count of closed tickets and increasing the count of open tickets.

### Ticket Statistics

- The system keeps track of the following ticket statistics:
  - Total number of tickets created
  - Number of resolved (closed) tickets
  - Number of open (active) tickets

- Users can view these statistics at any time.

## Usage

1. Run the script by executing `python software_project.py` in your terminal.

2. Choose from the following options:
   - Submit a helpdesk ticket
   - Show all tickets
   - Respond to a ticket by number
   - Reopen a received ticket
   - Display ticket state
   - Exit
  
## Menu Options

Choose from the following menu options:

   - `1. Submit helpdesk ticket`: Submit a new helpdesk ticket.
   - `2. Show all tickets`: Display all submitted tickets.
   - `3. Respond to ticket by number`: Respond to an existing ticket.
   - `4. Re-open received ticket`: Reopen a closed ticket.
   - `5. Display ticket state`: View ticket statistics.

## Example Usage

Below is an example of how the system displays ticket statistics and ticket information:

   ```plaintext
  - Displaying Ticket Statistics

   Tickets Created: 3
   Tickets Resolved: 1
   Tickets To Solve: 2

  - Printing Tickets:

   Ticket Number: 2001
   Ticket Creator: Inna
   Staff ID: INNAM
   Email Address: inna@whitecliffe.co.nz
   Description: My monitor stopped working
   Response: Not Yet Provided
   Ticket Status: Open

   Ticket Number: 2002
   Ticket Creator: Maria
   Staff ID: MARIAH
   Email Address: maria@whitecliffe.co.nz
   Description: Request for a videocamera to conduct webinars
   Response: Not Yet Provided
   Ticket Status: Open

   Ticket Number: 2003
   Ticket Creator: John
   Staff ID: JOHNS
   Email Address: john@whitecliffe.co.nz
   Description: Password change
   Response: New password generated: JOJoh
   Ticket Status: Closed

  - Displaying Ticket Statistics

   Tickets Created: 3
   Tickets Resolved: 2
   Tickets To Solve: 1

  - Printing Tickets:

   Ticket Number: 2001
   Ticket Creator: Inna
   Staff ID: INNAM
   Email Address: inna@whitecliffe.co.nz
   Description: My monitor stopped working
   Response: The monitor has been replaced.
   Ticket Status: Closed

   Ticket Number: 2002
   Ticket Creator: Maria
   Staff ID: MARIAH
   Email Address: maria@whitecliffe.co.nz
   Description: Request for a videocamera to conduct webinars
   Response: Not Yet Provided
   Ticket Status: Open


## Requirements

- Python 3.x

## Author

Laura Mckinnon
