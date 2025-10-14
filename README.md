# BlackJack Game

A terminal-based BlackJack game written in Python with an automated dealer opponent.

## Overview

This is a simplified version of the classic casino card game BlackJack (also known as 21). Players compete against an automated dealer to get as close to 21 as possible without going over. The game features betting mechanics, rule explanations, and an engaging terminal interface with timed outputs for a more immersive experience.

## Features

- **Interactive Gameplay**: Choose to hit or stay as you build your hand
- **Automated Dealer**: Computer-controlled opponent with strategic logic
- **Betting System**: Place bets between $50 and $10,000
- **Rule Tutorial**: Optional in-game rules explanation for new players
- **Input Validation**: Robust error handling for user inputs
- **Paced Interface**: Timed outputs create a more engaging experience

## Game Rules

- Players start with two randomly dealt cards
- Goal: Get as close to 21 as possible without exceeding it
- **Hit**: Draw another card to increase your total
- **Stay**: Keep your current total and end your turn
- **Bust**: Going over 21 results in an automatic loss
- The dealer must hit if their total is below 16
- Winning doubles your bet amount

## Requirements

- Python 3.x
- Standard library modules (no external dependencies required):
  - `random`
  - `time`

## Installation

1. Clone or download this repository
2. Ensure Python 3.x is installed on your system
3. No additional packages need to be installed

## How to Run

```bash
python blackjack.py
```

Or if you're using Python 3 explicitly:

```bash
python3 blackjack.py
```

## How to Play

1. Run the program
2. Choose whether to read the rules or skip to gameplay
3. Place your bet (between $50 - $10,000)
4. Receive your initial two cards
5. Decide whether to hit (2) or stay (1)
6. The dealer plays automatically after you stay
7. The winner is determined based on final totals
8. If you win, collect double your bet!

## Game Mechanics

### Card Values
- Number cards (2-10): Face value
- Face cards (Jack, Queen, King): Worth 10 points
- Aces: Worth 11 points (simplified from standard BlackJack)

### Dealer Logic
- Dealer must hit if total is less than 16
- Dealer stays on 16 or higher
- Dealer can bust just like the player

### Winning Conditions
- Your total is higher than the dealer's (both under 22)
- Dealer busts while you're still in play
- If totals are equal, the game results in a tie

## Code Structure

- `main()`: Entry point, handles game flow and user interface
- `rules()`: Displays game rules to the player
- `bet()`: Handles betting input and validation
- `game()`: Core game logic including card dealing and turn management

## Future Enhancements

Potential improvements for future versions:
- Multi-round gameplay with running balance
- Ace flexibility (1 or 11 point value)
- Card splitting and doubling down
- Multiple deck support
- Save/load game state
- Difficulty levels for dealer strategy

## Author

**Matthew Wood**  
Email: Woodmatthewj522@aol.com

## Acknowledgments

This is one of my first Python programs. Thank you for playing!

## License

This project is open source and available for educational purposes.

---

*Enjoy the game and gamble responsibly (even if it's just for fun)!* 🎰
