class Phrase:
    """Deals with phrase manipulation for the game."""

    def __init__(self, chosen_phrase):
        """Recieve phrase for use in game."""
        self.phrase = chosen_phrase.lower()

    def display(self, guessed_letter):
        """Print the phrase to console with only guessed letters visibile."""
        self.hidden_phrase = self.phrase
        for letter in self.phrase:
            if letter != " ":
                if letter != guessed_letter:
                    self.hidden_phrase = self.hidden_phrase.replace(letter, "_")
        print(self.hidden_phrase)

    def check_letter(self, guessed_letter):
        """Check to see if the letter selected by the user matches a letter in the phrase."""
        return guessed_letter in self.phrase

    def check_complete(self):
        """Check to see if the whole phrase has been guessed."""
        return self.hidden_phrase == self.phrase


if __name__ == "__main__":
    phrase_one = Phrase('bruh')
    phrase_one.check_letter('d')