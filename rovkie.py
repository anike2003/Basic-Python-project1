import random
print('''
Hey!!! You are about playing rock,paper,Scissors
      ''')
ch= ("rock","paper","scissors" )

num_start=0
num_end=3
user_score=0
comp_score=0
while num_start < num_end:
     user_choice=input("Please enter rock,paper or scissors: ").lower()
     comp_choice=random.choice(ch)
     num_start+=1
     if user_choice not in ch:
        print(" Dear player enter 'rock' 'paper' 'scissors' ")
        continue
     if user_choice == comp_choice:
        print("This is a tie")
     else:
         if user_choice=="rock":
           if comp_choice=="scissors":
             user_score+=1
             print("Hurray!!! you won")
           else:
             comp_score+=1
             print("You looose")
          
         if user_choice =="paper":
          if comp_choice=="rock":
            user_score+=1
            print("Hurray!!! you won")
          else:
            comp_score+=1
            print("You looose")
         
         if user_choice =="scissors":
           if comp_choice=="paper":
            user_score+=1
            print("Hurray!!! you won")
           else:             
             print("You loose")
             comp_score+=1
     
print(f"Total score = {user_score} - {comp_score}")

if num_start==num_end:
  ask= input("Do you want to continue of yes press /y, if no press any key to qiut: ").lower()
  if ask != "/y":
    print("You chose to quit buy :) ") 
    exit()
  else:
     print("You chose to continue let go!!!")
     while True: 
       user_score=0
       comp_score=0
       



