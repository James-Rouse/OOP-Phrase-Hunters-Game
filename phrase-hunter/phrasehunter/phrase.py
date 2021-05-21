"""Used to pick a random phrase."""
import random


class Phrase:
    """Deals with phrase manipulation for the game."""

    def random_phrase():
        """Choose a random phrase."""
        phrases = [
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
        return random.choice(phrases)

    def __init__(self, chosen_phrase):
        """Recieve phrase for use in game."""
        self.phrase = chosen_phrase.lower()

    def display(self, guessed_letter):
        """Print the phrase to console with only guessed letters visibile."""
        hidden_phrase = self.phrase
        for letter in self.phrase:
            if letter != ' ':
                if letter != guessed_letter:
                    hidden_phrase = hidden_phrase.replace(letter, '_')
        return hidden_phrase

    def check_letter(self, guessed_letter):
        """Check to see if the letter selected by the user matches a letter in the phrase."""
        return guessed_letter in self.phrase

    def check_complete(self, hidden_phrase):
        """Check to see if the whole phrase has been guessed."""
        return hidden_phrase == self.phrase


guessed_letter = 'o'
chosen_phrase = Phrase.random_phrase()
phrase_one = Phrase('hello world')
hidden_phrase = phrase_one.display(guessed_letter)

print(phrase_one.display(guessed_letter))
print(phrase_one.check_letter(guessed_letter))
print(phrase_one.check_complete(hidden_phrase))
