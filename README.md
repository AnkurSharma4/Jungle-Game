# Jungle Game

This is a simple text-based game implemented in Python, where the player makes choices to navigate through a jungle. Depending on the player's choices, the game either ends with a "Game Over" or a "Win." The game is controlled via console input and presents a series of decision points that lead to different outcomes.

## Features

- The game presents the player with choices at each step.
- The player can make decisions by entering numbers to move left, right, or interact with the game environment.
- The game has multiple endings based on the player's choices:
  - "Game Over"
  - "You Win!"

## Gameplay

- The game begins with a prompt to choose a direction (left or right).
- After each decision, the player is asked to make another choice.
- If the player takes the wrong path or makes an undesirable choice, the game ends with "Game Over."
- If the player makes the right choice at a critical point, they can win the game.

## Requirements

- Python 3.x

## How to Run the Game

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the folder where the `jungle_game.py` file is located.
4. Run the game using Python by typing:
   ```bash
   python jungle_game.py
   ```
5. Follow the on-screen prompts to play the game.

## Code Explanation

The game flow is as follows:

1. The game starts by printing "Jungle Game."
2. The player is asked to choose whether to go left (1) or right (2).
3. Depending on the choice, the game asks for additional inputs:
   - If the player goes left, they are asked to choose left (3) or right (4), both of which lead to a "Game Over."
   - If the player goes right, they are asked to choose left (2) or right (1). If they choose to go left, they encounter a stranger and can decide to accept help (1) or deny help (2).
   - If the player accepts the stranger's help, they win the game.
   - If the player denies help or chooses an invalid option, it results in a "Game Over."

## Example Gameplay

```
                                                     Jungle Game                                                    

Press 1 for left  |  Press 2 for right: 1
Press 3 for left  |  Press 4 for right: 3
Game Over
```

or

```
                                                     Jungle Game                                                    

Press 1 for left  |  Press 2 for right: 2
Press 1 for right  |  Press 2 for left: 2
Do you want to take help from this stranger?
Press 1 to take help  |  Press 2 to deny help: 1
You Win!
```

## License

This project is licensed under the MIT License

---

This README provides an overview of the game, its features, instructions for running it, and a brief code explanation. Feel free to edit or enhance it further depending on any additional functionality or changes you make to the code.
