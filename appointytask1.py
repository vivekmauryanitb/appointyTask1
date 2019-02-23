
import random   #for genrating random input from computer
from os import system, name
import numpy as np

c=0
d=0
u=0

#Help

print("Console app will first ask your choice of input.")
print("Enter a valid input for Rock Paper and Scissor")
print("System will show output of game")



import array 
   
res= array.array('i',[0, 0, 0])  

# to clear the console

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

for i in range(0,3):

#User Input

    player = input("Enter your choice (Rock/Paper/Scissor): ");

#to make user input in lower case for comparision
    player = player.lower();

    while (player != "rock" and player != "paper" and player != "scissor"):
        print(player);
        #for invalid inputs ask for another input
        player = input("That choice is not valid. Enter your choice (Rock/Paper/Scissor): ");
        player = player.lower();


#Computer Input

    computerInt = random.randint(0,2);
    if (computerInt == 0):
        computer = "rock";
    elif (computerInt == 1):
        computer = "paper";
    elif (computerInt == 2):
        computer = "scissor";
    else:
        computer = "Error...";
    print("Choice of Computer: %s" %(computer));    

#Checking Winner/Looser


    if (player == computer):
        print("Draw!");
        res[i]=2;
    elif (player == "rock"):
        if (computer == "paper"):
            print("Computer wins!");
        else:
            print("You win!");
            res[i]=1;
    elif (player == "paper"):
        if (computer == "rock"):
            print("You win!");
            res[i]=1;
        else:
            print("Computer wins!")
    elif (player == "scissor"):
        if (computer == "rock"):
            print("Computer wins!");
        else:
            print("You win!");
            res[i]=1;


#Printing Winners

    print("Your choice: " + player + "\nComputer choice: " + computer + "\nThank you for playing!");

    clear()
    print("\n")

for j in range(0,3):
    print("%d " %(res[j]));
for j in range(0,3):
    if(res[j]== 0):
        c = c+1;
    elif(res[j]==1):
        u = u+1;
    elif(res[j]==2):
        d = d+1;
print("Results of Best of three \n");


        

    
    




