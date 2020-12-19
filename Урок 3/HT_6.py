def letter_up(word):
    a = word.title()
    print(a)


user_word = input('Введите слово с маленькой буквы: ')
letter_up(user_word)


def words_up(words):
    words_upper = words.title()
    print(words_upper)


user_words = input('Введите любое предложение с маленькой буквы: ')
words_up(user_words)
