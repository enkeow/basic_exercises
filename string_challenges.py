# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.count('а'))
    

# Вывести количество гласных букв в слове
word = 'Архангельск'
wovels = 'а у о ы э я ю ё и е'
count = 0
for i in word:
    if i.lower() in wovels:
        count += 1
print(count)
print()

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for i in sentence.split():
    print(i[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
a = sentence.split()
b = 0
for i in a:
    b+=len(i)
print(b/len(a))
