#Step 1 

HANGMANPICS = ['''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


# FIX LOGIC NOT WORKING ON DUPLICATE CHARACTERS
# Fixed

import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list

chosen_word = random.choice(word_list)
display = []
lives = 6
hang_stage = 0
end_of_game = False
logo = hangman_art.logo

for i in range(len(chosen_word)):
    display.append('_')

life_reduced = False

print(logo)
while not end_of_game:
    guess = input('Guess a letter: ').lower()
    match_found = False

    for index, char in enumerate(chosen_word):
        if guess == char:
            display[index] = char
            print('Guessed letter: ', char)
            match_found = True
        
    if not match_found:
        if not life_reduced:
            lives -= 1
            print(HANGMANPICS[hang_stage])
            hang_stage += 1
            life_reduced = True

    life_reduced = False
    if '_' not in display:
        end_of_game = True
        print('You Win')
        print(f'{"".join(display)} was the word!')

    if lives == 0:
        end_of_game = True
        print('Game Over')
        print('The word was: ', chosen_word)
    print(display)