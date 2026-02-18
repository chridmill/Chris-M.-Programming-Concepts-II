# Monthly Expense Analyzer
# Chris
# February 18, 2026
# This program collects a user's monthly expenses (category and amount),
# then calculates and displays the total, highest, and lowest expenses.

def get_expenses():
    """
    Interactively collects monthly expense entries from the user.

    Prompts the user repeatedly for an expense category (type) and its amount.
    Collection stops when the user presses Enter without entering a category name.
    Validates that amounts are non-negative numbers.

    Returns:
        list[dict]: A list of expense records. Each record is a dictionary with:
                    - 'category': str – the name/type of expense
                    - 'amount': float – the monetary amount

    Raises:
        ValueError: Handled internally when user enters invalid (non-numeric) amount

    Side effects:
        Prints prompts and feedback messages to stdout.
        Handles input validation errors with user-friendly messages.
    """
    expenses = []

    print("Enter your monthly expenses.")
    print("When finished, just press Enter without typing a category.\n")

    while True:
        category = input("Expense type/category (or press Enter to finish): ").strip()

        # If user just presses Enter, stop collecting
        if not category:
            break

        try:
            amount = float(input(f"Amount for '{category}': $"))
            if amount < 0:
                print("Please enter a non-negative amount.\n")
                continue

            expenses.append({"category": category, "amount": amount})
            print()  # blank line for readability

        except ValueError:
            print("Invalid amount. Please enter a number.\n")

    return expenses


def calculate_total(expenses):
    """
    Computes the sum of all expense amounts using functools.reduce.

    Parameters:
        expenses (list[dict]): List of expense dictionaries, each containing
                               at least an 'amount' key with a numeric value.

    Returns:
        float: The total sum of all expense amounts.
               Returns 0.0 if the list is empty.

    Example:
        >>> calculate_total([{'amount': 50.0}, {'amount': 120.75}])
        170.75
    """
    from functools import reduce
    if not expenses:
        return 0.0
    return reduce(lambda acc, exp: acc + exp["amount"], expenses, 0.0)


def find_highest_expense(expenses):
    """
    Finds the expense record with the highest amount using functools.reduce.

    Parameters:
        expenses (list[dict]): List of expense dictionaries. Each must contain
                               'category' (str) and 'amount' (float/int) keys.

    Returns:
        dict | None: The complete dictionary of the highest expense
                     (with 'category' and 'amount'), or None if list is empty.

    Raises:
        IndexError: Avoided by checking for empty list first
    """
    from functools import reduce
    if not expenses:
        return None
    return reduce(
        lambda max_exp, current: current if current["amount"] > max_exp["amount"] else max_exp,
        expenses,
        expenses[0]  # starting point
    )


def find_lowest_expense(expenses):
    """
    Finds the expense record with the lowest amount using functools.reduce.

    Parameters:
        expenses (list[dict]): List of expense dictionaries. Each must contain
                               'category' (str) and 'amount' (float/int) keys.

    Returns:
        dict | None: The complete dictionary of the lowest expense
                     (with 'category' and 'amount'), or None if list is empty.
    """
    from functools import reduce
    if not expenses:
        return None
    return reduce(
        lambda min_exp, current: current if current["amount"] < min_exp["amount"] else min_exp,
        expenses,
        expenses[0]  # starting point
    )


def display_results(expenses):
    """
    Displays a formatted summary of the expense analysis.

    Shows:
    - Total expenses
    - Highest single expense (amount + category)
    - Lowest single expense (amount + category)

    Parameters:
        expenses (list[dict]): List of expense records from get_expenses()

    Returns:
        None: Output is printed to stdout only.

    Side effects:
        Prints a formatted report to the console.
        Handles empty list case with a message.
    """
    if not expenses:
        print("\nNo expenses were entered.")
        return

    total = calculate_total(expenses)
    highest = find_highest_expense(expenses)
    lowest = find_lowest_expense(expenses)

    print("\n" + "=" * 40)
    print("MONTHLY EXPENSE SUMMARY")
    print("=" * 40)
    print(f"Total expenses:          ${total:,.2f}")
    print(f"Highest expense:         ${highest['amount']:.2f} ({highest['category']})")
    print(f"Lowest expense:          ${lowest['amount']:.2f} ({lowest['category']})")
    print("=" * 40)


def main():
    """
    Main program entry point and control flow.

    Coordinates:
    1. Collecting expenses from the user
    2. Displaying the analysis results

    Returns:
        None
    """
    expenses_list = get_expenses()
    display_results(expenses_list)


# Program entry point
if __name__ == "__main__":
    main()