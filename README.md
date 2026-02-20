# Blackjack Game
A command-line implementation of Blackjack featuring hand splitting, betting, and standard casino rules.

## How to Run
```bash
python main.py
```

## File Structure

### `card.py`
*   Defines the `Card` class with rank, suit, and numerical value.
*   Assigns values to face cards (J, Q, K = 10) and a default value of 11 for Aces.
*   Includes a string representation method for easy printing (e.g., "K of Hearts").

### `game.py`
*   Manages `Deck`, `Player`, and `Dealer` classes, including shuffling and dealing mechanics.
*   Implements core logic for **splitting hands** and dynamic **Ace calculation** (converting 11 to 1 if over 21).
*   Contains the Dealer AI (hits until 17) and the logic to determine winners and payouts.

### `main.py`
*   Serves as the entry point, managing the game loop and user inputs (Hit, Stand, Split).
*   Enforces a **fixed bet of $50** per hand and handles immediate money deduction.
*   Manages multiple hands in a single turn (if a split occurs) and checks for player bankruptcy.