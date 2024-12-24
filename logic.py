import requests

def get_word(length):
    url = f'https://random-word-api.herokuapp.com/word?length={length}'
    try:
        response = requests.get(url)

        if response.status_code == 200:
            word = response.json()[0]
            return word
        else:
            print('Error:', response.status_code)
            return None

    except Exception as e:
        print('Error:', e)
        return None

def check_word(word, guess):
    if word != guess and len(word) == len(guess):
        print(f'\033[93mLetters correct: {check_letter(word,guess)} \n\033[92mLetters in correct position: {check_position(word,guess)}. \033[39m')

    elif word == guess:
        print(f'\n\033[92mYou guessed right! The word was "{word}".')

    else:
        print('\033[91mThe length of the word is not correct.\033[39m')

def check_letter(word, guess):
    correct_letter = 0
    for letter in word:
        if letter in guess:
            correct_letter += 1
    return correct_letter

def check_position(word, guess):
    correct_letter_position = 0
    for i in range(len(word)):
        if word[i] == guess[i]:
            correct_letter_position += 1
    return correct_letter_position
