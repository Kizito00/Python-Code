


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

    print(f"Your final bill is £{bill}")

else:
    print("Sorry youre too short to ride this rollercoaster")

