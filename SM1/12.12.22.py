# a = 3
# b = 1
# c = a + b
# print(c)

####################################################################################

#За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
#Input:
#n = 700
#m = 750
#Output:
#2

# n = int(input())
# m = int(input())
# t = (m+n-1)//n
# print(t)
################################################################


#В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся.
# Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
#Input: 20 21 22(ввод чисел НЕ в одну строку)
#Output: 32


# first = int(input('Первый класс '))
# second = int(input('Второй класс '))
# three = int(input('Третий класс '))
# sum1 = (first+1)//2
# sum2 = (second+1)//2
# sum3 = (three+1)//2
# print(sum1+sum2+sum3)

###############################################################


# Вагоны в электричке пронумерованы натуральными числами, начиная с 1 
# (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с 
# «хвоста»; это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер. 
# Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. Он хочет определить, 
# сколько всего вагонов в электричке. Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6


# def Locomotive():
#     i = int(input("Порядковый номер вагона: "))         Способ решения методом!
#     j = int(input("Номер на вагоне: "))
#     result = i + j - 1
#     print(result,"вагонов")
# Locomotive()    

################################################################



# Дано натуральное число. Требуется определить, является ли год с данным номером високосным. 
# Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем, 
# год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.
# Input: 2016
# Output: YES


# i = int(input("Ввудите год: "))
# if (i%4==0 and i%100!=0) or (i%400==0):
#     print("Yes")
# else:
#     print("No")    