import random
from player import Player

class Game:
    # region Major_Features
    def __init__(self):
        self.MAX_INCT_GUESS = 7
        self.answer = get_word().upper()
        self.answer_len = len(self.answer)
        self.hidden_answer = "-" * self.answer_len
        self.num_inct_guess = 0
        self.num_crct_guess = 0
        self.p = Player(self.answer_len)

        self.guessed = False

    def progress_game(self):
        self.print_answer_len()
        
        while (self.num_inct_guess < self.MAX_INCT_GUESS and self.num_crct_guess < len(self.answer)):
            self.print_hidden()
            guess = self.p.user_guess(self.hidden_answer)

            if self.answer.__contains__(guess):
                print("CORRECT GUESS")
                self.reveal_hidden_with_guess(guess)
                self.add_num_crct_guess()
            else:
                print("INCORRECT GUESS")
                self.add_num_inct_guess()
                self.print_hangman()
                self.p.remove_inct_guess(guess)

        success = self.num_crct_guess >= self.answer_len
        if not success:
            print("FAILED")
            self.guessed = False
        else:
            print("CONGRATULATION")
            self.guessed = True
            
        print(f"Answer was {self.answer}")

        return self.guessed

    # endregion

    # region Helpers
    def print_hangman(self):
        print("")
        if self.num_inct_guess == 0:
            for i in range(4):
                print("")
        elif self.num_inct_guess == 1:
            print("  O  ")
            print("     ")
            print("     ")
            print("     ")
        elif self.num_inct_guess == 2:
            print("  O  ")
            print("  |  ")
            print("     ")
            print("     ")
        elif self.num_inct_guess == 3:
            print("  O  ")
            print(" /|  ")
            print("     ")
            print("     ")
        elif self.num_inct_guess == 4:
            print("  O  ")
            print(" /|\\")
            print("     ")
            print("     ")
        elif self.num_inct_guess == 5:
            print("  O  ")
            print(" /|\\")
            print("  |  ")
            print("     ")
        elif self.num_inct_guess == 6:
            print("  O  ")
            print(" /|\\")
            print("  |  ")
            print(" /   ")
        elif self.num_inct_guess == 7:
            print("  O  ")
            print(" /|\\")
            print("  |  ")
            print(" / \\")

    def get_num_inct_guess(self):
        return self.num_inct_guess

    def get_answer_length(self):
        return self.answer_len

    def add_num_inct_guess(self):
        self.num_inct_guess += 1

    def add_num_crct_guess(self):
        hidden = self.hidden_answer.count("-")
        self.num_crct_guess = self.answer_len - hidden

    def checking_guess(self,guess):
        if self.answer.__contains__(guess):
            return True
        else:
            return False

    def print_hidden(self):
        print(f"Word is : {self.hidden_answer}")
    
    def reveal_hidden_with_guess(self, guess):
        for i in range(self.answer_len):
            if self.answer[i] == guess:
                self.hidden_answer = self.hidden_answer[:i] + guess + self.hidden_answer[i+1:]

    def print_answer_len(self):
        print(f"Word is {self.answer_len} letters long")

    # endregion



def get_word():
    dictionary = open("./words_alpha.txt", "r")
    words = dictionary.readlines()
    words_count = len(words)

    return words[random.randint(0, words_count - 1)].rstrip("\n")