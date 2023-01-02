# Blackjack

This is a command-line version of a single game of Blackjack.

## Usage


1. Clone this Github repo or unzip the folder.
2. Open terminal of choice and cd into the Blackjack directory.
3. To run the application (user instructions available upon opening), enter (make sure you have python):
```bash
python main.py
```

## Repo Content
1. `README.md`:
Containing information about the repo and its usage.
2. `main.py`: Main file to handle user interactions of the game


## Summary & Approach & Challenges & Caveats
### Summary
The application is an attempt for the Freenome coding challenge. Specifically, it contains:
- All required basic functionalities as stated in the challenge.
- An easy to use UI with command-line of your choice.
- README and easy installations.
### Approach
About total of 1 hour to write the program
- I chose Python as it is a friendly language to program in a short time period.
- I spent 10-15 minutes reading the challenge then 30 minutes brainstorming the workflow.
- As a card deck problems, I used a list of numbers which represents the card symbols.
- I wrote seperate functions for actions like "hit", "hand", and "stand".
- Then I wrote the "play" function which will be called to start the game.

### Challenges
About total of 30 minutes to debug the program
- I had a lot of bugs regarding logics of my workflow like the order of prints and score calculation.
- I ran the program multiple times to make sure that I cover every case (blackjack, bust, etc)

### Caveats
The project can be improved given more time, for examples in some areas like:

- Testability: Currently, I don't have test files for the program due to limited of time. If I had more time, I would write automated test and unit tests.
  - Unit tests: test the functionality of every function in the main.py (given an input and check if the function yields expected output or does correct action)
  - Automated tests: mock the output of some functions with some mock library in python (I will need to take time looking on this) to cover corner cases and check if the output of the game is as expected
- Viability: Clean code and make sure there are no duplicate lines of code.
- Robustness: More extensive testing and design to bring more OOP or other design patterns (singleton) to increase robustness and maintenance ease.