import math


# Если сумма будет превосходить 2**32
def addModuleTwo(x, y, module=2 ** 32):
    return ((x + y) % module)


# сдвиг бинарной записи
def bitShift(s, sh):
    s = bin(s)[2:]
    s = int((s[sh:] + s[:sh]), 2)
    return s


# Вспомогательные функции
def F(B, C, D):
    return (B & C | ~B & D)


def G(B, C, D):
    return (B & D | ~D & C)


def H(B, C, D):
    return (B ^ C ^ D)


def I(B, C, D):
    return (C ^ (B | ~D))


# Четыре 32-битные переменные
A = int('01234567', 16)
B = int('89abcdef', 16)
C = int('fedcba98', 16)
D = int('76543210', 16)

bufer = [A, B, C, D]
functions = [F, G, H, I]

# Запрос текста
text = input('Введение исходного текста: ')

textInNumbers = ''

for i in range(len(text)):
    # Перевод элемента строки в двоичный вид
    text_element = text[i]
    textInNumbersElement = bin(ord(text_element))[2:]
    # Если длина двоичного вида < 8, то селва добавляем нули
    if len(textInNumbersElement) < 8:
        textInNumbersElement = '0' * (8 - len(textInNumbersElement)) + textInNumbersElement
    # Добавляем в конечную строку
    textInNumbers += textInNumbersElement

# Переводим длину строки в двоичный вид и добавляем нули слева от строки
length = bin(len(textInNumbers))[2:]
length = '0' * (64 - len(length)) + length

textInNumbers += '1'

# Пока длина строки не дает остаток 448 от деления на 512
while len(textInNumbers) % 512 != 448:
    # Дописываем 0
    textInNumbers += '0'

textInNumbers += length

m = [[] for i in range(len(textInNumbers) // 32)]
k = 0

# Проход по каждым 32 битам и записывание hexа в свой индекс (в список m)
for i in range(0, len(textInNumbers), 32):
    hexNumber = ''
    for j in range(4):
        p = hex(int((textInNumbers[i + 8 * j:i + j * 8 + 8]), 2))[2:]
        if len(p) < 2:
            p = '0' + p
        hexNumber += p
    m[k] = int(hexNumber, 16)
    k += 1

# Создаем константы
T = []
for i in range(1, 65):
    T += [round(2 ** 32 * abs(math.sin(i)))]
k = [hex(i) for i in T]

S = [[7, 12, 17, 22], [5, 9, 14, 20], [4, 11, 16, 23], [6, 10, 15, 21]]
K = [[], [], [], []]
K[0] = [int(i) for i in range(16)]
K[1] = [int(i) % 16 for i in range(1, 80, 5)]
K[2] = [int(i) % 16 for i in range(5, 53, 3)]
K[3] = [int(i) % 16 for i in range(0, 110, 7)]

ind_t = 0

# Изменяем buffer по алгоритму
for j in range(4):
    AA = bufer[0]
    BB = bufer[1]
    CC = bufer[2]
    DD = bufer[3]
    for k in range(16):
        bufer[0] = addModuleTwo(bufer[0], (functions[j](bufer[1], bufer[2], bufer[3])))
        bufer[0] = addModuleTwo(bufer[0], m[K[j][k]])
        bufer[0] = addModuleTwo(bufer[0], T[ind_t])
        bufer[0] = bitShift(bufer[0], S[j][k % 4])
        bufer[0] = addModuleTwo(bufer[1], bufer[0])
        bufer = bufer[3:4] + bufer[0:3]
        ind_t += 1
    bufer[0] = AA + bufer[0]
    bufer[1] = BB + bufer[1]
    bufer[2] = CC + bufer[2]
    bufer[3] = DD + bufer[3]

hexStr = '0x'
for i in bufer:
    h = hex(i)[2:]
    if len(h) < 8:
        h = '0' * (8 - len(h)) + h
    hexStr += h

# Выводим результат
print(hexStr)






