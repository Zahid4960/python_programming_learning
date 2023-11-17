is_male = False
is_tall = False

if is_male and is_tall:
    print("You're a male with long height")
elif is_male and not(is_tall):
    print("You're a male with short height.")
elif not(is_male) and is_tall:
    print("You're a female with long height")
elif not(is_male) and not(is_tall):
    print("You're a female with short height")
else:
    print("Something went wrong!")