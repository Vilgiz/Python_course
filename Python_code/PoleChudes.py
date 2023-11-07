import random
import json

class PoleChudes:
    
    def __init__(self):
        self.guessed_word = None
        self.guessed_letters = []
        with open('Words.json') as f:
            self.words = json.load(f)

    def start_game(self):
        self.guessed_word = random.choice(self.words)
        self.guessed_letters = ['_'] * len(self.guessed_word)
        
    def add_word(self, word):
        self.words.append(word)
        with open('Words.json', 'w') as f:
            json.dump(self.words, f)

    def guess_letter(self, letter):
        if letter in self.guessed_word:
            for i in range(len(self.guessed_word)):
                if self.guessed_word[i] == letter:
                    self.guessed_letters[i] = letter
        else:
            print("Буква не найдена в загаданном слове!")

    def is_word_guessed(self):
        return '_' not in self.guessed_letters

    def display_word(self):
        print(' '.join(self.guessed_letters))


if __name__ == "__main__":
    
    game = PoleChudes()
    #game.add_word("данные")
    game.start_game()

    while not game.is_word_guessed():
        game.display_word()
        letter = input("Введите букву: ")
        game.guess_letter(letter)

    print("Поздравляем! Вы угадали слово:", game.guessed_word)