import random
incorrect=0
correct=0
a=0

name=input('what is your name?')

z=int(input("Hello "+(name)+", welcome to the math quiz machine! \n how many questions do you want?").strip() or 10)

oper=int(input("what type of question do you want?\n 1 for multiply \n 2 for addition\n 3 for division\n 4 for subtraction\n 5 for random ").strip() or 5)
difficulty=int(input("what difficulty do you want?\n 1 for easy\n 2 for meduium\n 3 for hard ").strip() or 1)
ques=oper

if difficulty == 1:
  MAX_value=7
elif difficulty == 2:
  MAX_value=13
elif difficulty == 3:
  MAX_value=25
  

for i in range(z):
  x=random.randrange(1,MAX_value)
  y=random.randrange(1, MAX_value)
  if oper == 5:
    ques = random.randrange(1, 5)
  if ques == 1 :   
    a=int(input("what is "+ str(x) +" times "+ str(y)+": "))
    if a == (x*y):
      print ("That is correct")
      correct+=1
    else:
      print ("incorrect, the answer is "+ str(x*y))
      incorrect+=1
  elif ques == 2 :
    
    
    a=int(input("what is "+ str(x) +" plus "+ str(y)+": "))
    if a == (x+y):
      print ("That is correct")
      correct+=1
    else:
      print ("incorrect, the answer is "+ str(x+y))
      incorrect+=1
  elif ques == 3 :
    
    while ((x/y)%1)>0:
      x=random.randrange(4,MAX_value)
      y=random.randrange(2,MAX_value) 
      #debug print (str(x) + " / " + str(y) + " = " + str((x/y)%1))
    a=float(input("what is "+ str(x) +" divided by "+ str(y)+": "))
    
    if a == (x/y):
      print ("That is correct")
      correct+=1
    else:
      print ("incorrect, the answer is "+ str(x/y))
      incorrect+=1
  elif ques == 4  :
    a=int(input("what is "+ str(x) +" minus "+ str(y)+": "))  
    if a == (x-y):
      print ("That is correct")
      correct+=1
    else:
      print ("incorrect, the answer is "+ str(x-y))
      incorrect+=1

    
  else:
    #print("invalid answer defaulting to multiplication") 
    a=int(input("what is "+ str(x) +" times "+ str(y)+": "))
    if a == (x*y):
      print ("That is correct")
      correct+=1
    else:
      print ("incorrect, the answer is "+ str(x*y))
      incorrect+=1
    
    
print ("you had "+str(correct)+" correct answers and "+str(incorrect)+ " incorrect answers" ) 
print ("or "+str(correct)+ " out of "+ str(z) )
percent=round((correct/z)*100,2)
print ("or "+str(percent)+" % correct")
