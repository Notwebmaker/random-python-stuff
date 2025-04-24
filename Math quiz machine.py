# this is the most "complex" in this repo, It may be challenging to understand for newcomers
import random
incorrect=0
correct=0
a=0

name=input('what is your name?')

z=int(input("Hello "+(name)+", welcome to the math quiz machine! \n how many questions do you want?").strip() or 10)

oper=int(input("what type of question do you want?\n 1 for multiply \n 2 for addition\n 3 for division\n 4 for subtraction\n 5 for random ").strip() or 5)#asks for question type defaults to 5 (random) on no answer
difficulty=int(input("what difficulty do you want?\n 1 for easy\n 2 for meduium\n 3 for hard ").strip() or 1) # asks for the difficulty, defaults to 1 (easy)on no answer
ques=oper#signifies that the variable 'ques'is equal to 'oper'(this is so the random element work correctly)

#difficulty perameters (MAX_value determines the highest number in a question )
if difficulty == 1:
  MAX_value=7
elif difficulty == 2:
  MAX_value=13
elif difficulty == 3:
  MAX_value=25
  

for i in range(z):
  x=random.randrange(1,MAX_value)
  y=random.randrange(1, MAX_value)
  #randomly chooses type of question if set to random option
  if oper == 5:
    ques = random.randrange(1, 5)
    #code for multiplication
  if ques == 1 :   
    a=int(input("what is "+ str(x) +" times "+ str(y)+": ")) 
    if a == (x*y):
      print ("That is correct")
      correct+=1 #adds 1 to the 'correct' variable if right
    else:
      print ("incorrect, the answer is "+ str(x*y))
      incorrect+=1 # adds 1 to the 'incorrect' variable if wrong
  elif ques == 2 :
    
    #code for addition
    a=int(input("what is "+ str(x) +" plus "+ str(y)+": ")) 
    if a == (x+y):
      print ("That is correct")
      correct+=1
    else:
      print ("incorrect, the answer is "+ str(x+y))
      incorrect+=1
  #code for division
  elif ques == 3 :
    # anti decimal point code for division , forces a new set of numbers if the answer results in a decimal point
    while ((x/y)%1)>0:
      x=random.randrange(4,MAX_value)
      y=random.randrange(2,MAX_value) 
      #debug print (str(x) + " / " + str(y) + " = " + str((x/y)%1)) # this is leftover debug code from creating the program 
    a=float(input("what is "+ str(x) +" divided by "+ str(y)+": ")) # float instead of int used in case you want to remove the anti decimal point code
    
    if a == (x/y):
      print ("That is correct")
      correct+=1
    else:
      print ("incorrect, the answer is "+ str(x/y))
      incorrect+=1
  #code for subtraction
  elif ques == 4  :
    a=int(input("what is "+ str(x) +" minus "+ str(y)+": "))  
    if a == (x-y):
      print ("That is correct")
      correct+=1
    else:
      print ("incorrect, the answer is "+ str(x-y))
      incorrect+=1

    
  else:
    #fallback code if for some reason 'ques' or 'oper' is more than 4
    a=int(input("what is "+ str(x) +" times "+ str(y)+": "))
    if a == (x*y):
      print ("That is correct")
      correct+=1
    else:
      print ("incorrect, the answer is "+ str(x*y))
      incorrect+=1
    
#answers code
print ("you had "+str(correct)+" correct answers and "+str(incorrect)+ " incorrect answers" )  #shows correct and incorrect answers
print ("or "+str(correct)+ " out of "+ str(z) )#also shows correct and incorrect answers
percent=round((correct/z)*100,2) #calculating percentage
print ("or "+str(percent)+" % correct")#printing percentage
