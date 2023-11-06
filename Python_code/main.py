import json
import sys



class Game:
    
    def __init__(self):
        with open('Words.json') as f:
            self.data = json.load(f)
        pass
    
    def add_words(self, word):
        self.data.append(word)
        with open('Words.json', 'w') as f:
            json.dump(self.data, f)
            
    



if __name__ == "__main__":
    game = Game()
    #game.add_words("Задача")
    print(game.data)
