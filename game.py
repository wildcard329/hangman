from words import words
from stages import stages
import random

class Game:
    def __init__(self):
        self.word = random.choice(words)
        self.counter = 0
        self.playing = False
        self.right = set()
        self.wrong = set()

    def clear_game(self):
        self.word = random.choice(words)
        self.counter = 0
        self.playing = False
        self.right = set()
        self.wrong = set()

    def compare_player_progress(self, word):
        if word == self.word:
            print("You win!!!")
            self.clear_game()
            self.prompt_player()
            self.print_board()

    def display_word(self):
        string = ''
        for letter in list(self.word):
            if letter != ' ' and letter not in self.right:
                string += '-'
            else:
                string += letter
                self.compare_player_progress(string)
        print(string)

    def display_stage(self):
        print(stages[self.counter])

    def print_stage(self):
        if len(stages) == self.counter:
            self.playing = False
            print('Oh no, you lose!')
            self.clear_game()
            self.prompt_player()
            self.print_board()
        else:
            self.display_stage()

    def prompt_player(self):
        play = input('Play hangman? ')
        if play == 'y'.lower() or 'yes'.lower():
            self.playing = True

    def check_guess(self, guess, word):
        if guess in word:
            self.right.add(guess)
        else:
            self.wrong.add(guess)
            self.counter += 1
        incorrect = 'incorrect: '
        for letter in self.wrong:
            incorrect += letter + ', '
        incorrect += '\b\b'
        print(incorrect)

    def print_board(self):
        self.print_stage()
        self.display_word()

    def round(self):
        self.prompt_player()
        while self.playing == True:
            word = list(self.word)
            self.print_board()
            guess = input('Guess a letter ')
            if guess in self.right or guess in self.wrong:
                print(f"${guess} has already been guessed.")
            elif guess == '':
                print('Invalid guess')
            else:
                self.check_guess(guess, word)

g = Game()
g.round()
