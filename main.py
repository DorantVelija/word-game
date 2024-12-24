from logic import get_word, check_word

print('Input the word length: ')
length = int(input())
word = get_word(length)
guess = ''
print(word)

while guess != word:
    print('Guess a word: ')
    guess = input().lower()
    check_word(word, guess)
