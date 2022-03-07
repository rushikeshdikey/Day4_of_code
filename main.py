# start to python day-4 code
# starting code is basics learned
# main project code at end

# Author: Rushikesh Dikey
# Date: 07-03-2022

# Leap year calculator

# year = int(input("Enter year to check is it a leap year or not "))
#
# if(year%4 == 0):
#     if(year%100 == 0):
#         if(year%400 == 0):
#             print("Leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year")
#
# Rollercoaster entry

# print("Welcome to the Rollercoaster\n")
#
# hieght = int(input("What is your hieght in cms? "))
# bill = 0
#
# if hieght >= 120:
#     print("You can ride the rollercoster")
#     age = int(input("Enter your age: "))
#
#     if age < 12:
#         print("Child tickets are ₹5")
#         bill = 5
#     elif age <= 18:
#         print("Youth tickets are ₹7")
#         bill = 7
#     else:
#         print("Adult tickets are ₹12")
#         bill = 12
#     photo = input("Do you want photograph? enter Y or N: ")
#
#     if photo == 'Y':
#         bill = bill +3
#         print(f"Total bill is ₹ {bill}")
#     else:
#         print(f"Total bill is ₹ {bill}")
#
# else:
#     print("Sorry, you can grow your taller before you ride")

# Pizza bill generator

print("Welcome to DK's Pizza")

size = input("What size pizza do you want S, M or L: ")
pepperoni = input("Do you want pepperoni Y or N: ")
chesse = input("Do you want extra chesse Y or N: ")

bill = 0

if size == 'S':
    bill = 250
elif size == 'M':
    bill  = 550
else:
    bill = 850

if pepperoni == 'Y':
    if size == 'S':
        bill += 50
    elif size == 'M':
        bill += 80
    elif size == 'L':
        bill +=110
if chesse == 'Y':
        bill += 30
else:
    print("Try adding cheese")

print(f"Your final bill is: ${bill}.")