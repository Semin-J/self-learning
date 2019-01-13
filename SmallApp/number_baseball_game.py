# Semin Jeon
# Last mod: 2019/Jan/13

import random

def random_number():
    n = random.sample(range(10), 3)
    if n[0] == 0 :
        while n[0] == 0 :
            n = random.sample(range(10), 3) 
            
    key = ""
    for i in range(0,3,1) :
        key += str(n[i])
    return key

def baseball_game():
    key = random_number()  
    loop = True
    while loop:
        user = input("put your number : ")
        strike = 0
        ball = 0
        if user.isnumeric() == False:
            print("Please enter \"3-digit numbers\"")
        else:
            if user[0] == user[1] or user[0] == user[2] or user[1] == user[2]:
                print("each number should be different")
            else :
                for i in range(0,3,1):
                    for k in range (0,3,1):
                        if key[i] == user[k] and i == k:
                            strike += 1
                            
                        elif key[i] == user[k] and i != k:
                            ball += 1
                if strike == 3 :
                    print("HOMERUN!!!")
                    loop = False
                elif strike != 0 and ball != 0:
                    print(strike, "strike")
                    print(ball, "ball")
                elif strike != 0 and ball == 0:
                    print(strike, "strike")
                elif strike ==0 and ball != 0:
                    print(ball, "ball")
                elif strike ==0 and ball == 0:
                    print("OUT!")
                
    print("The answer is", key, "!!!")
       

def main():
    print(" *******************************************************\n",
    "********** Welcome to Number Baseball Game!! **********\n",
    "1. Please enter 3-digit number\n",
    "2. Each digit has a different number\n",
    "3. When the numbers and digits is correct -> strike\n",
    "4. When only the numbers are correct but digit -> ball\n",
    "*******************************************************\n")



main()
resume = "y"
while (resume == "y" or resume == "Y"):
    baseball_game()
    resume = input("Do you want to play again? (y/n) : ")
print("Thank you for playing!")
input()

