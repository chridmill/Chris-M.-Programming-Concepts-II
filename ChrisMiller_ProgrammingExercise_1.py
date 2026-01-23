"""
Movie Ticket Pre-Sale
A console application to sell up to 20 movie tickets with a limit of 4 per buyer.
Asks users until all tickets are sold, then prints total buyers.
"""


def get_tickets(max_per_buyer: int, remaining_tickets: int) -> int:
    """
     Description
        asks the user for a valid number of tickets to buy and returns it after validation.

     Parameters
        - max_per_buyer: maximum tickets allowed per person
        - remaining_tickets: tickets still available for sale

     Variables used
        - tickets: user entered number of tickets
        - ask: str formatted input message

     Logical steps
        - Loop until valid input received
        - Get user input
        - Check if input is between 1 and max_per_buyer
        - Check if input does not exceed remaining_tickets
        - If valid return number
        - Otherwise print error message and repeat

     Return
         number of tickets the buyer wants
    """
    while True:
        try:
            ask = f"How many tickets would you like to buy (1-{max_per_buyer})? "
            tickets = int(input(ask))

            if tickets < 1 or tickets > max_per_buyer:
                print(f"Please enter a number between 1 and {max_per_buyer}.")
            elif tickets > remaining_tickets:
                print(f"Sorry, only {remaining_tickets} ticket(s) remaining.")
            else:
                return tickets

        except ValueError:
            print("Please enter a valid whole number.")


def sell_tickets() -> None:
    """
     Description
        Manages the ticket sale process until all tickets are sold.

     Parameters
        None

     Variables
        - TOTAL_TICKETS: constant (20) total tickets available
        - MAX_PER_BUYER: constant (4) max tickets per person
        - remaining_tickets: accumulator tracking unsold tickets
        - buyer_count: accumulator tracking number of buyers
        - tickets_bought: number of tickets bought in current iteration

     Logical steps
        - Initialize constants and accumulators (remaining_tickets = 20, buyer_count = 0)
        - Display welcome message and limits
        - While remaining_tickets > 0:
           - Call get_tickets() to get valid purchase amount
           - Subtract purchased tickets from remaining_tickets
           - Increment buyer_count
           - Show confirmation and updated remaining tickets
        - When loop ends → print sold-out message and final buyer count

     Return
        None (prints output)
    """
    TOTAL_TICKETS = 20
    MAX_PER_BUYER = 4

    remaining_tickets = TOTAL_TICKETS
    buyer_count = 0

    print("Welcome to Movie Ticket Pre-Sale!")
    print(f"Total tickets available: {TOTAL_TICKETS}")
    print(f"Limit: {MAX_PER_BUYER} tickets per person\n")

    while remaining_tickets > 0:
        tickets_bought = get_tickets(MAX_PER_BUYER, remaining_tickets)

        remaining_tickets -= tickets_bought
        buyer_count += 1

        print(f"Thank you! You bought {tickets_bought} ticket(s).")
        print(f"Tickets remaining: {remaining_tickets}\n")

    print("=== All tickets have been sold! ===")
    print(f"Total number of buyers: {buyer_count}")


if __name__ == "__main__":
    sell_tickets()