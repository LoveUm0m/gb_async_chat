#1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и также проверить тип и содержимое переменных.
word_1 = "разработка"
word_2 = "сокет"
word_3 = "декоратор"

#Проверка типа и содержания переменных в строковом формате
print(type(word_1), word_1)
print(type(word_2), word_2)
print(type(word_3), word_3)

#Преобразование строковых представлений в формат Unicode
unicode_word_1 = word_1.encode('unicode_escape').decode()
unicode_word_2 = word_2.encode('unicode_escape').decode()
unicode_word_3 = word_3.encode('unicode_escape').decode()

#Проверка типа и содержания переменных в формате Unicode
print(type(unicode_word_1), unicode_word_1)
print(type(unicode_word_2), unicode_word_2)
print(type(unicode_word_3), unicode_word_3)


#2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
word_1 = b"class"
word_2 = b"function"
word_3 = b"method"

#Проверка типа, содержания и длины переменных
print(type(word_1), word_1, len(word_1))
print(type(word_2), word_2, len(word_2))
print(type(word_3), word_3, len(word_3))


#3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
VAR_1 = 'attribute'
VAR_2 = 'класс'
VAR_3 = 'функция'
VAR_4 = 'type'

VAR_LIST = [VAR_1, VAR_2, VAR_3, VAR_4]

# Вариант 1
for el in VAR_LIST:
    try:
        print(bytes(el, 'ascii'))
    except UnicodeEncodeError:
        print(f'Слово "{el}" невозможно записать в виде байтовой строки')

# Вариант 2
# функция eval() интерпретирует строку как код
for el in VAR_LIST:
    try:
        print('Слово записано в байтовом типе:', eval(f'b"{el}"'))
    except SyntaxError:
        print(
            f'Слово "{el}" невозможно записать в байтовом типе с помощью префикса b')


#4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).
VAR_1_STR = 'разработка'
VAR_2_STR = 'администрирование'
VAR_3_STR = 'protocol'
VAR_4_STR = 'standard'

STR_LIST = [VAR_1_STR, VAR_2_STR, VAR_3_STR, VAR_4_STR]

ELEMS_B = []
for el in STR_LIST:
    el_b = el.encode('utf-8')
    ELEMS_B.append(el_b)

print(ELEMS_B)
print()

ELEMS_STR = []
for el in ELEMS_B:
    el_str = el.decode('utf-8')
    ELEMS_STR.append(el_str)

print(ELEMS_STR)
#5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.
import subprocess
import chardet

ARGS = ['ping', 'yandex.ru']
YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in YA_PING.stdout:
    result = chardet.detect(line)
    print(result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

#6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.

from chardet import detect

with open('test.txt', encoding='utf-8') as file:
    for line in file.read():
        print(line)
#file.close()

# UnicodeDecodeError: 'utf-8' codec can't decode
# byte 0xf0 in position 0: invalid continuation byte


# открываем файл в правильной кодировке
file = open('test.txt', 'rb')
for line in file:
    print(line.decode(encoding='utf-8'))
