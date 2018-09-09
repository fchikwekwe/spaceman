# Requirements:
#
#

from collections import Counter
import random

word_list = ["neptune", "pistachios", "orangutan"]

# secret_word = random.choice(word_list)
secret_word = "apple"

# creates blank phrase to be replaced with correct guesses
def word_length():
    masked_word = "-" * len(secret_word)
    return masked_word

# counts the number of each letter in the secret word
def count_letters():
    counted = {}
    counted = Counter(secret_word)
    return counted

# gets user input
def user_input(prompt):
    user_input = input(prompt)
    return user_input

# gets index of all occurrences of guessed letter
def check_word(letter, my_copy_of_secret_word):
    current_letter = my_copy_of_secret_word.rfind(letter)
    index_list = []
    while current_letter != -1:
        index_list.append(current_letter)
        my_copy_of_secret_word = my_copy_of_secret_word[:current_letter]
        current_letter = my_copy_of_secret_word.rfind(letter)
    return index_list

# replaces all occurrences of correctly guessed letter in secret word
word_length
def replace(check_word, word_length, letter_choice):
    for x in check_word:
        word_length = '%s%s%s'%(word_length[:x], letter_choice, word_length[x+1:])
    return word_length

# checks guessed letter and allows player to proceed
def letter_choice(game_choice):
    if game_choice.isalpha() == True & len(game_choice) == 1:
        check_word(game_choice, secret_word)
        return False
    else:
        print("Please do not enter a number or a punctation mark. Please choose one letter at a time. Try again: ")
        return True

# checks if game has been won or lost
def game_not_won(letter):
    # Game still ongoing
    if replace.find("-") != -1:
        letter_choice(letter)
    # Win condition
    elif replace.find("-") >= 0:
        print("Congratulations! You're down to earth!")
    # Loss condition
    else:
        print("Ground control to Major Tom! Time for blast off!")

# prompts player to guess a letter
letter_unchosen = True
while letter_unchosen:
    print(word_length())
    choose_letter = user_input("Please select a letter: ")
    letter_unchosen = game_not_won(choose_letter)


# test function
def test():
    print(count_letters())
    print(word_length())
    print(replace([2, 1], "-----", "p"))
