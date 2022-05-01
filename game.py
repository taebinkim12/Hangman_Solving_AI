import random
import player


MAX_INCT_GUESS = 7
answer, hidden_answer = "", ""
answer_len = 0
num_inct_guess = 6
num_crct_guess = 0

# region Major_Features
def begin_game():
    global answer, num_inct_guess, answer_len, hidden_answer
    answer = get_word()
    answer = answer.upper()
    answer_len = len(answer)
    hidden_answer = "-" * answer_len
    num_inct_guess = 0

def progress_game():

    print_answer_len()
    
    while (num_inct_guess < MAX_INCT_GUESS and num_crct_guess < len(answer)):
        print_hidden()
        guess = player.user_guess()
        if guess == "STATUS":
            print_hangman()
            # guess = player.user_guess()
        elif guess == "HELP":
            player.recommendation(answer_len, hidden_answer)
            # guess = player.user_guess()
        elif guess == "VIEW":
            player.print_view()
            # guess = player.user_guess()
        elif answer.__contains__(guess):
            print("CORRECT GUESS")
            reveal_hidden_with_guess(guess)
            add_num_crct_guess(hidden_answer)
        else:
            print("INCORRECT GUESS")
            add_num_inct_guess()
            print_hangman()

    success = num_crct_guess >= answer_len
    if not success:
        print("SUCKER")
    else:
        print("CONGRATULATION")
        
    print(f"Answer was {answer}")

def get_word():
    dictionary = open("./words_alpha.txt", "r")
    words = dictionary.readlines()
    words_count = len(words)

    return words[random.randint(0, words_count - 1)].rstrip("\n")

# endregion

# region Helpers
def print_hangman():
    print("")
    if num_inct_guess == 0:
        for i in range(4):
            print("")
    elif num_inct_guess == 1:
        print("  O  ")
        print("     ")
        print("     ")
        print("     ")
    elif num_inct_guess == 2:
        print("  O  ")
        print("  |  ")
        print("     ")
        print("     ")
    elif num_inct_guess == 3:
        print("  O  ")
        print(" /|  ")
        print("     ")
        print("     ")
    elif num_inct_guess == 4:
        print("  O  ")
        print(" /|\\")
        print("     ")
        print("     ")
    elif num_inct_guess == 5:
        print("  O  ")
        print(" /|\\")
        print("  |  ")
        print("     ")
    elif num_inct_guess == 6:
        print("  O  ")
        print(" /|\\")
        print("  |  ")
        print(" /   ")
    elif num_inct_guess == 7:
        print("  O  ")
        print(" /|\\")
        print("  |  ")
        print(" / \\")

def get_num_inct_guess():
    return num_inct_guess

def get_answer_length():
    return answer_len

def add_num_inct_guess():
    global num_inct_guess 
    num_inct_guess += 1

def add_num_crct_guess(hidden_answer):
    global num_crct_guess, answer_len
    hidden = hidden_answer.count("-")
    num_crct_guess = answer_len - hidden

def checking_guess(guess):
    if answer.__contains__(guess):
        return True
    else:
        return False

def print_hidden():
    print(f"Word is : {hidden_answer}")
   
def reveal_hidden_with_guess(guess):
    global hidden_answer
    for i in range(answer_len):
        if answer[i] == guess:
            hidden_answer = hidden_answer[:i] + guess + hidden_answer[i+1:]

def print_answer_len():
    print(f"Word is {answer_len} letters long")

# endregion
