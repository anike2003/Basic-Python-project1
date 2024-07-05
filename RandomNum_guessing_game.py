import random
num=random.randint(1,5)
guess_time_start=0
guess_time_stop = 5
while guess_time_start < guess_time_stop :
   guess_num = float(input("Guess a number:"))
   guess_time_start+=1
   if guess_num == num:
      print("Correct that the number!!!")
      break
   elif num < guess_num:
       print("Too high")
   else:
       print("Too low")
else:
      print("Oops all your guesses are Wrong!!!")










