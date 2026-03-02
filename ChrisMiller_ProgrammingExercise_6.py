import re


def is_valid_phone_number(phone: str) -> bool:
    """
    Validate a US phone number using a flexible regular expression.

    Accepts common North American formats including:
    - 123-456-7890
    - (123) 456-7890
    - 1234567890
    - 123.456.7890
    - +1 123-456-7890
    - 1-123-456-7890
    - (123)456-7890

    Parameters
    ----------
    phone : str
        The phone number string to validate (may contain spaces, parentheses, dots, dashes)

    Returns
    -------
    bool
        True if the input matches a valid US phone number pattern, False otherwise

    Examples
    --------
    >>> is_valid_phone_number("123-456-7890")
    True
    >>> is_valid_phone_number("+1 (555) 123-4567")
    True
    >>> is_valid_phone_number("1234567890")
    True
    >>> is_valid_phone_number("123-45-6789")   # looks like SSN
    False
    >>> is_valid_phone_number("+44 20 7946 0958")  # UK number
    False
    """
    phone = phone.strip()
    pattern = r'^(?:\+?1[-.\s]?)?(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}$'
    return bool(re.match(pattern, phone))


def is_valid_ssn(ssn: str) -> bool:
    """
    Validate a United States Social Security Number (SSN) format and basic rules.

    Supports:
    - XXX-XX-XXXX
    - XXXXXXXXX
    - XXX XX XXXX  (spaces)

    Invalid cases caught:
    - Area numbers 000, 666, 900–999
    - Group number 00
    - Serial number 0000

    Parameters
    ----------
    ssn : str
        The SSN string to validate

    Returns
    -------
    bool
        True if format and basic validity rules are satisfied, False otherwise

    Examples
    --------
    >>> is_valid_ssn("123-45-6789")
    True
    >>> is_valid_ssn("078051120")
    True
    >>> is_valid_ssn("000-12-3456")
    False
    >>> is_valid_ssn("666-55-4444")
    False
    >>> is_valid_ssn("987-65-4321")
    True
    >>> is_valid_ssn("123-00-4567")
    False
    """
    ssn = ssn.strip()
    pattern = r'^(?!000|666|9\d{2})\d{3}[- ]?(?!00)\d{2}[- ]?(?!0000)\d{4}$'
    return bool(re.match(pattern, ssn))


def is_valid_zip_code(zip_code: str) -> bool:
    """
    Validate a United States ZIP Code (5 digit or ZIP 4 format).

    Accepted formats:
    - 12345
    - 12345-6789

    Parameters
    ----------
    zip_code : str
        The ZIP code string to validate

    Returns
    -------
    bool
        True if the input is a valid 5 digit or 5+4 ZIP code format, False otherwise

    Examples
    --------
    >>> is_valid_zip_code("90210")
    True
    >>> is_valid_zip_code("33101-1234")
    True
    >>> is_valid_zip_code("00501")
    True
    >>> is_valid_zip_code("1234")
    False
    >>> is_valid_zip_code("12345-678")
    False
    >>> is_valid_zip_code("12345-67890")
    False
    """
    zip_code = zip_code.strip()
    pattern = r'^\d{5}(?:-\d{4})?$'
    return bool(re.match(pattern, zip_code))


def validate_input(phone: str, ssn: str, zip_code: str) -> dict:
    """
    Convenience function that validates all three inputs at once.

    Parameters
    ----------
    phone : str
        Phone number string
    ssn : str
        Social Security Number string
    zip_code : str
        ZIP code string

    Returns
    -------
    dict
        Dictionary with validation results:
        {
            "phone": bool,
            "ssn": bool,
            "zip_code": bool
        }
    """
    return {
        "phone": is_valid_phone_number(phone),
        "ssn": is_valid_ssn(ssn),
        "zip_code": is_valid_zip_code(zip_code)
    }


def main() -> None:
    """
    Interactive command line interface for validating phone numbers, SSNs, and ZIP codes.

    Repeatedly prompts the user for input until an empty phone number is entered.
    Displays validation results for each set of inputs.

    Returns
    -------
    None
    """
    print("=== US Data Validator (Phone / SSN / ZIP) ===\n")
    print("Leave phone number blank and press Enter to quit.\n")

    while True:
        phone = input("Phone number: ").strip()
        if not phone:
            print("\nExiting validator.\n")
            break

        ssn = input("SSN (XXX-XX-XXXX or XXXXXXXXX): ").strip()
        zip_code = input("ZIP Code (12345 or 12345-6789): ").strip()

        results = validate_input(phone, ssn, zip_code)

        print("\nValidation Results:")
        print(f"  Phone     : {phone:20} → {'VALID' if results['phone'] else 'INVALID'}")
        print(f"  SSN       : {ssn:20} → {'VALID' if results['ssn'] else 'INVALID'}")
        print(f"  ZIP Code  : {zip_code:20} → {'VALID' if results['zip_code'] else 'INVALID'}")
        print("-" * 60)


def run_tests() -> None:
    """
    Execute a suite of unit style tests for all validation functions.

    Prints pass/fail status for each test case.

    Returns
    -------
    None
    """
    print("=== Validation Function Tests ===\n")

    phone_cases = [
        ("123-456-7890", True),
        ("(555) 867-5309", True),
        ("+12025550123", True),
        ("202-555-0191", True),
        ("5555555555", True),
        ("1-800-FLOWERS", False),
        ("+44 20 1234 5678", False),
        ("123-45-678", False),
    ]

    ssn_cases = [
        ("123-45-6789", True),
        ("078051120", True),
        ("987-65-4321", True),
        ("000-12-3456", False),
        ("666-55-1212", False),
        ("901-23-4567", False),
        ("123-00-9999", False),
        ("123-45-0000", False),
    ]

    zip_cases = [
        ("90210", True),
        ("10001-1234", True),
        ("00501", True),
        ("1234", False),
        ("123456", False),
        ("12345-67890", False),
        ("ABCDE", False),
    ]

    def run_test_set(name: str, func, cases):
        print(f"{name} tests:")
        for inp, expected in cases:
            result = func(inp)
            mark = "✓" if result == expected else "✗"
            print(f"  {inp:18} → {result}  {mark}")
        print()

    run_test_set("Phone", is_valid_phone_number, phone_cases)
    run_test_set("SSN", is_valid_ssn, ssn_cases)
    run_test_set("ZIP", is_valid_zip_code, zip_cases)

    print("Tests complete.")


if __name__ == "__main__":
    print("\n" + "═" * 70 + "\n")
    main()