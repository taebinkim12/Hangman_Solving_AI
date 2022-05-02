class Player:

    def __init__(self, answer_len):
        self.words = open("./words_alpha.txt", "r").readlines()

        self.have_guessed = [False for i in range(26)]
        self.alphabets_count = {}
        self.dict_hidden_ans = {}
        self.answer_len = answer_len

        self.words = [word for word in self.words if len(word) == self.answer_len + 1]

    def initialize_alhabet_count(self):
        for i in range(26):
            char = chr(ord('A') + i).upper()
            self.alphabets_count[char] = 0

    def print_view(self):
        
        for i in range(26):
            print(chr(i+ord('a')).upper(), end=":")
            if (self.have_guessed[i] is False):
                print("     ", end = "")
            else:
                print("  X  ", end = "")
            if (i % 5) == 4:
                print("")
        print("")

    def user_guess(self):
        comd = input("Type your command\n").lower()

        while (True):
            if not self.validate_command(comd):
                print("INVALID COMMAND")
            elif comd == "status":
                return "STATUS"
            elif comd == "view":
                return "VIEW"
            elif comd == "help":
                return "HELP"    
            elif comd.__contains__("guess"):
                if not self.validate_guess(comd):
                    print("INVALID GUESS")
                else:
                    break

            comd = input("Type your command\n").lower()
        
        user_guess = comd.split()[1].upper()
        print(f"You have guessed {user_guess}")
        return user_guess

    def validate_guess(self, comd):
        guess = comd.split()
        if len(guess) != 2:
            return False
        elif len(guess[1]) != 1:
            return False
        elif not guess[1].isalpha():
            return False
        
        guess = guess[1]

        if self.have_guessed[ord(guess)-ord('a')] is False:
            self.have_guessed[ord(guess)-ord('a')] = True
        else:
            return False

        return True

    def validate_command(self, comd):
        if comd.__contains__("guess") or comd == "status" or comd == "view" or comd == "help":
            return True

        return False

    def recommendation(self, hidden_answer):
        self.initialize_alhabet_count()
        # self.words = open("./words_alpha.txt", "r").readlines()

        if not self.check_all_vowel_guessed():
            print("Try to guess one of the Vowels first!")
            self.print_view()
            return

        # NEED TO UPDATE THE 'words' LIST with length
        #self.words = [word for word in self.words if len(word) == self.answer_len + 1]

        # Have this function take one more param, "hidden answer"
            # gotta decide type - string or list?
            # anyway, get that and update words again based on that information
        self.update_words(self.answer_len, hidden_answer)

        # counting occurrence of each letter
        for word in self.words:
            word = word.rstrip("\n").upper()
            for i in range(self.answer_len):
                self.alphabets_count[word[i].upper()] += 1
        most_frequent = max(self.alphabets_count, key=self.alphabets_count.get)

        # prints our occurrence nicely
        for key,value in self.alphabets_count.items():
            if (self.have_guessed[ord(key) - ord('A')]) or value == 0:
                continue
            print(key, ' : ', value)

        print(self.words)
        print(len(self.words))


    def check_all_vowel_guessed(self):
        char_a = ord('a')
        a = ord('a') - char_a
        e = ord('e') - char_a
        i = ord('i') - char_a
        o = ord('o') - char_a
        u = ord('u') - char_a

        if (self.have_guessed[a] and self.have_guessed[e] and self.have_guessed[i] and self.have_guessed[o] and self.have_guessed[u]):
            return True

        return False

    def update_words(self, answer_len, hidden_answer):
        for i in range(len(hidden_answer)):
            self.dict_hidden_ans[i] = hidden_answer[i]
        
        new_words = list()

        for word in self.words:
            # compare word and dict_hidden_ans
            valid = True
            for i in range(answer_len):
                if self.dict_hidden_ans[i] != "-":
                    if self.dict_hidden_ans[i] != word[i].upper():
                        valid = False
                        break

            if valid:
                new_words.append(word)

        self.words = new_words
        
    def remove_inct_guess(self, guess):
        new_words = list()
        guess = guess.lower()
        for word in self.words:
            if not word.__contains__(guess):
                new_words.append(word)
        self.words = new_words