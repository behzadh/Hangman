'''
This code is written to design Hangman game. Hangman Game is a game that asks the user for a letter and checks if it is in the word.
@autor: Behzad -> with the help of AiCore team
'''
import random
from random import *

class Hangman:
    def __init__(self, word_list, num_lives=5):
        ## Initializing all attributes
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self.word_list[randint(0, len(self.word_list) - 1)]
        #self.num_letters = len(self.word)
        self.word_guessed = ['_'] * len(self.word)
        self.list_letters = []
        self.list_remaining_letters = list(self.word)
        print(f"The mystery word has {len(self.word)} characters")
        print(self.word_guessed)

    def ask_letter(self):
        ## This functions asks the user for a letter to start the game
        letter = input('Please enter a letter -> ')
        while letter in self.list_letters: 
            print(f'{letter} was already tried or given')
            letter = input('Please, enter another character -> ')
        while len(letter) != 1: 
            letter = input('Please, enter just one character! -> ')
        if letter.isalpha: 
            self.list_letters.append(letter.lower())
            self.check_letter(letter.lower())
    
    def check_letter(self, letter) -> None:
        ## This function checks if the letter is in the word. Each time the user lose live, the code provide a letter as a hint (see give_hintd() function)
        if letter.lower() in self.word:
            indexes = [pos for pos, char in enumerate(self.word) if char == letter]
            replacements = [letter] * len(indexes)
            for (index, replacement) in zip(indexes, replacements):
                self.word_guessed[index] = replacement
            print(f'Nice! {letter} is in the word!')
            print(self.word_guessed)
        else:
            self.num_lives = self.num_lives - 1
            print(f'Sorry, {letter} is not in the word.')
            print(f"**** You have {self.num_lives} lives left ****")
            if self.num_lives == 0:
                print(f"You ran out of lives. The word was * {self.word} *")
            else:
                self.give_hints()

    def give_hints(self):
        ## This function provides a hint letter if user picks wrong letter. However it should not be the last letter to be guessed
        missing_letters = [x for i, x in enumerate(self.word_guessed) if x == '_']
        if len(missing_letters) > 1:
            self.list_remaining_letters = [x for x in self.list_remaining_letters if x not in self.list_letters]
            random_index = randint(0, len(self.list_remaining_letters) - 1)
            help_char = self.list_remaining_letters[random_index]
            help_indexes = [pos for pos, char in enumerate(self.word) if char == help_char]
            help_replacements = [help_char] * len(help_indexes)
            for (index, replacement) in zip(help_indexes, help_replacements):
                self.word_guessed[index] = replacement
            self.list_letters.append(help_char.lower())
            print(f'letter {help_char} is a hint!')
            print(self.word_guessed)
    
    def play_game(self, word_list):
        ## Running the game until the user wins or loses
        while self.num_lives > 0:
            if '_' in self.word_guessed:
                self.ask_letter()
            else:
                print("Congratulations, you won!")
                break

def main():
    ## main function to define the world list and number of lives to start the game
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    game = Hangman(word_list, num_lives=5)
    game.play_game(word_list)

if __name__ == '__main__':
    main()