"""Movie Theater Ticketing System - v3
Calculate Ticket Price
Created by Sarah Qiao
"""

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

        print(f"\nYou have ordered {num_tickets} {ticket_type} ticket(s)"
              f"at a cost of ${cost * num_tickets:.2f}!")
        ticket_wanted = input("Do you want to sell another ticket? (Y/N):"
                              "").upper()




# Main routine
sell_ticket()