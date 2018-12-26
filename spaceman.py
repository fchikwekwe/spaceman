# To do:
# work out exceptions
# give user option to restart game
#

from os import system, name
from termcolor import colored
import random

print(colored("***Let's play a game of Spaceman!***", "magenta", attrs=["bold"]) + colored("\nI have a secret word and you guess the letters it contains!", "cyan") + colored("\nIf you guess all the letters, then you win!", "yellow") + colored("\nBut if you guess seven wrong letters then you lose!", "red", attrs=["bold"]))

guessed_letters = []

# hide secret_word by replacing length of string with dashes
def mask_word(list_to_mask):
    masked_word = list("-" * len(list_to_mask))
    return masked_word

def user_input(masked_list, remaining_lives):
    print("Here is the secret word: ", masked_list)
    print("And here are your remaining lives: ", remaining_lives)
    # prompt player to guess word
    guessing = True
    while guessing:
        try:
            letter_guess = input(colored("Please guess a letter: ", "green", attrs=["bold"]))
            if letter_guess in guessed_letters:
                print(colored("Please pick a letter you have not already guessed. ", "cyan"))
            elif letter_guess.isalpha() != True:
                print(colored("Please make sure your selection is  a letter. ", "magenta"))
            elif len(letter_guess) != 1:
                print(colored("Please pick a single letter to guess. ", "yellow", attrs=["bold"]))
            else:
                guessed_letters.append(letter_guess)
                guessing = False
                pass
        except EOFError:
            print(colored("Please guess a letter first. ", "yellow", attrs=["bold"]))
    return letter_guess

def start_game():
    # import a list of words
    words = open("words.txt", "r")
    secret_select = words.read().split(" ")
    secret_word = random.choice(secret_select)

    secret_list = list(secret_word)
    masked_list = mask_word(secret_list)
    remaining_lives = ["<3", "<3", "<3", "<3", "<3", "<3", "<3"]

    # if player has guessed seven times, loss condition
    # if player has revealed all letters in secret word, win conditions
    guessed_seven = False
    guessed_word = False
    while guessed_seven == False and guessed_word == False:
        letter_guess = user_input(masked_list, remaining_lives)
        result = check_if_guess_is_correct(letter_guess, secret_list, masked_list)

        # if guess is incorrect, then take a life out of remaining_lives
        if result is None:
            remaining_lives.pop(0)
        else:
            pass

        if remaining_lives == []:
            guessed_seven = True
        else:
            pass

        if masked_list == secret_list:
            guessed_word = True
        else:
            pass

    #check if the game is a win or loss
    if guessed_seven == True:
        guessed_letters.clear()
        print("Sorry! You lose! The secret word was \"{}\".".format(secret_word))
    elif guessed_word == True:
        guessed_letters.clear()
        print(masked_list)
        print("Congratulations! You win!")

    play_again()

def check_if_guess_is_correct(guessed_letter, secret_list, masked_list):
    # if the guess is correct
    did_replace_letter = False
    for (i, letter) in enumerate(secret_list):
        # check if guessed_letter is equal to letter
        if guessed_letter == letter:
            # replace the element in the masked_list at the i'th index with the guessed_letter
            masked_list[i] = guessed_letter
            did_replace_letter = True
        else:
            pass
    if did_replace_letter == True:
        return masked_list
    else:
        return None

def clear():
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')

def play_again():
    play_or_not = True
    while play_or_not:
        try:
            play_quit = input("Enter 'P' to play again or 'Q' to quit the game. ")
            if play_quit.lower() == "p":
                clear()
                print(colored("***Let's play a game of Spaceman!***", "magenta", attrs=["bold"]) + colored("\nI have a secret word and you guess the letters it contains!", "cyan") + colored("\nIf you guess all the letters, then you win!", "yellow") + colored("\nBut if you guess seven wrong letters then you lose!", "red", attrs=["bold"]))
                start_game()
                play_or_not = False
            elif play_quit.lower() == "q":
                print("Thanks for playing! Goodbye!")
                play_or_not = False
            else:
                print("Please make a selection. ")
        except EOFError:
            print("Please make a selection. ")

start_game()

def test():
    print(mask_word(["t", "e", "s", "t"]))

# test()
