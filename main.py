import game, player
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
game.begin_game()
game.progress_game()