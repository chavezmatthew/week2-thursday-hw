# 2. Python Programming Challenges for Customer Service Data Handling


# Objective: This assignment is designed to test and enhance your Python programming skills, focusing on real-world applications in customer service data management. You will practice correcting code, organizing customer data, and implementing a feedback system using Python dictionaries.

# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).

# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket  to "closed".
# Display all tickets.
#   (Bonus) filter by status


# Initialize with some sample tickets and include functionality for additional ticket entry.

# Example ticket structure:



import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

service_tickets = {
    1: {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    2: {"Customer": "Bob", "Issue": "Payment issue", "Status": "open"}
}

def next_id():
    # Function to return a new ID for a new service ticket
    last_id = max(service_tickets.keys()) if service_tickets else 0
    return last_id + 1

def new_ticket():
    new_id = next_id()
    while True:
        customer = input("Please enter the customer name: \n")
        issue = input("Please state the issue: \n")
        print(f"Customer: {customer}, Issue: {issue}")
        correct = input("Does this information look correct? (y/n) \n")
        if correct.lower() == 'y':
            # Create ticket
            service_tickets[new_id] = {'Customer': customer, 'Issue': issue, 'Status': 'open'}
            break
        else:
            # Go back to the top of the while loop (skip to the next iteration)
            clear()
            continue

def update_ticket():
    print ("Which ticket would you like to close? \n")
    for ticket_id, ticket_info in service_tickets.items():
        print(f"Ticket ID: {ticket_id}")
        print(f"Customer: {ticket_info['Customer']}")
        print(f"Issue: {ticket_info['Issue']}")
        print(f"Status: {ticket_info['Status']}")
        print("-" * 20)
    while True:
        try:
            ticket_id = int(input("Please enter the ticket ID to update status to closed: \n"))
            if ticket_id in service_tickets:
                service_tickets[ticket_id]['Status'] = 'closed'
                print(f"Ticket ID {ticket_id} has been updated to closed.")
                input("Press Enter to return to the main menu...")
                break
            else:
                print("Invalid ticket ID. Please enter a correct ticket ID.")
        except ValueError:
            print("Invalid input. Please enter a numeric ticket ID.")

def print_tickets():
    if not service_tickets:
        print("No tickets available.")
    else:
        for ticket_id, ticket_info in service_tickets.items():
            print(f"Ticket ID: {ticket_id}")
            print(f"Customer: {ticket_info['Customer']}")
            print(f"Issue: {ticket_info['Issue']}")
            print(f"Status: {ticket_info['Status']}")
            print("-" * 20)

def main():
    while True:
        ans = input('''
SERVICE TICKET MANAGER
Enter the corresponding number for the action you'd like to take:
    1 - Open a new service ticket.
    2 - Update the status of an existing ticket to "closed".
    3 - Display all tickets.
    4 - Quit \n
Please select an action: ''')
        if ans == '1':
            clear()
            new_ticket()  # Function to add a new ticket
        elif ans == '2':
            clear()
            update_ticket()  # Function to update an existing ticket
        elif ans == '3':
            clear()
            print_tickets()  # Function to display all tickets
            input("\nPress Enter to return to the main menu...")  
        elif ans == '4':
            print("Thanks for making service tickets and stuff like that. Have a good one!")
            break
        else:
            print("Please enter a valid number.")

main()