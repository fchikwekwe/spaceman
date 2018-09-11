from termcolor import colored
import random

print(colored("***Let's play a game of Spaceman!***", "magenta", attrs=["bold"]) + colored("\nI have a secret word and you guess the letters it contains!", "cyan") + colored("\nIf you guess all the letters, then you win!", "yellow") + colored("\nBut if you guess seven wrong letters then you lose!", "red", attrs=["bold"]))
# hide secret_word by replacing length of string with dashes
def mask_word(list_to_mask):
    masked_word = list("-" * len(list_to_mask))
    return masked_word

def user_input(masked_list, remaining_lives):
    # prompt player to guess word
    print("Here is the secret word: ", masked_list)
    print("And here are your remaining lives: ", remaining_lives)
    letter_guess = input(colored("Please guess a letter: ", "green", attrs=["bold"]))
    return letter_guess

def start_game():
### if player has guessed seven times, loss condition
### if player has revealed all letters in secret word, win condition
# import a list of words
# get a word from word bank
    words = open("words.txt", "r")
    secret_select = words.read().split(" ")
    secret_word = random.choice(secret_select)
    print(secret_word)

    secret_list = list(secret_word)
    masked_list = mask_word(secret_list)
    remaining_lives = ["√", "√", "√", "√", "√", "√", "√"]

    guessed_seven = False
    guessed_word = False
    while guessed_seven == False and guessed_word == False:
        letter_guess = user_input(masked_list, remaining_lives)

        result = check_if_guess_is_correct(letter_guess, secret_list, masked_list)
        # if guess is incorrect
        if result is None:
            remaining_lives.pop(0)

        if remaining_lives == []:
            guessed_seven = True
        else:
            pass

        if masked_list == secret_list:
            guessed_word = True
        else:
            pass
        #end while loop

    #check if the game is a win or loss; length == 0
    if guessed_seven == True:
        print("Sorry! You lose! The secret word was \"{}\".".format(secret_word))
    else:
        print("Congratulations! You win!")
        # you won

def check_if_guess_is_correct(guessed_letter, secret_list, masked_list):
    '''check if the given guessed letter is in the given secret list.
    If so, update the given masked list with the guessed letterself and return the new list.
    If the guess is not in the secret list, return None'''
    # if the guess is correct
    # if letter_guess in secret_list:
    did_replace_letter = False
    for (i, letter) in enumerate(secret_list):
        # check if guessed_letter is equal to letter
        if guessed_letter == letter:
        ## if so,
            ### replace the element in the masked_list at the i'th index with the guessed_letter
            masked_list[i] = guessed_letter
            ### set did_replace_letter = true
            did_replace_letter = True
        else:
            ## else, do nothing. continue for loop
            pass

    # check if did_replace_letter is true
    if did_replace_letter == True:
    ## if so, return the updated masked_list
        return masked_list
    else:
    ## else, return None
        return None

start_game()

def test():
    print(secret_select)
    print(secret_word)

# test()
