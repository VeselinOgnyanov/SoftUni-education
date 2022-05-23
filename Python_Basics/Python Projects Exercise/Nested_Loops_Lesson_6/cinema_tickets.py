command = input()
student_counter = 0
standard_counter = 0
kid_counter = 0
current_tickets = 0
seats_are_full = False
total_tickets_sold = 0

while command != "Finish":
    free_seats = int(input())
    ticket_type = input()
    while ticket_type != "End":
        if ticket_type == "student":
            student_counter += 1
        elif ticket_type == "standard":
            standard_counter += 1
        else:
            kid_counter += 1
        current_tickets += 1
        total_tickets_sold += 1
        if current_tickets == free_seats:
            seats_are_full = True
            break
        ticket_type = input()
    perc = current_tickets / free_seats * 100
    print(f"{command} - {perc:.2f}% full.")
    current_tickets = 0
    command = input()
perc_student = student_counter / total_tickets_sold * 100
perc_standard = standard_counter / total_tickets_sold * 100
perc_kid = kid_counter / total_tickets_sold * 100
print(f"Total tickets: {total_tickets_sold}")
print(f"{perc_student:.2f}% student tickets.")
print(f"{perc_standard:.2f}% standard tickets.")
print(f"{perc_kid:.2f}% kids tickets.")

