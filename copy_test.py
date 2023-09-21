# foods = ['Pizza', 'sushi', 'icecream']
# you_food = foods[:]
# you_food [-1] = 'meat'
# print(foods)
# print(you_food)
# //--------------------------кортежі---------------------------------------------
# foods = ('Pizza', 'sushi', 'icecream')
# foods [0] = 'spagetti'
# print(foods) 
# (x, y) = (6, 8)
# print(x)
# print(y)
# x, y = y, x
# print(x)
# print(y)
# //-----------------------------------------------------------------------
# foods = ('Pizza', 'sushi', 'icecream','sup', 'rice')
# for food in foods:
#     print(food)
# //------------------------ділення по итерації-----------------------------------------------
# s = 'HEllo'
# print(list(s))
# p = list(s)
# p[0] = "O"
# print(p)
# //------------------------ділення по словам-----------------------------------------------
# text = "Lorem ipsum dolor sit amet"
# list_text = text.split()
# print(list_text)
# list_text.reverse()
# print(" ".join(list_text))
# //-----------------------------------------------------------------------
# type_words = input("Введіть послідовність чисел:").split(", ")
# print(type_words)
# numbers = []
# for i in type_words:
#     numbers.append(int(i))
# print(tuple(numbers))
# //-----------------------------------------------------------------------

# //--------------------------МНоЖИНИ-----------------------------------------------
# a = set([1,1,2,3,5,8,13,21,34,55,89])
# b = set([1,2,3,4,5,6,7,8,9,10,11,12,13])
# c = list(a.intersection(b))
# print(c)
# //---------------------------рядкові методи--------------------------------------------

# s = 'hEllo woRld'
# print(s.capitalize())
# print(s.title())
# print(s.upper())
# print(s.lower())
# print(s.swapcase()) 
# print(s.center(50))
# print(s.center(50))
# print(s.count('l'))
# score = 30
# print("Score:", score)
# print("Score: " + str(score))
# print(f"Score: {score}")
# print("Score: {}" .format(score))
# //-------------------------------------------------------------------------------------
# s = 'hEllo woRld'
# print(s.startswith("h"))
# print(s.endswith("m"))
# s1 = '            \n\n\naaaaaaa \n\n\n                   '
# print(s1.strip())
# //-------------------------------------------------------------------------------------
 
# a = 'Клара у Карла 123 вкрала кларнет 456'
# if 'р' in a:
#     print(a.title())
# print(a.count('а'))
# if not a.isalpha():
#     print(a.upper())
# if not a.isdigit():
#     print(a.lower())
# //------------------------------ФункціЇ-------------------------------------------------------
# //------------------------------ФункціЇ-------------------------------------------------------
# def greet_user(name, surname = "Pupkin"):
#     print("Hello,", name, surname)
    
# greet_user(name="Vasya", surname="Pupkin")
# greet_user("Petya", "Pyatochkin")
# //-------------------------------------------------------------------------------------
# def make_short(prints = "I love Python", size = "L"):
#     print("Розмір, ", size)
#     print("Прінт, ", prints)
# make_short("apple","50")
# make_short()
# make_short(size="M")
# make_short(prints="i = python")
# make_short(prints="MAC", size="60")
# //-------------------------------------------------------------------------------------
# import math
# def Geron (a, b, c):
#     p = (a+b+c)/2
#     s = math.sqrt(p*(p-a)*(p-b)*(p-c))
#     return s
# print ("Площа:", Geron(7,8,12))
# //-------------------------------------------------------------------------------------
# задача номер 3 
# def season (number_month):
#     if number_month in [12,1,2]:
#         return "Зима"
#     elif number_month in [3,4,5]:
#         return "Весна"
#     elif number_month in [6,7,8]:
#         return "Літо"
#     elif number_month in [9,10,11]:
#         return "Осінь"
#     else:
#         return "Такого місяця не існує"
# print(season(9))
# //-------------------------Рандомний пароль------------------------------------------------------------

# import random


# def random_password():
#     legth = random.randint(7, 10)
#     s = ""
#     for i in range(legth):
#         a = random.randint(33, 126)
#         s += chr(a)
#     return s
# print(random_password())

# //----------------------------------------------------------------------------------------------------
# from math import acos, sin, cos, pi
# t1= float(input("Enter coordinates t1:"))
# g1= float(input("Enter coordinates g1:"))
# t2= float(input("Enter coordinates t2:"))
# g2= float(input("Enter coordinates g2:"))
# distance = 6371.01 * acos(sin(t1)* sin(t2)+ cos(t1)* cos(t2)* cos(g1-g2))
# print (f"Відстань між точками {distance / pi} км")
# //----------------------------------------------------------------------------------------------------
# //----------------------------------------------------------------------------------------------------
def fibonachi ():
    fib1= 0
    fib2= 0
    n = int(input("Введіть порядковий номер числа"))
    for i in range(n-2):
      fib_sum = fib1 + fib2
      fib1=fib2
      fib2=fib_sum
print(f("{n} Число в ряді Фібоначчі це -  {fib_sum}"))




                   
                 

    



