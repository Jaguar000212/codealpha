from time import sleep
import json


def ReadFile():
    with open("settings.json", "r") as f:
        return json.load(f)


def SaveFile(dictionary):
    with open("settings.json", "w") as f:
        json.dump(dictionary, f, indent=4)


class Settings:

    def __init__(self):
        settings = ReadFile()
        self.turns = settings["turns"]
        self.level = settings["level"]
        self.words = settings["words"]
        self.score = settings["score"]

    def change_turns(self):
        chances = None
        while not chances:
            try:
                chances = int(input("Enter the number of chances you want : "))
                if chances < 1:
                    chances = None
                    raise ValueError()
            except ValueError:
                print("Please enter a number greater than 0")
        settings = ReadFile()
        settings["turns"] = chances
        SaveFile(settings)
        self.turns = chances

    def change_level(self):
        print("Select the difficulty level")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        difficulty = None
        while not difficulty:
            try:
                difficulty = int(input("Select from 1/2/3 : "))
                if difficulty not in [1, 2, 3]:
                    difficulty = None
                    raise ValueError()
            except ValueError:
                pass

        settings = ReadFile()
        settings["level"] = difficulty
        SaveFile(settings)
        self.level = difficulty

    def add_word(self):
        new_word = input("Enter the word : ")
        settings = ReadFile()

        if len(new_word) < 2:
            print("Word should be of minimum 2 characters")
            sleep(1)
            return self.add_word()
        
        if new_word in settings["words"]["easy"] or new_word in settings["words"]["medium"] or new_word in settings["words"]["hard"]:
            print(f"{new_word} already exists in the dictionary")
            sleep(1)
            return self.add_word()
        
        if new_word.isalpha() is False:
            print("Word should contain only alphabets")
            sleep(1)
            return self.add_word()

        if len(new_word) in range(2, 4):
            settings["words"]["easy"].append(new_word.lower())
            print(f"{new_word} added to easy list")
        elif len(new_word) in range(5, 6):
            settings["words"]["medium"].append(new_word.lower())
            print(f"{new_word} added to medium list")
        else:
            settings["words"]["hard"].append(new_word.lower())
            print(f"{new_word} added to hard list")

        self.words = settings["words"]
        SaveFile(settings)

    def remove_word(self):
        word = input("Enter the word : ")
        settings = ReadFile()
        for key in settings["words"]:
            if word in settings["words"][key]:
                settings["words"][key].remove(word)
                print(f"{word} removed from {key} list")
                break
        else:
            print(f"{word} not found in any list")
        self.words = settings["words"]
        SaveFile(settings)
    
    def view_score(self):
        print(f"Win : {self.score['win']}")
        print(f"Lost : {self.score['lost']}")
        print(f"Total : {self.score['win'] + self.score['lost']}")
        input("Press Enter to continue")

    def set_score(self, state):
        settings = ReadFile()
        settings["score"][state] += 1
        self.score = settings["score"]
        SaveFile(settings)

    def reset_score(self):
        settings = ReadFile()
        settings["score"] = {"win": 0, "lost": 0}
        self.score = settings["score"]
        SaveFile(settings)
        print(f"Score reset!!")
