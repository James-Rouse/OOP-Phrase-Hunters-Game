class Phrase:
    """Deals with phrase checking and manipulation for the game."""

    def __init__(self, chosen_phrase):
        """Recieve phrase for use in game."""
        self.phrase = chosen_phrase.lower()
        self.guesses = []

    def display(self, guessed_letter, output_string):
        """Print the phrase to console with only guessed letters visibile."""
        self.hidden_phrase = self.phrase
        for letter in self.phrase:
            if letter != " " and letter != guessed_letter and letter not in self.guesses:
                self.hidden_phrase = self.hidden_phrase.replace(letter, "_")
                self.guesses.append(guessed_letter)
        if output_string != "":
            print(f"\n{output_string}\n")
        print(self.hidden_phrase)

    def check_letter(self, guessed_letter):
        """Check to see if the letter selected by the user matches a letter in the phrase."""
        return guessed_letter in self.phrase

    def check_complete(self):
        """Check to see if the whole phrase has been guessed."""
        return self.hidden_phrase == self.phrase
