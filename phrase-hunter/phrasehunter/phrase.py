# Create your Phrase class logic here.
class Phrase:

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

    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self):
        hidden_phrase = self.phrase
        for letter in self.phrase:
            if letter != ' ':
                hidden_phrase = hidden_phrase.replace(letter, '_')
        print(hidden_phrase)


#    def check_letter():

#    def check_complete():


phrase_instance_1 = Phrase('hello world')

guessed_letter = 'o'

phrase_instance_1.display()