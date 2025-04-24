import random

b =(random.randrange(1, 100)) #selects secret number
c=0#for counting number of tries

while True:# infinite repeat, can only be stopped with 'break', ctrl c , or closing the window
    a = int(input("Guess the secret number under 100!: "))
    print("your guess is :" + str(a))

    if (c == 45):# if you make to many guesses the number will change, this prevents brute forcing
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

        
    


 
