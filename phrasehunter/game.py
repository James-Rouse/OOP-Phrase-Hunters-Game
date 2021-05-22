import random
from phrasehunter.phrase import Phrase


class Game:
    """Operates most of the game mechanics."""

    def __init__(self):
        """Instance starting values."""
        self.phrases = [
        'blowing away',
        'in the wind',
        'the brown hat',
        'my English teacher',
        'the grocery store',
        'ran quickly',
        'has been raining',
        'on the boat',
        'above the stove',
        'around the corner',
        'hello world']
        self.active_phrase = None
        self.missed = 0
        self.guesses = []

    def start(self):
        """Initiate game loop."""
        self.missed = 0
        self.active_phrase = None
        self.guesses = []
        self.welcome()
        self.active_phrase = self.get_random_phrase().lower()
        self.phrase_instance_one = Phrase(self.active_phrase)
        self.phrase_instance_one.display("")
        self.get_guess()

    def get_random_phrase(self):
        """Return a random phrase from self.phrases."""
        return random.choice(self.phrases)

    def welcome(self):
        """Display welcome message."""
        print("\nWelcome to the Phrase Hunters Game!\n")

    def get_guess(self):
        """Get guess from user and append it to self.guesses attribute."""
        while self.phrase_instance_one.check_complete() is not True and self.missed < 5:
            self.guess = input("\nGuess a letter: ")
            self.guess = self.guess.lower()
            try:
                int(self.guess)
                print("\nPlease enter a letter, not a number!")
            except ValueError:
                try:
                    self.guess[1]
                    print("\nPlease input only one letter!")
                except IndexError:
                    if self.phrase_instance_one.check_letter(self.guess) is False:
                        self.missed += 1
                        self.guesses.append(self.guess)
                        print(f"\nThe phrase doesn't have that letter. You have {5 - self.missed} more misses before you lose!")
                    elif self.phrase_instance_one.check_letter(self.guess) is True and self.guess not in self.guesses:
                        print("\nYou got one! Here is the updated phrase:\n")
                        self.guesses.append(self.guess)
                        self.phrase_instance_one.display(self.guess)
                    elif self.phrase_instance_one.check_letter(self.guess) is True and self.guess in self.guesses:
                        print("\nYou already revealed that letter!")
        self.game_over()

    def game_over(self):
        """Display a friendly win or loss message and ask to play again or end game."""
        if self.phrase_instance_one.check_complete() is True:
            print("\nYou did it! You won!")
            self.reset_or_quit()
        else:
            print("\nSorry! You lost!")
            self.reset_or_quit()

    def reset_or_quit(self):
        """Reset or quit game."""
        self.answer = input("\nEnter Y to play again, or anything else to exit! ")
        self.answer = self.answer.upper()
        if self.answer == "Y":
            self.start()
        else:
            print("\nThanks for playing!\n")
            exit()
