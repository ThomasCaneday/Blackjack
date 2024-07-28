# Blackjack Player vs Dealer

Python program for playing a simplified version of Blackjack where a player competes against the dealer. The game follows standard Blackjack rules, providing a straightforward and enjoyable experience.

## Features
- **Standard Rules:** Implements basic Blackjack rules including hitting and standing.
- **Interactive Gameplay:** Players can request another card (hit) or stop (stand).
- **Randomized Deck:** Utilizes a shuffled deck of 52 cards for an unpredictable and fair game.
- **Score Calculation:** Automatically calculates the scores for both the player and the dealer.

## Requirements
- Python 3.x

## How to Run
1. Clone this repository:
    ```sh
    git clone https://github.com/thomascaneday/blackjack.git
    ```
2. Navigate to the project directory:
    ```sh
    cd blackjack
    ```
3. Run the game:
    ```sh
    python blackjack.py
    ```

## How to Play
1. The game starts with the player and the dealer each being dealt two cards.
2. The player can choose to "hit" (request another card) or "stand" (stop).
3. If the player's score exceeds 21, the player loses.
4. The dealer will then draw cards until the dealer's score is at least 17.
5. The winner is determined based on the final scores:
    - Player wins if their score is higher than the dealer's without exceeding 21.
    - Dealer wins if the dealer's score is higher than the player's or if the player's score exceeds 21.
    - It's a tie if both scores are equal.

## Future Enhancements
- **Additional Features:** Implement advanced options like doubling down, splitting, and insurance.
- **Graphical User Interface (GUI):** Develop a GUI for a more interactive experience.
- **Multiplayer Mode:** Allow multiple players to play against the dealer.

## Contributions
Contributions are welcome! Please submit issues, fork the repository, and create pull requests to enhance the game.
