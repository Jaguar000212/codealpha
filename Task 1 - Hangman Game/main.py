from settings import Settings
from random import choice
from art import tprint
from time import sleep
from os import system, name

def clear():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class HangMan:
    def __init__(self):
        clear()
        self.settings = Settings()
        self.words_easy = self.settings.words["easy"]
        self.words_medium = self.settings.words["medium"]
        self.words_hard = self.settings.words["hard"]
        self.start()

    def start(self):
        tprint("Welcome to Hangman Game")
        condition = None
        while not condition:
            try:
                condition = int(
                    input(
                        "1. Play\n2. Settings\n3. Exit\nSelect an Option (1/2/3) : "
                    )
                )
                if condition not in [1, 2, 3]:
                    condition = None
                    raise ValueError
            except ValueError:
                print("Please select from (1/2/3) only")
        if condition == 1:
            clear()
            self.play()
        elif condition == 2:
            clear()
            self.edit_settings()
        else:
            print("Thank you for playing Hangman Game")
            sleep(1)
            exit()

    def edit_settings(self):
        print("------- Settings -------")
        print(f"1. Number of Chances: {self.settings.turns}")
        print(f"2. Difficulty Level: {self.settings.level}")
        print("3. Add a Word to Dictionary")
        print("4. Remove a Word to Dictionary")
        print("5. View Score")
        print("6. Reset Score")
        print("7. Back to Main Menu")

        settings_option = None
        while not settings_option:
            try:
                settings_option = int(input("Select an Option (1/2/3/4/5/6/7) : "))
                if settings_option not in [1, 2, 3, 4, 5, 6, 7]:
                    settings_option = None
                    raise ValueError
            except ValueError:
                print("Enter from 1,2,3,4,5,6,7 only")
        clear()
        if settings_option == 1:
            self.settings.change_turns()
        elif settings_option == 2:
            self.settings.change_level()
        elif settings_option == 3:
            self.settings.add_word()
        elif settings_option == 4:
            self.settings.remove_word()
        elif settings_option == 5:
            self.settings.view_score()
        elif settings_option == 6:
            self.settings.reset_score()
        elif settings_option == 7:
            return self.start()
        sleep(1)
        clear()
        self.edit_settings()

    def play(self):

        if self.settings.level == 1:
            word = choice(self.words_easy)
        elif self.settings.level == 2:
            word = choice(self.words_medium)
        elif self.settings.level == 3:
            word = choice(self.words_hard)

        characters = []
        temp = word
        turns = self.settings.turns
        while True:
            for i in word:
                characters.append("_")

            while turns > 0:
                if "_" in characters:
                    print("".join(characters))
                    letter = input("Guess a letter : ")

                    if len(letter) == 1:
                        if letter in word:
                            characters[word.index(letter)] = letter
                            word = word.replace(letter, "_", 1)
                            print("Correct!")

                        else:
                            turns -= 1
                            print("Turns left : " + str(turns))
                    else:
                        print("Enter only one alphabet")
                else:
                    print(
                        f"\nCongratulations! You won...\nThe correct answer is {''.join(characters)}"
                    )
                    self.settings.set_score("win")
                    break

            if "_" in characters:
                print("".join(characters))
                print(f"Sorry! You lost...\nThe correct answer is {temp}")
                self.settings.set_score("lost")
            replay = input("\nPress any key to play again or (f) to go to Main Menu : ")
            if replay.lower() == "f":
                self.start()
            else:
                self.play()

HangMan()