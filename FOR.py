# Ваша задача – написать код, который подсчитывает сумму всех чётных чисел 
# в заданном диапазоне от 1 до N.
#Число N - верхняя граница диапазона
#Напишите код, который подсчитывает сумму всех чётных чисел от 1 до N включительно, 
# и выводит это число.
#Используйте цикл for и функцию range для создания диапазона чисел.

N = 99
x = 0
for i in range(0,N+1,2):
    x += i
#print(x)

#Задание: Найти самое длинное слово
#Ваша задача – написать код, который находит самое длинное слово в заданной строке. 
# Слова в строке разделены пробелами.

#Дано:

#Строка text - текст для анализа.
#Задание:

#Напишите код, который находит самое длинное слово в строке и выводит это слово.
#Если у нескольких слов одинаковая длина, нужно вывести то, что находится раньше.
#Используйте цикл for для прохождения по словам в строке.
#Чтобы разделить строку на отдельные слова используйте функцию .split(' ')

text = 'Student eight natural actually big hair still wrong officer though girl during project daughter then place stuff senior.'

#longest = ''
max_length = 0
for length in (text[0:text.find('.')]).split(' '):
    #print(length)
    current_length = len(length)
    #print(length, current_length, max_length)
    #print(max_length)
    if current_length > max_length:
        print(current_length, max_length)
        longest = length
        #print(longest, length, max_length)
        max_length = current_length
#print(longest)
