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

