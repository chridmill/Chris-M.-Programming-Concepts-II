import random


class Deck:
    """
    Deck class based on Section 11.5 of Supercharged Python.
    Uses numbers 0-51 internally and converts to rank/suit when needed.
    """

    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['♣', '♦', '♥', '♠']  # Clubs, Diamonds, Hearts, Spades

    def __init__(self, size: int = 52):
        """Initialize and shuffle a new deck."""
        self.card_list = [i for i in range(size)]
        self.cards_in_play = []  # cards currently dealt
        random.shuffle(self.card_list)

    def deal(self):
        """Deal one card (returns a number 0-51)."""
        if len(self.card_list) < 1:
            print("Reshuffling...")
            self.card_list = self.cards_in_play[:]
            random.shuffle(self.card_list)
            self.cards_in_play = []

        card = self.card_list.pop(0)
        self.cards_in_play.append(card)
        return card

    def get_card_name(self, card_num: int) -> str:
        """Convert card number (0-51) to rank + suit string."""
        rank = self.ranks[card_num % 13]
        suit = self.suits[card_num // 13]
        return f"{rank}{suit}"


# ====================== Game Functions ======================

def deal_poker_hand(deck: Deck) -> list[int]:
    """
    Deal a 5-card poker hand. Returns list of card numbers.
    """
    hand = []
    for _ in range(5):
        hand.append(deck.deal())
    return hand


def display_hand(hand: list[int], deck: Deck, title: str = "Your Hand"):
    """Display the hand with position numbers."""
    print(f"\n{title}:")
    for i, card_num in enumerate(hand, 1):
        print(f"  {i}) {deck.get_card_name(card_num)}")
    print()


def get_cards_to_replace() -> list[int]:
    """
    Get positions (1-5) of cards the player wants to replace.
    """
    while True:
        inp = input("Enter positions to replace (e.g. 1 3 5) or press Enter to keep all: ").strip()

        if not inp:
            return []

        try:
            positions = [int(x) for x in inp.replace(',', ' ').split()]
            if all(1 <= p <= 5 for p in positions) and len(set(positions)) == len(positions):
                return sorted(positions)
            else:
                print("Please enter numbers between 1 and 5 (no duplicates).")
        except ValueError:
            print("Invalid input. Please use numbers only.")


def replace_cards(hand: list[int], positions: list[int], deck: Deck):
    """Replace cards at given positions with new ones from the deck."""
    for pos in positions:
        hand[pos - 1] = deck.deal()


def main():
    """Main program for 5-Card Draw Poker."""
    print("=== 5-Card Draw Poker (Section 11.5 Deck) ===\n")

    deck = Deck(52)

    # Initial deal
    hand = deal_poker_hand(deck)
    display_hand(hand, deck, "Your Initial Hand")

    # Draw phase
    to_replace = get_cards_to_replace()

    if to_replace:
        replace_cards(hand, to_replace, deck)
        display_hand(hand, deck, "Your Final Hand")
    else:
        print("You kept your original hand.")

    print("Thanks for playing!")


if __name__ == "__main__":
    main()