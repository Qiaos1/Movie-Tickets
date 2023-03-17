"""Movie Theater Ticketing System - v4
Confirm Order
Created by Sarah Qiao
"""


# Component 4 - Confirm Order
def confirm_order(ticket, number, cost):
    confirm = ""
    while confirm != "Y" and confirm != "N":
      confirm = input(f"\nYou have ordered {number} {ticket} ticket(s)"
                      f"at a cost of ${cost * number:.2f}!\n"
                      f"'Y' or 'N': ").upper()
    if confirm == "Y":
        return True

    else:
        return False




    # Component 3 - Calculate Ticket Price
def get_price(type1):
    prices= [["A",12.5], ["C", 7], ["S", 9], ["G", 0]]
    for price in prices:
        if price[0] == type1:
            return price[1]


# Component 1 - Welcoming screen and set up variables
def sell_ticket():
    print("********** Fanfare Movies - ticketing system **********\n")

    adult_tickets = 0
    student_tickets = 0
    child_tickets = 0
    gift_tickets = 0
    tickets_sold = 0
    total_sold = 0

    # Component 2 - Get the category and number of tickets required

    ticket_wanted = "Y"
    while ticket_wanted == "Y":
        ticket_type = input("What kind of ticket do you want: \n"
                            "/t'A' for Adult, or\n"
                            "/t'S' for student, or\n"
                            "/t'C' for child, or\n"
                            "/t'G' for gift voucher\n"
                            ">> ").upper()
        num_tickets = int(input(f"How many {ticket_type} tickets do you want: "
                                f""))
        cost = get_price(ticket_type)

        if confirm_order(ticket_type, num_tickets, cost):
            print("Order confirmed")

            # Component 5 - Update Totals
            total_sold += cost * num_tickets
            tickets_sold += num_tickets
            if ticket_type == "A":
                adult_tickets += num_tickets
            elif ticket_type == "S":
                student_tickets += num_tickets
            elif ticket_type == "C":
                child_tickets += num_tickets
            else:
                gift_tickets += num_tickets


        else:
            print("Order Cancelled")

        ticket_wanted = input("Do you want to sell another ticket? (Y/N):"
                              "").upper()




# Main routine
sell_ticket()