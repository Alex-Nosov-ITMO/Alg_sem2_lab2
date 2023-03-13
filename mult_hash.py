string = [i for i in input("Введите фразу: ").split()]   # исходная фраза

stringHash = ''                                           # строка для сохранения хешированной фразы
c = 0.3                                                   # константа от 0 до 1
key = int(input("Введите ключ: ")) # ключ

for i in range(len(string)):
    # перебираем каждое слово в фразе и хешируем по принципу умножения, а затем добавляем в hash
    stringHash += str(int((len(string[i]) * ((key * c) % 1))))

print(stringHash)



