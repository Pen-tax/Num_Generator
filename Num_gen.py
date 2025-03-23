## user inputs some paramiter and then random numbers get chosen
import random

def randnum():
  checks = False
  while checks == False:
   ## allows user to input paramiters
    try:
      min = int(input("Please enter the Lowest number to be picked\nEnter Here: "))
      max = int(input("Please enter the Highest number to be picked\nEnter Here: "))
      amount = int(input("Please enter how many numbers in will be picked\nEnter Here: "))
      checks = True
    except:
     print("Please enter a number")
    ## loops to match the amount needed  
    number = 0
    while number != amount:
      number = number + 1
      print(random.randint(min,max))
  
## main
randnum()