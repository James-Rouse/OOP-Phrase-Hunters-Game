import random
from phrasehunter.phrase import Phrase


class Game:
    """Operates most of the game mechanics."""

    def __init__(self):
        """Instance starting values."""
        self.phrases = [
            Phrase("blowing away"),
            Phrase("in the wind"),
            Phrase("the brown hat"),
            Phrase("my English teacher"),
            Phrase("the grocery store"),
            Phrase("ran quickly"),
            Phrase("has been raining"),
            Phrase("on the boat"),
            Phrase("above the stove"),
            Phrase("around the corner"),
            Phrase("hello world")]
        self.active_phrase = None
        self.missed = 0
        self.guesses = []
        self.used_phrases = []

    def start(self):
        """Initiate game loop."""
        self.missed = 0
        self.active_phrase = None
        self.guesses = []
        self.welcome()
        self.active_phrase = self.get_random_phrase()
        self.active_phrase.guesses = []
        self.active_phrase.display("")
        self.get_guess()

    def get_random_phrase(self):
        """Return an unused random phrase from self.phrases. When all are used, the used list resets."""
        self.random_choice = random.choice(self.phrases)
        if len(self.used_phrases) == 11:
            self.used_phrases = []
        while self.phrases.index(self.random_choice) in self.used_phrases:
            self.random_choice = random.choice(self.phrases)
        self.phrase_index = self.phrases.index(self.random_choice)
        self.used_phrases.append(self.phrase_index)
        return self.random_choice

    def welcome(self):
        """Display welcome message."""
        print("\nWelcome to the Phrase Hunters Game!\n")

    def get_guess(self):
        """Get guess from user and append it to self.guesses attribute."""
        while self.active_phrase.check_complete() is not True and self.missed < 5:
            self.guess = input("\nGuess a letter: ")
            self.guess = self.guess
            try:
                int(self.guess)
                print("\nPlease enter a letter, not a number!")
            except ValueError:
                try:
                    self.guess[1]
                    print("\nPlease input only one letter!")
                except IndexError:
                    self.a_though_z = "abcdefghijklmnopqrstuvwxyz"
                    if self.guess == "":
                        print("\nYou didn't enter anything!")
                    elif self.guess not in self.a_though_z:
                        print("\nPlease only enter a letter within a-z!")
                    elif self.active_phrase.check_letter(self.guess) is False:
                        self.missed += 1
                        self.guesses.append(self.guess)
                        print(f"\nThe phrase doesn't have that letter. You have {5 - self.missed} more misses before you lose!")
                    elif self.active_phrase.check_letter(self.guess) is True and self.guess not in self.guesses:
                        print("\nYou got one! Here is the updated phrase:\n")
                        self.guesses.append(self.guess)
                        self.active_phrase.display(self.guess)
                    elif self.active_phrase.check_letter(self.guess) is True and self.guess in self.guesses:
                        print("\nYou already revealed that letter!")
        self.game_over()

    def game_over(self):
        """Display a friendly win or loss message and ask to play again or end game."""
        if self.active_phrase.check_complete() is True:
            print("\nYou did it! You won!")
            self.reset_or_quit()
        else:
            print("\nSorry! You lost!")
            self.reset_or_quit()

    def reset_or_quit(self):
        """Reset or quit game."""
        while True:
            self.answer = input("\nWould you like to play again? Y/N? ")
            self.answer = self.answer.upper()
            if self.answer == "Y":
                self.start()
                break
            elif self.answer == "N":
                print("\nThanks for playing!\n")
                exit()
            else:
                print("\nPlease enter only Y or N!")
                continue
