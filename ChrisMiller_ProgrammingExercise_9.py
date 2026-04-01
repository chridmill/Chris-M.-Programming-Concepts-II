class BankAcct:
    """
    Represents a simple bank account with basic banking operations.

    Attributes (State Information):
        name (str): Full name of the account holder
        account_number (str): Unique account identifier
        amount (float): Current balance in the account
        interest_rate (float): Annual interest rate as a decimal (e.g. 0.045 for 4.5%)

    Methods:
        - deposit(), withdraw(), get_balance()
        - adjust_interest_rate()
        - calculate_interest()
        - __str__() for nice display
    """

    def __init__(self, name: str, account_number: str, initial_amount: float = 0.0, interest_rate: float = 0.0):
        """
        Initialize a new BankAcct object.

        Parameters
        ----------
        name : str
            Name of the account holder
        account_number : str
            Unique account number (string to support leading zeros or formats)
        initial_amount : float, optional
            Starting balance (default 0.0)
        interest_rate : float, optional
            Annual interest rate as decimal (default 0.0)
        """
        self.name = name.strip()
        self.account_number = account_number.strip()
        self.amount = max(0.0, float(initial_amount))  # prevent negative initial balance
        self.interest_rate = max(0.0, float(interest_rate))  # prevent negative interest rate

    def deposit(self, amount: float) -> bool:
        """
        Deposit money into the account.

        Parameters
        ----------
        amount : float
            Amount to deposit (must be positive)

        Returns
        -------
        bool
            True if deposit successful, False if amount is invalid
        """
        if amount > 0:
            self.amount += float(amount)
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw money from the account.

        Parameters
        ----------
        amount : float
            Amount to withdraw

        Returns
        -------
        bool
            True if withdrawal successful, False if insufficient funds or invalid amount
        """
        amount = float(amount)
        if amount > 0 and amount <= self.amount:
            self.amount -= amount
            return True
        return False

    def get_balance(self) -> float:
        """
        Return the current account balance.

        Returns
        -------
        float
            Current amount in the account
        """
        return self.amount

    def adjust_interest_rate(self, new_rate: float) -> bool:
        """
        Change the annual interest rate.

        Parameters
        ----------
        new_rate : float
            New annual interest rate as decimal (e.g. 0.035 for 3.5%)

        Returns
        -------
        bool
            True if rate was updated successfully, False if invalid rate
        """
        if new_rate >= 0:
            self.interest_rate = float(new_rate)
            return True
        return False

    def calculate_interest(self, days: int) -> float:
        """
        Calculate simple interest earned over a given number of days.

        Formula: Interest = Principal × Rate × Time
        where Time = days / 365

        Parameters
        ----------
        days : int
            Number of days to calculate interest for (must be positive)

        Returns
        -------
        float
            Interest amount earned (does NOT add it to the balance)
        """
        if days <= 0:
            return 0.0

        time_in_years = days / 365.0
        interest = self.amount * self.interest_rate * time_in_years
        return round(interest, 2)

    def __str__(self) -> str:
        """
        Return a nicely formatted string representation of the account.

        Used by print() and str() functions.

        Returns
        -------
        str
            Formatted account information including name, account number,
            balance, and current interest rate.
        """
        return (f"Bank Account\n"
                f"Name            : {self.name}\n"
                f"Account Number  : {self.account_number}\n"
                f"Balance         : ${self.amount:,.2f}\n"
                f"Interest Rate   : {self.interest_rate * 100:.2f}%")


def test_bank_account() -> None:
    """
    Test function that demonstrates and verifies all methods of the BankAcct class.

    Creates sample accounts and tests deposit, withdraw, interest calculation,
    rate adjustment, and string representation.

    Returns
    -------
    None
        Prints test results to console.
    """
    print("=== BankAcct Class Test ===\n")

    # Test 1: Create account
    acct = BankAcct("Chris Johnson", "987654321", 1250.75, 0.045)
    print("Account created:")
    print(acct)
    print("-" * 50)

    # Test 2: Deposit
    print("Depositing $500.00...")
    acct.deposit(500.00)
    print(f"New balance: ${acct.get_balance():,.2f}\n")

    # Test 3: Withdraw
    print("Withdrawing $200.00...")
    success = acct.withdraw(200.00)
    print(f"Withdrawal successful: {success}")
    print(f"New balance: ${acct.get_balance():,.2f}\n")

    # Test 4: Calculate interest for 30 days
    interest = acct.calculate_interest(30)
    print(f"Interest for 30 days at {acct.interest_rate * 100:.2f}%: ${interest:.2f}\n")

    # Test 5: Adjust interest rate
    print("Adjusting interest rate to 5.25%...")
    acct.adjust_interest_rate(0.0525)
    print(f"New interest rate: {acct.interest_rate * 100:.2f}%\n")

    # Test 6: Calculate interest again with new rate
    interest2 = acct.calculate_interest(365)
    print(f"Interest for 1 full year at new rate: ${interest2:.2f}\n")

    # Test 7: Invalid operations
    print("Testing invalid operations:")
    print(f"Withdraw $999999: {acct.withdraw(999999)}")
    print(f"Deposit negative amount: {acct.deposit(-100)}")
    print(f"Set negative rate: {acct.adjust_interest_rate(-0.01)}\n")

    print("Final account status:")
    print(acct)
    print("\n=== All tests completed ===")


if __name__ == "__main__":
    test_bank_account()