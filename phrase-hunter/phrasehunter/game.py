"""Used to pick a random phrase."""
import random
from phrase import Phrase


class Game:

    def __init__(self):
        """Instance starting values."""
        self.missed = 0
        self.phrases = [
        "blowing away",
        "in the wind",
        "the brown hat",
        "my English teacher",
        "hello world"]
        self.active_phrase = None
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
        """Returns a random phrase from self.phrases."""
        return random.choice(self.phrases)

    def welcome(self):
        """Display welcome message."""
        print("Welcome to the Phrase Hunters Game!")

    def get_guess(self):
        """Get guess from user and append it to self.guesses attribute."""
        while self.phrase_instance_one.check_complete() is not True and self.missed < 5:
            self.guess = input("Guess a letter: ")
            self.guess = self.guess.lower()
            try:
                int(self.guess)
                print("Please enter a letter, not a number!")
            except ValueError:
                try:
                    self.guess[1]
                    print("Please input only one letter!")
                except IndexError:
                    if self.phrase_instance_one.check_letter(self.guess) is False:
                        self.missed += 1
                        self.guesses.append(self.guess)
                        print(f"The phrase doesn't have that letter. You have {5 - self.missed} more misses before you lose!")
                    elif self.phrase_instance_one.check_letter(self.guess) is True and self.guess not in self.guesses:
                        print("You got one! Here is the updated phrase:")
                        self.guesses.append(self.guess)
                        self.phrase_instance_one.display(self.guess)
                    elif self.phrase_instance_one.check_letter(self.guess) is True and self.guess in self.guesses:
                        print("You already revealed that letter!")
        self.game_over()

    def game_over(self):
        """Display a friendly win or loss message and ask to play again or end game"""
        if self.phrase_instance_one.check_complete() is True:
            print("You did it! You won!")
            self.reset_or_quit()
        else:
            print("Sorry! You lost!")
            self.reset_or_quit()

    def reset_or_quit(self):
        """Reset or quit game"""
        self.answer = input("Enter Y to play again, or anything else to exit! ")
        self.answer = self.answer.upper()
        if self.answer == "Y":
            self.start()
        else:
            print("Thanks for playing!")
            exit()      


if __name__ == "__main__":
    game_one = Game()
    game_one.start()
