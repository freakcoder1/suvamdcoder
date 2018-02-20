import random
print('Hello User, Welcome to rock, paper, scissors with suvam jaiswal')
print('What is your name?')
User = input()
print("lets begin")
import random
L=["rock","paper","scissor",]
count=0
while(count<=5):
    computer=random.choice(L)
    user=input("enter rock, paper or scissor")
    count+=1
    if(user=="rock"):
       if(computer==user):
           print("tie dishoom dishoom")

       elif(computer=="paper"):
            print("paper shadowed the rocks, computer wins")
       else:
           print("scissors were crushed by the stone, you win")
        
           
    elif  (user=="paper"):
         if(computer==user):
             print("tie blast")
           
         elif(computer=="rock"):
            print("paper shadowed the rocks, computer wins")

         else:
           print("scissors cut the paper, you lose")
           
        
                 
    elif  (user=="scissor"):   
          if(computer==user):
             print("tie blast")
           
          elif(computer=="paper"):
            print("scissor cut the paper,you win huraaay")

          else:
           print("rock crush the scissor, you lose")
           
             
