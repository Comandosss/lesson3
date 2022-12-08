# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.count('а'))

# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = set('УЕЫАОЭИЮуеыаоэию')
amount_vowels = 0
for count in word:
    if count in vowels:
        amount_vowels += 1
print(amount_vowels)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
amount = sentence.count(' ')
print(amount + 1)


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
word_list = sentence.split()
for count in word_list:
    print(count[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
amount_words = sentence.count(' ') + 1
word_list = ''.join(sentence)
len_letter_list = len(word_list)
avg_len = len_letter_list / amount_words
print(avg_len)
