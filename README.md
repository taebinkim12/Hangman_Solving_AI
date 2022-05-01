# Hangman Solving Helper

This program is a ***Hangman*** game with features helping for user to make next guess.

Here are instructions on how to run this program and play a game of Hangman!
___
## Quick Heads-up with the rule
- User gets **7 trials** to guess the correct word
- Guessing a previously-tried letter will NOT count as a trial
___
## To Start the Game


**First**, to start the program, navigate to folder containing files

**Second**, execute following command to start the program
```
$ python3 main.py
```
___
## To Play the Game
Player has 4 commands to choose
### Guessing a letter
Type following command to guess
```
$ guess {letter_to_guess}
```
For example, to guess letter 'Z'
```
$ guess Z
```
** The letter is **NOT** sensitive to upper/lower case. Hence, proceed with the way you prefer
___
### Check your Hangman
To check how close you are to complete hangman (how many wrong guesses that you have made), please type following command
```
$ status
```
___
### Check your Guesses So Far
To see what letters you have guessed so far, type following comand
```
$ view
```
The terminal will show 'X' beside the letter that you have gueesed already
___
### Need Some Help?
**YES!** I got you! Type following command to see the occurrences of each letter that you have not guessed yet among the words that have potential to be correct answer
```
$ help
```
___
### Thank you very much!