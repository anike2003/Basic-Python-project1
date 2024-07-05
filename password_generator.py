import random

lst_small_characters = ["jq" , "bp" , "ck" , "dl" , "em" , "fn" , "gd" , "hy"]
lst_upper_characters = ["ADF", "GVB" , "GYY" , "SXC"]
lst_special_char = ["#" , "&" , "@"]


char = random.choice(lst_small_characters)
sp_char = random.choice(lst_special_char)
up_char = random.choice(lst_upper_characters)
num = random.randint(100 , 1000)

password = f"{char}{sp_char}{up_char}{num}"

print(f"Your password is : {password}")

