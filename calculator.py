print('2 operent calculator (only one symbol in equation)')
while True:
    a = int(input("Enter 1st number: "))
    print("first number is: " + str(a))
    c = input ("enter symbol (+-/*)")
    print (c)
    b = int(input("Enter 2nd number: "))
    print("second number is: " + str(b))
    numbers = [a,b]
    if(c == '+'):
        d=a + b
    elif(c == '-'):
        d=a-b
    elif(c== '/'):
        d=a/b
    else:
        d=a*b

    print(a,c,b,'equals',d)
    e = (input("new calculation? y n: "))
    if e==('n'):
        print('')
        print("Program terminated")
        break
    
    
