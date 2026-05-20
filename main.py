from repository.ticket_management import TicketManagement
from exception.ticket_not_found_exception import TicketNotFoundException

def main():
    tm = TicketManagement()

    while True:
        print("\n1. Add ticket")
        print("2. Update priority")
        print("3. Delete ticket")
        print("4. View all tickets")
        print("5. Search by employee name and status")
        print("6. Filter by excluding issue type and maximum priority")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            employee_name = input("Enter employee name: ").strip()
            issue_type = input("Enter issue type: ").strip()
            try:
                priority = int(input("Enter priority: ").strip())
            except ValueError:
                print("Invalid priority. Please enter an integer.")
                continue
            raised_date = input("Enter raised date (YYYY-MM-DD): ").strip()
            status = input("Enter status: ").strip()
            result = tm.add_ticket(employee_name, issue_type, priority, raised_date, status)
            if result:
                print("Ticket added successfully.")
            else:
                print("Failed to add ticket.")

        elif choice == "2":
            try:
                ticket_id = int(input("Enter ticket ID: ").strip())
                priority = int(input("Enter new priority: ").strip())
            except ValueError:
                print("Invalid input. Please enter integers.")
                continue
            try:
                tm.update_priority(ticket_id, priority)
                print("Priority updated successfully.")
            except TicketNotFoundException as e:
                print(e)

        elif choice == "3":
            try:
                ticket_id = int(input("Enter ticket ID: ").strip())
            except ValueError:
                print("Invalid ticket ID. Please enter an integer.")
                continue
            try:
                tm.delete_ticket(ticket_id)
                print("Ticket deleted successfully.")
            except TicketNotFoundException as e:
                print(e)

        elif choice == "4":
            tickets = tm.get_all_tickets()
            if not tickets:
                print("No tickets found.")
            else:
                for ticket in tickets:
                    print(ticket)

        elif choice == "5":
            employee_name = input("Enter employee name: ").strip()
            status = input("Enter status: ").strip()
            try:
                tickets = tm.search_by_employee_and_status(employee_name, status)
                for ticket in tickets:
                    print(ticket)
            except TicketNotFoundException as e:
                print(e)

        elif choice == "6":
            excluded_issue = input("Enter issue type to exclude: ").strip()
            try:
                max_priority = int(input("Enter maximum priority: ").strip())
            except ValueError:
                print("Invalid priority. Please enter an integer.")
                continue
            tickets = tm.filter_exclude_issue_and_priority(excluded_issue, max_priority)
            if not tickets:
                print("No tickets match the filter criteria.")
            else:
                for ticket in tickets:
                    print(ticket)

        elif choice == "7":
            print("Exiting...")
            tm.close_connection()
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
