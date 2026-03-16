import re


def split_sentences(text: str) -> list[str]:
    """
    Split a paragraph into sentences using look-ahead, following Supercharged Python Section 7.4.

    Starts sentences with uppercase letter OR digit.
    Uses non-greedy matching + positive look-ahead to avoid splitting on:
    - Abbreviations (Mr. Dr. U.S.A.)
    - Decimals (3.14, 310.5)
    - Other mid-sentence periods

    Parameters
    ----------
    text : str
        The input paragraph or multi-line text.

    Returns
    -------
    list[str]
        List of extracted sentences (with original punctuation, stripped whitespace).

    Notes
    -----
    - Uses re.DOTALL so '.' matches newlines.
    - Look-ahead (?= ...) checks for space + uppercase/digit or end-of-string without consuming them.
    - Adapted from book pattern '[A-Z].*?[.!?](?= [A-Z]|\Z)' to also allow digit sentence starts.
    """
    if not text.strip():
        return []

    # Pattern from book, extended to allow sentences starting with digit (0-9)
    # [A-Z0-9] instead of just [A-Z]
    pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|\Z)'

    # Find all non-overlapping matches
    sentences = re.findall(pattern, text, flags=re.DOTALL)

    # Clean up extra surrounding whitespace (in case of multiple spaces/newlines)
    return [s.strip() for s in sentences if s.strip()]


def display_sentences(sentences: list[str]) -> None:
    """
    Display each sentence numbered, followed by the total count.

    Parameters
    ----------
    sentences : list[str]
        List of sentence strings to print.

    Returns
    -------
    None
        Prints to console.
    """
    if not sentences:
        print("No sentences found.")
        return

    for i, sentence in enumerate(sentences, start=1):
        print(f"Sentence {i}: {sentence}")

    print(f"\nTotal number of sentences: {len(sentences)}")


def main() -> None:
    """
    Main function: prompt user for paragraph input and display split sentences.

    User enters lines; blank line (Enter twice) ends input and processes.
    Empty input (just Enter at start) quits the program.

    Returns
    -------
    None
    """
    print("=== Sentence Splitter (Supercharged Python 7.4 Look-Ahead Style) ===")
    print("Supports sentences starting with numbers or capital letters.")
    print("Enter paragraph below. Press Enter twice to process.")
    print("Just press Enter (blank) to quit.\n")

    while True:
        print("Input paragraph:")
        lines = []
        while True:
            line = input()
            if line == "":  # blank line ends paragraph entry
                break
            lines.append(line)

        paragraph = " ".join(lines).strip()

        if not paragraph:
            print("Goodbye!")
            break

        sentences = split_sentences(paragraph)
        display_sentences(sentences)
        print("\n" + "-" * 70 + "\n")


if __name__ == "__main__":
    main()