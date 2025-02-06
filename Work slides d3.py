
# print("welcome to the rollercoster!")
# height = int(input("What is your height in cm? "))
# bill = 0


# if height >= 120:
#     print("You can ride the rollercoaster!")
#     Age = int(input("What is your age? "))
#     if Age <= 12:
#         bill = 5
#         print("Child ticket is £5 ")
#     elif Age <= 18:
#         bill = 7
#         print("Youth ticket it £7")
#     else:
#        bill = 12
#        print ("Adult ticket is £12")

#     photo = input("Do you want a photo taken? Y/N ")
#     if photo == "y":
#         bill += 3

#     print(f"Your final bill is £{bill}")

# else:
#     print("Sorry youre too short to ride this rollercoaster")


# number = int(input("Please input a number? "))
# if number % 2 == 0:
#     print("This number is Even")
# else:
#     print("This number is Odd")

# weight = 80
# height = 1.85

# bmi = weight / (height ** 2)

# # 🚨 Do not modify the values above
# # Write your code below 👇

# if bmi < 18.5:
#     print ("underweight")
# elif bmi < 25:
#     print ("normal " )
# else:
#     print ("overweight")

#small = £15
#medium = £20
#large = £25

#Psmall = £2
#Pmedium/large = £3
#xcheese = £1

print ("Welcome to python pizza deliveries!")
size = input("Whast size pizza would you like? S, M, L: ")
pepperoni = input("Would you like pepperoni on your pizza? Y/N: ")
extra_cheese = input("Would you like extra cheese on your pizza? Y/N: ")
bill = 0

if size == "L":
    bill = 25
    print("Pizza will be £25")
    if pepperoni == "Y":
        bill += 3
    if extra_cheese =="Y":
        bill += 1
elif size == "M":
    bill = 20
    print ("Pizza will be £20")
    if pepperoni == "Y":
        bill += 3
    if extra_cheese =="Y":
        bill += 1
else:
    print ("Pizza will be £15")
    bill = 15
    if pepperoni == "Y":
        bill += 2
    if extra_cheese =="Y":
        bill += 1

print (f"Your Total order is £{bill}")



