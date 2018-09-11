# Requirements:
#


# from collections import Counter
import random

word_list = ["neptune", "pistachios", "orangutan"]

# secret_word = random.choice(word_list)
secret_word = "apple"
secret_list = list(secret_word)

# creates blank phrase to be replaced with correct guesses
def masked_word():
    hidden_word = "-" * len(secret_list)
    return hidden_word

# counts the number of each letter in the secret word
# def count_letters():
#     counted = {}
#     counted = Counter(secret_word)
#     return counted

# gets user input
def user_input(prompt):
    user_input = input(prompt)
    return user_input

# gets index of all occurrences of guessed letter
def check_word(letter, copy_secret_word):
    current_letter = copy_secret_word.rfind(letter)
    index_list = []
    while current_letter != -1:
        index_list.append(current_letter)
        copy_secret_word = copy_secret_word[:current_letter]
        current_letter = copy_secret_word.rfind(letter)
    return index_list

# replaces all occurrences of correctly guessed letter in secret word
replaced_word = ""
def replace(check_word, masked_word, letter_choice):
    for x in check_word:
        word_h = '%s%s%s'%(masked_word[:x], letter_choice, masked_word[x+1:])
    return masked_word

# checks guessed letter and allows player to proceed
def letter_choice(game_choice):
    if game_choice.isalpha() == True & len(game_choice) == 1:
        check_word(game_choice, secret_list)
        return False
    else:
        print("Please do not enter a number or a punctation mark. Please choose one letter at a time. Try again: ")
        return True

# checks if game has been won or lost
def game_not_won(letter, word):
    # Game still ongoing
    if replaced_word.find("-") != -1:
        unguessed_word = masked_word()
        user_letter = letter_choice(letter)
        word_index = check_word(user_letter, word)
        replace(word_index, unguessed_word, user_letter)
    # Win condition
    elif replaced_word.find("-") >= 0:
        print("Congratulations! You're down to earth!")
    # Loss condition
    else:
        print("Ground control to Major Tom! Time for blast off!")

# prompts player to guess a letter
letter_unchosen = True
while letter_unchosen:
    print(masked_word())
    choose_letter = user_input("Please select a letter: ")
    word = "word"
    letter_unchosen = game_not_won(choose_letter, word)

# test function
def test():
    print(count_letters())
    print(masked_word())
    print(replace([2, 1], "-----", "p"))
    print(list(secret_word))
# test()
