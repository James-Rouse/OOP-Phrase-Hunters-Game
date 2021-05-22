class Game:

    def __init__(self):
        self.missed = 0
        self.phrases = ['blowing away', 'in the wind', 'the brown hat', 'my English teacher', 'hello world']
        self.active_phrase = None
        self.guesses = []

    def start(self):
        d

    def get_random_phrase(self):
        d

    def welcome(self):
        print('Welcome to the Phrase Hunters Game!')

    def get_guess(self):
        while True:
            guess = input('Guess a letter: ')
            guess = guess.lower()
            try:
                int(guess)
                print('Please enter a letter, not a number!')
                continue
            except ValueError:
                try:
                    guess[1]
                    print('Please input only one letter!')
                    continue
                except IndexError:
                    self.guesses.append(guess)
                    break

    def game_over(self):
        d


game_one = Game()
game_one.welcome()
game_one.get_guess()
