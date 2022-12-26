# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 1

# 1 2 1 2 2
# Вывод: 2

# import random

# n = int(input("Введите N: "))
# count = 0
# array = []
# for num in range(0, n):
#     random_number = random.randint(0, 10)
#     array.append(random_number)
# print(array)

# x = int(input("Введите X: "))
# for i in range(len(array)):
#     if array[i] == x:
#         count +=1
# print(count)


# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

# import random

# n = int(input("Введите число N: "))
# array = []
# for num in range(n):
#     random_number = round(random.randint(1, n))
#     array.append(random_number)

# print(array)
# x = int(input("Введите число X: "))


# def number(count):

#     for i in range(0, len(array)):
#         if array[i] == x - count:
#             return array[i]
#         elif array[i] == x + count:
#             return array[i]

#     return number(count+1)


# print(number(0))

# Задача 20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Ввод: ноутбук
# Вывод: 12
print('Напишите программу, которая вычисляет стоимость введенного пользователем слова.'
 'Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.'
 'Write a program that calculates the cost of a word entered by the user.'
 'We will assume that only one word is given as input, which contains either only English or only Russian letters.')

dictionary = {   1 :'А, В, Е, И, Н, О, Р, С, Т, A, E, I, O, U, L, N, S, T, R' ,
                 2 :'D, G, Д, К, Л, М, П, У'  ,
                 3 : 'B, C, M, P, Б, Г, Ё, Ь, Я' ,
                 4 : 'F, H, V, W, Y, Й, Ы' ,
                 5 : 'K, Ж, З, Х, Ц, Ч' ,
                 8 : 'J, X, Ш, Э, Ю' ,
                 10: 'Q, Z, Ф, Щ, Ъ'
}

slovo = input('Введите слово на русском или английском языке\Enter a word in Russian or English: ')
slovo = slovo.upper()

res = 0
for i in slovo:
    if str.isalpha():
        res += dictionary
        print('Стоимость слова\Word cost: ')
    else:
        print('Некорректный ввод/Incorrect input')
