is_male = False
is_tall = True
if is_male and is_tall:
    print("you are a male tall male")
elif is_male and not is_tall:
    print("you are a short male")
elif not is_male and is_tall:
    print("you are not male but short")
else:
    print("you are either not  male or not tall or both")
