import random

b =(random.randrange(1, 100))
c=0

while True:
    a = int(input("Guess the secret number under 100!: "))
    print("your guess is :" + str(a))

    if (c == 50):
        print ('too many guesses, secret number changed')
        b =(random.randrange(1, 100))
        c=0

    if(a == b):# checks if guess is exact
        
        print("that is correct!")
        print("You win")
        break # ends the code after winning
    elif(a > b):# displayed when guess is too high
        print("too high try again")
        c+=1

        
    else:
        print("too low mate, try again")
        c+=1

        
    


 
