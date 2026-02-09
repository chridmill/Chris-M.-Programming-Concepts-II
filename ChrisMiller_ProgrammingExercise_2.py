# spam_detector.py
# Chris's Spam Email Checker
"""
Spam Detector Program
Assignment: Detect spam in email messages using keyword matching

This program:
1. Contains a list of 30 common spam words/phrases
2. Asks the user to enter an email message
3. Counts occurrences of each spam term (case-insensitive)
4. Calculates a spam score (1 point per occurrence)
5. Determines spam likelihood based on the score
6. Shows the score, likelihood rating, and which words/phrases were found

Author: Chris
Date: February 2025
"""
# List of 30 common suspicious spam words and phrases
suspicious_words = ["free", "win", "winner", "congratulations", "cash", "money",
                    "discount", "buy now", "click here", "urgent", "act now",
                    "limited time", "guarantee", "viagra", "weight loss",
                    "million dollars", "opportunity", "risk free", "no cost",
                    "exclusive", "best deal", "extra income", "work from home",
                    "as seen on", "order now", "special offer", "clearance",
                    "pure profit", "be your own boss", "financial freedom"]


def get_user_message():
    """
    Collects the email message from the user.

    The user can paste or type multiple lines of text.
    Input ends when the user presses Enter on a blank line.

    Returns:
        str: The complete email message as one string.
    """
    print("Type or paste the email message here.")
    print("When finished, press Enter two times (empty line).\n")

    message = ""
    while True:
        line = input()
        if line == "":
            break
        message = message + " " + line

    return message


def check_for_spam(message):
    """
    Scans the message for suspicious spam keywords.

    This function:
    1. Converts message to lowercase
    2. Counts how many times each spam word appears
    3. Builds a total score (points = total matches)
    4. Keeps track of which words were found and how often

    Parameters:
        message (str): The email text to check

    Returns:
        tuple: (int score, list of strings describing found words)
    """
    # make everything lowercase
    message_low = message.lower()

    score = 0
    found_list = []

    i = 0
    while i < len(suspicious_words):
        word = suspicious_words[i]
        how_many = message_low.count(word)

        if how_many > 0:
            score = score + how_many
            found_list.append(word + " (" + str(how_many) + " times)")

        i = i + 1

    return score, found_list


# --- Main program starts here ---

print("Welcome to Spam Checker.\n")

# Get the message using the first function
full_message = get_user_message()

if full_message == "":
    print("You didn't enter a message. Goodbye.")
else:
    # Use the second function to check for spam
    spam_score, suspicious_found = check_for_spam(full_message)

    # Decide what to say about the score
    if spam_score == 0:
        result = "Probably not spam."
    elif spam_score <= 3:
        result = "Unlikely Spam."
    elif spam_score <= 7:
        result = "Suspicious!"
    else:
        result = "This is probably SPAM!!!"

    # Show the results
    print("")
    print("---------------------")
    print("Spam Score:", spam_score)
    print("Result:", result)

    if len(suspicious_found) > 0:
        print("")
        print("Suspicious words:")
        j = 0
        while j < len(suspicious_found):
            print(" - " + suspicious_found[j])
            j = j + 1
    else:
        print("No suspicious words or phrases found.")

    print("---------------------")
    print("Complete")

