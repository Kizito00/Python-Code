# print("Hello " + input("What is your name? ") + "!")  input("What is your name? ")


# name = "Kieran"
# print(len(name))

# name ="Simon"
# print(len(name))


# print(len(input("what is your name?")))

#user_name = input("what is your name? ")
#length = len(user_name)
#print (length)


print("welcome to the rollercoster!")
height = int(input("What is your height in cm? "))
bill = 0


if height >= 120:
    print("You can ride the rollercoaster!")
    Age = int(input("What is your age? "))
    if Age <= 12:
        bill = 5
        print("Child ticket is £5 ")
    elif Age <= 18:
        bill = 7
        print("Youth ticket it £7")
    else:
       bill = 12
       print ("Adult ticket is £12")

    photo = input("Do you want a photo taken? Y/N ")
    if photo == "y":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry youre too short to ride this rollercoaster")


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