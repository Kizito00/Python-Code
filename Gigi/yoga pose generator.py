#Yoga pose Generator
import random

yoga_pose = open("C:/Users/kiera/Desktop/Python/Gigi/list.txt").read().splitlines()
myline =random.choice(yoga_pose)
   
while True:
    response = input ("Good Morning, Would you like to do some yoga? (Yes/No) ").strip().lower()
    
    if response == "yes" or response == "y":
        print("Heres a yoga pose:", random.choice(yoga_pose))

        while True:
            response = input("Would you like to do another yoga pose? (Yes/No) ").strip().lower()
        
            if response == "yes" or response == "y":
                print("Heres a yoga pose:", random.choice(yoga_pose))
            elif response == "no" or response == "n":
                print ("Hope this made you feel better!") #stops the script  
                exit() 
            else:
                print("error: input is valid. Please enter 'yes' or 'no' ")
                if response == "Yes" or response == "y":
                    continue
                elif response == "no" or response == "n":
                    exit()
    
    elif response == "no" or response == "n":
        print ("Do some yoga lazy bones!")
        exit()
    else:
        print("error: input is valid. Please enter 'yes' or 'no' ") 




