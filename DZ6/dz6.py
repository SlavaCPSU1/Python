# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# .
# Структура данных:
# Фамилия, имя, отчество, номер телефона.
# .
# Пример данных:
# Ivanov, Ivan, Ivanovich, +79111234567
# Petrov, Petr, Petrovich, +79119876543
# .
# Функции справочника:
# - Показать все записи
# - Найти запись по вхождению частей имени
# - Найти запись по телефону
# - Добавить новый контакт
# - Удалить контакт
# - Изменить номер телефона у контакта
# .
# Пример работы программы:
# .
# При запуске программы пользователю выдается меню:

# Введите номер действия:
# 1 - Показать все записи
# 2 - Найти запись по вхождению частей имени
# 3 - Найти запись по телефону
# 4 - Добавить новый контакт
# 5 - Удалить контакт
# 6 - Изменить номер телефона у контакта
# 7 - Выход

# .
# После выбора действия выполняется функция, реализующая это действие.
# После завершения работы функции пользователь возвращается в меню.


# import os
# import time


# fileName = 'DZ6/spravochnik.txt'


# def add_data():
#     while (True):
#         print('Добавление записи(""-выход)')
#         last_name = input("Фамилия: ")
#         first_name = input("Имя: ")
#         patronymic = input("Отчество: ")
#         phone_number = input("Номер Телефона: ")
#         data_to_save = [last_name, first_name, patronymic, phone_number]
#         save_data_to_file(data_to_save)
#         exit_data = input("Enter для выхода: ")
#         if exit_data == '':
#             return


# def save_data_to_file(data_to_save):
#     data_to_save = ",".join(data_to_save)+"\n"
#     print(data_to_save)
#     with open('spravochnik.txt', 'a', encoding='utf8') as datafile:
#         datafile.write(data_to_save)


# def readFile(file_name):
#     result = []
#     with open(file_name, 'r+', encoding='utf8') as data:
#         for line in data:
#             result.append(line.replace('\n', '').split(','))
#     return result


# def search_data():
#     while (True):
#         answer = input('Строка поиска(\'\'-выход) :>')
#         if answer == "":
#             return
#         result = []
#         with open(fileName, 'r', encoding='utf8') as datafile:
#             for line in datafile:
#                 result.append(line.strip('\n'))
#             result = list(filter(lambda line: answer in line, result))
#         print(' '.join(result))


# def print_all_data():
#     my_list = readFile(fileName)
#     num = 0
#     for i in my_list:
#         print(' '.join(i))
#         num += 1
#     input(f'Записано {num} Контактов, Enter для выхода>: ')


# def del_data():
#     my_list = readFile(fileName)
#     search = input(f'Введите данные которые хотите удалить>: ')
#     index = 0
#     for user in my_list:
#         for data in user:
#             if search == data:
#                 print(f"{' '.join(user)} {index} индекс")
#         index += 1
#     delete = input('введите индекс кого хотите удалить или Enter >: ')
#     if delete == '':
#         return
#     else:
#         my_list.pop(int(delete))
#         with open('spravochnik.txt', 'w', encoding='utf8') as data:
#             data.write('')
#         for i in my_list:
#             save_data_to_file(i)
#     input("Enter для выхода >: ")


# def Change_contact():
#     my_list = readFile(fileName)
#     search = input(f'Введите Имя или фамилию контакта>: ')
#     index = 0
#     for user in my_list:
#         for data in range(2):
#             if search == user[data]:
#                 print(f"{' '.join(user)} {index} индекс")
#         index += 1
#     change = input('введите индекс человека или Enter >: ')
#     if change == '':
#         return
#     else:
#         yslovie = input('вы хотите добавить номер "y" или его заменить "c">: ')
#         if yslovie == 'y':
#             my_list[int(change)].append(input('Введите номер>: '))
#         else:
#             if len(my_list[int(change)]) > 4:
#                 nomer = int(input('введите номер по счету>: '))+2
#             else:
#                 nomer = 3
#             my_list[int(change)][nomer] = input('Введите новый номер>: ')
#         with open('spravochnik.txt', 'w', encoding='utf8') as data:
#             data.write('')
#         for i in my_list:
#             save_data_to_file(i)
#     input("Enter для выхода >: ")





# menu = 'Телефонный справочник\n\n1 - Вывод данных\n\n2 - Добавление контакта\n\n'\
#     '3 - Поиск контакта\n\n4 - Удаление контакта\n\n5 - Замена(Добавка) номера\n\n6 - Выход \n\n'
# while (True):
#     print(menu)
#     answer = input('Ввод >: ')
#     match answer:
#         case "1":
#             # вывод данных
#             print_all_data()

#         case "2":
#             # добавление данных
#             add_data()

#         case "3":
#             # поиск
#             search_data()
#         case "4":
#             # удаление данных
#             del_data()
#         case "5":
#             # Замена номера
#             Change_contact()
#         case "6":
#             # выход
#             exit(0)

#         case _:
#             print("неверный ввод")
#             time.sleep(3)