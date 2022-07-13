# name = input("What is your name? ")
# print("Hello " + name)
# birth_year = input("What is your birth year? ")
# age = 2022 - int(birth_year)
# print(age)

# first = float(input("first number: "))
# second = float(input("second number: "))
# print(first + second)
#
# course = 'Python for Beginners'
# print(course.upper())
# print(course.find('B'))
# print(course.replace('for', '4'))
# print("Python" in course)

# temp = 10
# if temp > 30:
#     print("It's a hot day " + str(temp))
# elif temp > 20:
#     print("It's a nice day " + str(temp))
# else:
#     print("Seems COLD!")

# weight = float(input("What is your weight: "))
# K_or_L = input("In (K)g or (L)bs: ")
# if K_or_L.upper() == "L":
#     print("weight in KG: " + str(weight * 0.453592))
#
# elif K_or_L.upper() == "K":
#     print("weight in Lbs: " + str(weight / 0.453592))
# else:
#     print("you didn't enter l or k")

# i = 1
# while i <= 5:
#     print(i * '*')
#     i = i + 1

# names= ["noah","bob","jay",'sam','mary']
# print(names[0])
# print(names[-1])
# names[0] = "jon"
# print(names)
# print(names[0:3])

# numbers = [1, 2, 3, 4, 5]
# numbers.append(6)
# numbers.insert(6, 4)
# numbers.remove(4)
# print(len(numbers))
# print(numbers)


# for item in numbers:
#     print(item)

# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i = i +1
#
# numbers = range(0, 5, 2)
#
# for number in numbers:
#     print(number)
#
# buzz = range(100)
# for fizz in buzz:
#     if fizz % 3 == 0:
#         print(str(fizz) + " fizz")
#     elif fizz % 5 == 0:
#         print(str(fizz) + " buzz")
#     else:
#         print(fizz)

# numbers = (1, 2, 3, 3)
# count = numbers.count(3)
# print(count, "two")

# --------------------------------------------------------

# def reverse_list(x):
#     return x.reverse()
#
#
# num = [1, 2, 3]
# y = reverse_list(num)
# # print(y)
# print(num)
#
#
# def powers_of_two(n):
#     return [2 ** i for i in range(n + 1)]
#
#
# print(powers_of_two(8))

# ------------------------------------------------------------------------
# beginner series #2 clock CODEWARS
# def past (h, m, s):
#     return (h * 3600000) + (m * 60000) + (s * 1000)
#
# print(past(3, 5, 6))
# -------------------------------------------------------------------------
# Calculate BMI

def bmi(weight, height):
    bmis = weight / height ** 2
    if bmis <= 18.5: return "Underweight"
    elif bmis <= 25: return "Normal"
    elif bmis <= 30: return "Overweight"
    else: return "Obese"


print(bmi(68, 74))

