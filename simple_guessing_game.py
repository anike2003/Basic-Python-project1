secrete_number =9
guess_count=0
guess_limit=3
while guess_count < guess_limit:
    guess = int(input("guess:"))
    guess_count+=1
    if guess == secrete_number:
        print("You won")
        break
    else:
        print("You loss")