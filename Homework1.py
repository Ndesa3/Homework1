import random
low = 1
high = 100
mid = 0
tries = 0
number = 0
print('Hello! What is your name?')
myName = input()
print('Well, ' + myName + ', Think of random number from 1 to 100, and I will try to guess it!')
while(True):
    tries = tries + 1
    mid = int((low+high)/2)
    print("Is it ",mid," ?")
    cont = str(input("yes/no : "))
    if cont == 'yes' :
        print (mid, "Good Job!! You Get the correct Guess")
        print ("No of tries is ", tries)
        if cont == str(input("Do you want to play more? (yes/no)")) :
            low = 1
            mod = 0
            high = 100
            tries = 0
        else:
            exit()
    if cont == 'no' :
        print("It is greater than",mid," ?")
        cont_local = str(input("yes/no : "))        
        if cont_local == 'yes':        
            low = mid
        if cont_local == 'no' :        
            high = mid
