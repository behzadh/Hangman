# Hangman Project Documentation Guideline

> Hangman Game is a game that asks the user for a letter and checks if it is in the word. It starts with a default number of lives and a random word from the word_list. The game is written under Hangman class in which includes three functions: initialization, ask a letter and check the letter.

## Milestone 1

- This project is written in a class method in order to organize each part of the game separately. This allows us to splite our project to smaller parts and make a better control on our code.

- In the first part of the code we initialized the attributes used in the game as following:
  
```python
"""
def __init__(self, word_list, num_lives=5):
    self.word_list = word_list
    self.num_lives = num_lives
    self.word = self.word_list[randint(0, len(self.word_list) - 1)]
    #self.num_letters = len(self.word)
    self.word_guessed = ['_'] * len(self.word)
    self.list_letters = []
    self.list_remaining_letters = list(self.word)
    print(f"The mystery word has {len(self.word)} characters")
    print(self.word_guessed)
    pass
"""
```

- This function initializes the attributes and prints out the first two sentences to  start the game:

```python
"""
The mystery word has 4 characters
['_', '_', '_', '_']
"""
```

## Milestone 2

- In this section, we are ready to start the game by asking the user to enter a valid single character. That's not always straightforward as a user can mistakenly enter multiple letters or not alphabetic letters. Therefore, we must define some conditions to avoid such mistakes.

```bash
1: It has to be a single character. 
2. It has to be a letter that has not been tried yet.
3: If the letter is valid, go to the next part.
```

- The above conditions are used to check whether the letter has been entered correctly by the user. Once confirmed, the letter will be checked with another function, so-called check_letter(), to see if the guessed letter is in the word. The result of this is below:

```python
"""
def ask_letter(self):
    letter = input('Please enter a letter -> ')
    while letter in self.list_letters: 
        print(f'{letter} was already tried or given')
        letter = input('Please, enter another character -> ')
    while len(letter) != 1: 
        letter = input('Please, enter just one character! -> ')
    if letter.isalpha: 
        self.list_letters.append(letter.lower())
        self.check_letter(letter.lower())
    else:
        pass
    return letter
"""
```

## Milestone 3

- The next session is to check if the guessed letter is in the guessed word. We need to follow these rules:
     -   If the letter is in the word, replace the '_' in the word_guessed list with the letter.
     -   If it is not, reduce the number of lives by one and, as a hint, visualise an additional part of the hangman. 

![image]([/Users/behzad/AiCore/hangman/hangman_scsh](https://github.com/behzadh/hangman/blob/Hangman_draft/hangman_scsh.png))

## Milestone 4

- The last part of our code is the play_game() function to put all steps above together to build the game. We need to iteratively ask the user for a letter until the user guesses the word or runs out of lives. In either case, the game will finish.

```python
"""
def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    while game.num_lives > 0:
        if '_' in game.word_guessed:
            game.ask_letter()
        if '_' not in game.word_guessed:
            print("Congratulations, you won!")
            break
        if game.num_lives == 0:
            print(f"You ran out of lives. The word was * {game.word} *")
    pass
"""
```

## Conclusions

- In this project, we designed the Hangman Game in which the program randomly picks up a word from a word list and asks the user to guess a letter and checks if it is in the word or not. The game continues until the user guess the word or runs out of lives.

- The command below allows you to start the game.

```bash
python hangman_solution.py
```
- Enjoy your game!
