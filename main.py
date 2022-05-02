from game import Game
def cleanup_words():
    a_file = open("words_alpha.txt", "r")
    lines = a_file.readlines()
    a_file.close()

    new_file = open("words_alpha.txt", "w")
    for line in lines:
        if len(line) != 2:
            new_file.write(line)

    new_file.close()
        
cleanup_words()

count_success = 0
count_fail = 0
for i in range(100):
    g = Game()
    if g.progress_game() == True:
        count_success += 1
    else:
        count_fail += 1

print("\nAfter 100 trials, here is the result")
print(f"{count_success} times succeeded to guess")
print(f"{count_fail} times failed to guess\n")