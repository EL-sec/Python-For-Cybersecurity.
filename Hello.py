# x = 4
# y = 6
# print(x)
# print(5)
# print(x+y)

# name = "my name is Emmanuel Okala"
# print(name)
# print("my name is Emmanuel Okala")
# print("name")

# f_name = "Emmanuel"
# l_name = "Okala"
# full_name = f_name + " " + l_name
# print(full_name)

age = 18
sentence = "legal age to vote in"
country = "Nigeria"
full_sentence = sentence + " " + country + " " + str(age)
print(full_sentence) 

# Types Of Variables 
# integers : They are whole numbers e.g 0 - 9
# floating point (float) : They are decimal values e.g 2.5
# strings (str) : They are text data e.g Emmanuel
# boolean (bool) : They are true or false data


# Dictionary: It's a collection of key-value pairs. It is used to store data value
# Dictionary are created using curly brackets.

cars = {"Toyota":"Camry","Acura":"ZDX","BMW":"M6","Ford":"Edge"}
print(cars)
print(cars["Toyota"])
print(cars["Acura"])
print(cars["BMW"])
print(cars["Ford"])
print(len(cars))

# List: It's a collection of item. It is used to store multiple items in a single variable.
# List is one of the 4 built-in data types in python. These data types are : Dictionary, List, Tuple & Set. 
# Lists are created using square brackets.

subjects = ["Maths","English","Physics","Chemistry","Geography"]
print(subjects)
print(len(subjects))
print(subjects[0])
print(subjects[1])
print(subjects[2])
print(subjects[3])
print(subjects[4])
print(subjects[0:4])
print(subjects[0:5])

subjects[0] = "backend"
subjects[4] = "devops"
print(subjects)

# Adding a new item to the list.

subjects.append("cloud")
subjects.append("data")
print(subjects)

# Removing an item from the list.

subjects.remove("data")
print(subjects)

# Removing an item from the list by index number 

subjects.pop(5)
print(subjects)

# Looping is a method used to call items per line or multiple times. 
# The different types of looping are 'for' & 'while'

# for subjects in subjects:
#     print(subjects)

# age_vote = input("how old are you: ")
# age = 18
# if age_vote == age: 
#     print("you can vote")
# elif age_vote < str(age):
#     print("go home")
# elif age_vote > str(age):
#     print("you can still vote")
# else:
#     print("vote wisely")

# Function is a block of code that only run when it is called.
# To call a function, type(call) the function after printing the infomation.
# Defining a function that greets people.

def greet():
    print("good morning")
greet()    

def subjects():
    print("data_analysis")
    print("cyber_security")
subjects()

# Passing argument to a function

def greet(name):
    print("good evening" + " " + name)
greet("Emmanuel")
greet("Ephraim")
greet("Chimaobi")


def sum_number(sum):
    return sum
print(10+10)
sum_number(sum)

# Write a function called divide_or_square that takes one argument (a number), and returns the square root of the number if it is divisible by 5, returns its remainder if it is not divisible by 5. For example, if you pass 10 as an argument, then your function should return 3.16 as the square root.


def divide_or_square(number):
    if number % 5 == 0:
        return number** 0.5
    else:
         return number % 5
print(divide_or_square(10))






