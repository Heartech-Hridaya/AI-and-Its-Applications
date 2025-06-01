# def main():
#     a=int(input("enter a number- "))

#     b= a / 130
#     print(f"your inputed Rupe amount {a} in dolar is {b:.2f} ")

# main()

# name ="Hridaya"
# age = 18
# print(type(age))
# 
# print("I am "+name)

# a = 4
# b = "mathyyy"
# c = str(a) + b

# print(c)

# a=50
# b=2.22
# c= "jjrrr"
# d= True

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

#Conditionals


# try:
#     a=int(input("Enter a number- "))
#     if (a>0):
#         print(f"{a} is a positive number")
#     elif (a<0):
#         print(f"{a} is a Negative number")
#     else:
#         print("You have entered 0")
# except:
#     print("Please enter an integer from -infinity to infinity")



#Loops


# try:

#     a=int(input("Enter a number- "))

#     for i in range(0,a):
#         print("Hello Bishal")
# except:
#         print("Please enter a number")

# import random

# choices = ['rock', 'paper', 'scissors']

# user_choice = input("Enter rock, paper, or scissors: ").lower()

# computer_choice = random.choice(choices)

# print(f"Computer chose: {computer_choice}")

# def main():
        
#     if user_choice == computer_choice:
#         print("It's a tie!")
#     elif (user_choice == 'rock' and computer_choice == 'scissors') or \
#         (user_choice == 'paper' and computer_choice == 'rock') or \
#         (user_choice == 'scissors' and computer_choice == 'paper'):
#         print("You win!")
#     elif user_choice in choices:
#         print("Computer wins!")
#     else:
#         print("Invalid input. Please choose rock, paper, or scissors.")

# main()


# age=int(input("Enter your age - "))

# if(age>=18):
#     print("You can Vote")
# else:
#     print("You can not Vote")

#Homework: WAP to check whether an entered number is odd or even


# a=int(input("Enter a number - "))
# if (a % 2 ==0):
#      print(f"{a} is a even number")
# elif (a % 2 != 0):
#      print(f"{a} is a odd number")
# else :
#      print("Please enter a valid integer ")

# r=int(input("Enter a radius for a circle"))
# def areaofcircle(r):
#   pi = 3.65
#   area = pi *r*r
#   return area

# print(f"The area of the given circle is {areaofcircle(r)}")


####################  Homework  ####################

# import datetime  #It is used to include Python's built-in datetime module, which allows us to work with dates and times.
# by = int(input("Enter your date of birth - "))
# cy = datetime.datetime.now().year
# age = cy-by
# print(f"Your age is {age}yrs old") 



# principal = float(input("Enter principal amount - "))
# rate = float(input("Enter rate of interest - "))
# time = float(input("Enter time taken in years - "))

# SI = (principal*rate*time)/100
# print(f"Your Simple interest is Rs.{SI:.2f}") 



# wt = float(input("Enter your weight (in kg) - "))
# h = float(input("Enter your height (in meters) - "))

# BMI = wt/(h**2)

# if BMI < 18.5:
#     category = "Underweight"
# elif 18.5 <= BMI < 24.9:
#     category = "Normal weight"
# elif 25 <= BMI < 29.9:
#     category = "Overweight"
# else:
#     category = "Obese"

# print(f"Your Body Mass Index is :{BMI:.2f}") 
# print(f"Your weight catagoey is :{category}") 



# rs = float(input("Enter an amount in NRP: Rs-"))
# usd = rs/132
# print(f"Your entered amount in USD id :{usd:.2f}$") 




####################  Homework2  ####################

# import math as m
# sine_of_30 = m.sin(m.radians(30))
# print(f"sine of 30 degrees using m.sin(m.radians(30) is : {sine_of_30:.3f}") 

# import random as ran 
# r = ran.randint(50,70)
# print(f"A ramdom integer between 50-75 is : {r}")


# %%writefile cal.py
# import math as m
# def square(x):
#   return  m.pow(x, 2)

# import cal
# print(f"The square of 8 is : {int(cal.square(8))}")

# import random as r
# fruits = ["Mango","Aple","Grape"]
# rc = r.choice(fruits)
# print(f"A random fruit from the list id - {rc}")

# try:
#     x=int(input("Enter number: "))
#     print(10/x)
# except ValueError:
#     print("Invalid input")
# except ZeroDivisionError:
#     print("cannot br divided by 0")
# finally:
#     print("Finally done")


#####3 



lang = input("Enter a word to convert - ")
v = lang[0]
if (lang[0] == "a"):
    for i in range (0,len(lang)):
        if (lang[i]=="a" or lang[i]=="e" or lang[i]=="i",lang[i]=="o",lang[i]=="u"):
            rest = lang[i:]
            break
        else:
            v = v + lang[i]
            
    
else:
        v = lang[0:2]
        rest = lang[2:]

final = "Ma" + rest + v + "da"

print(f"Your encoded word is : {final}")
