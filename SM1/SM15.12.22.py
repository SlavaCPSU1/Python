#Задача 9
# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while


# Input:       5

# Output:    120



# n = int(input())

# def factorial(n):
#     result = 1
#     while n > 1:
#         result *=n
#         n*=1
#         print(factorial(n))


# Задача №11
# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.

# Input:     5
# Output:  6


# def fibonache(n):
#     # 0 1 1 2 3 5 8 

#     if n == 0:
#         return 1
#     if n == 1:
#         return 2 
#     number0 = 0
#     number1 = 1
#     count = 2
#     while n >= number1:
#         if n == number1:
#             return count
#         temp = number1
#         number1 += number0
#         number0 = temp
#         count += 1
#     return -1

##################################
# import random

# n = 100
# m = []
# for num in range(0,n):                                      Рандомные числа, генератор!
#     random_number = round(random.uniform(-50,50),0)
#     m.append(random_number)


# print(m)

###############################################
# Задача №13
# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. 
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. 
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
# В следующих строках располагается N целых чисел. 
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50

# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2
 
#  import random
# n = 10
# m = []
# max_count = 0
# count = 0
# for num in range(0,n):
#     random_num = random.randint(-50,50)
#     m.append(random_num)
#     if random_num > 0:
#         count += 1
#     else:
#         if count > max_count:
#             max_count = count
#         count = 0

# print(max_count)
# print(m)


# Вариант решения 2


# def sinoptik(N):
#     days=[]
#     for _ in range(N):
#         days.append(round(random.uniform(-10,50),0))  
#     print(days)
#     maxPeriod = maxPeriodResult = 0
#     i = 0
#     while i<n:
#         if days[i]>0:
#             while days[i]>0:
#                 maxPeriod+=1
#                 i+=1
#             if maxPeriodResult<maxPeriod: maxPeriodResult=maxPeriod
#         maxPeriod=0
#         i+=1
#     return maxPeriodResult



# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

# def arbuzLine(N):
#     arbuzes=[]
#     for _ in range(N):
#         arbuzes.append(random.randint(5000,30000))
#     arbuzes.sort()
#     print(arbuzes)
    
#     min=max=arbuzes[0]
#     for item in arbuzes:
#         if min>item: min = item
#         elif max < item: max = item
    
#     return min, max

