from IfStatements.hangman_words import word_list
from random import randint

# n = randint(1,100)
# print(n)
# print(word[])

# choose a random word
# indicate length of word
# initialise lives counter
# start guessing letters - begin while loop
#   Get user input
#       check input is single letter
#   if letter in word:
#       Iterate through letters in word:
#       If current letter is guessed letter:
#           Change Underscore to letter in current display
#   Else:
#       reduce lives by 1
# if word completed:
#   celebrate, end game (break)
# if lives run out:
#   Commiseration, end game (break)
#
Rand_Word_num = randint(1, len(word_list))

word = word_list[Rand_Word_num]
print(word)
word_len = len(word)
print(word_len)

lifes = 10

guess = 'E'
display = '_' * word_len
gameState = True
while gameState is True:
    guess = input().upper()
    if len(guess) != 1:
        print("Too many letters!")

    if guess in word:
        print('CORRECT')
        pos = 0
        for letter in word:
            if guess == letter:
                display = display[:pos] + letter + display[pos + 1:]
            pos += 1
    if display == word:
        print(f"Well done! You finished the game, with {lifes} lifes remaining")
        break
    elif guess != 1:
        lifes -= 1
        print(f"Ah, darn. Try again, only {lifes} Lifes remaining")

    print(display)
    print(lifes)
if lifes == 0:
    gameState = False


# correct = True
# while correct is True:
#     word_guess = input("Input Letter: ")
#
#     amount_blankspace = "_" * len(word)
#
#
#     if len(word_guess) != 1:
#         print("Too many letters")
#     else:
#         letter_index = word.find(word_guess)
#         print(letter_index)
#         print(amount_blankspace)
#           if word_guess == letter_index
#


# for letter in word:
#     if word_guess == letter:
#         print("You got it right")
#
#
# print(lifes)
#


# while word_guess == word:
#
#     if word_guess == word:
#         print("test")
#     break


# if lifes == 0:
#     print("You're out of lifes, Game over")
#         break()
