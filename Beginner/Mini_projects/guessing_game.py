secret_keyword = "python programming"
my_guess = input("Enter your guess: ").lower()
max_guess_count = 5
guess_count = 1
is_max_guess_tried = False

while my_guess != secret_keyword and not(is_max_guess_tried) :
    if guess_count < max_guess_count:
        my_guess = input("Enter your guess: ").lower()
        guess_count += 1
    else:
        is_max_guess_tried = True

if is_max_guess_tried:
    print("Your guess limit is over. You loose!")
else:
    print("Correct guess. You win")



