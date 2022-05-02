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

    def user_guess(self, hidden_answer):
        my_guess = ''
        my_guess = self.recommendation(hidden_answer)
        self.validate_guess(my_guess)
        print(f"I have guessed {my_guess}")
        return my_guess

    def validate_guess(self, guess):
        guess = guess.lower()
        if self.have_guessed[ord(guess)-ord('a')] is False:
            self.have_guessed[ord(guess)-ord('a')] = True

    def recommendation(self, hidden_answer):
        self.initialize_alhabet_count()
        vowels = ('a', 'e', 'i', 'o', 'u')

        for vowel in vowels:
            if self.have_guessed[ord(vowel) - ord('a')] is False:
                return vowel.upper()
        
        self.update_words(hidden_answer)

        for word in self.words:
            word = word.rstrip("\n").upper()
            for i in range(self.answer_len):
                self.alphabets_count[word[i].upper()] += 1
        
        key_of_max_value = 'z'
        max_value = 0
        for key,value in self.alphabets_count.items():
            if (self.have_guessed[ord(key) - ord('A')]) or value == 0:
                continue
            else:
                if (value >= max_value):
                    key_of_max_value = key

        return key_of_max_value.upper()

    def update_words(self, hidden_answer):
        for i in range(len(hidden_answer)):
            self.dict_hidden_ans[i] = hidden_answer[i]
        
        new_words = list()

        for word in self.words:
            # compare word and dict_hidden_ans
            valid = True
            for i in range(self.answer_len):
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