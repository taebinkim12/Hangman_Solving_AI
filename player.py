words = list()
have_guessed = [False for i in range(26)]
# vowels_guessed = False
alphabets_count = {}
dict_hidden_ans = {}

def initialize_alhabet_count():
    global alphabets_count
    for i in range(26):
        char = chr(ord('A') + i).upper()
        alphabets_count[char] = 0

def print_view():
    for i in range(26):
        print(chr(i+ord('a')).upper(), end=":")
        if (have_guessed[i] is False):
            print("     ", end = "")
        else:
            print("  X  ", end = "")
        if (i % 5) == 4:
            print("")
    print("")

def user_guess():
    comd = input("Type your command\n").lower()

    while (True):
        if not validate_command(comd):
            print("INVALID COMMAND")
        elif comd == "status":
            return "STATUS"
        elif comd == "view":
            return "VIEW"
        elif comd == "help":
            return "HELP"    
        elif comd.__contains__("guess"):
            if not validate_guess(comd):
                print("INVALID GUESS")
            else:
                break

        comd = input("Type your command\n").lower()
    
    user_guess = comd.split()[1].upper()
    print(f"You have guessed {user_guess}")
    return user_guess

def validate_guess(comd):
    guess = comd.split()
    if len(guess) != 2:
        return False
    elif len(guess[1]) != 1:
        return False
    elif not guess[1].isalpha():
        return False
    
    guess = guess[1]

    if have_guessed[ord(guess)-ord('a')] is False:
        have_guessed[ord(guess)-ord('a')] = True
    else:
        return False

    return True

def validate_command(comd):
    if comd.__contains__("guess") or comd == "status" or comd == "view" or comd == "help":
        return True

    return False

def recommendation(answer_len, hidden_answer):
    global words
    initialize_alhabet_count()
    words = open("./words_alpha.txt", "r").readlines()

    if not check_all_vowel_guessed():
        print("Try to guess one of the Vowels first!")
        print_view()
        return

    # NEED TO UPDATE THE 'words' LIST with length
    words = [word for word in words if len(word) == answer_len + 1]

    # Have this function take one more param, "hidden answer"
        # gotta decide type - string or list?
        # anyway, get that and update words again based on that information
    update_words(answer_len, hidden_answer)

    # counting occurrence of each letter
    for word in words:
        word = word.rstrip("\n").upper()
        for i in range(answer_len):
            alphabets_count[word[i].upper()] += 1
    most_frequent = max(alphabets_count, key=alphabets_count.get)

    # prints our occurrence nicely
    for key,value in alphabets_count.items():
        if (have_guessed[ord(key) - ord('A')]) or value == 0:
            continue
        print(key, ' : ', value)

def check_all_vowel_guessed():
    char_a = ord('a')
    a = ord('a') - char_a
    e = ord('e') - char_a
    i = ord('i') - char_a
    o = ord('o') - char_a
    u = ord('u') - char_a

    if (have_guessed[a] and have_guessed[e] and have_guessed[i] and have_guessed[o] and have_guessed[u]):
        return True

    return False

def update_words(answer_len, hidden_answer):
    global words, dict_hidden_ans
    for i in range(len(hidden_answer)):
        dict_hidden_ans[i] = hidden_answer[i]
    
    new_words = list()

    for word in words:
        # compare word and dict_hidden_ans
        valid = True
        for i in range(answer_len):
            if dict_hidden_ans[i] != "-":
                if dict_hidden_ans[i] != word[i].upper():
                    valid = False
                    break

        if valid:
            new_words.append(word)

    words = new_words
    