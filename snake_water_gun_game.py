
import random


def game_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"

    elif (user_choice == "s" and computer_choice == "w") or \
         (user_choice == "w" and computer_choice == "g") or \
         (user_choice == "g" and computer_choice == "s"):
        return "user"

    else:
        return "computer"


random_number = random.randint(1, 3)

if random_number == 1:
    computer_choice = "s"
elif random_number == 2:
    computer_choice = "w"
else:
    computer_choice = "g"


user_choice = input(
    "Enter your choice (snake(s), water(w), gun(g)): "
).lower()

if user_choice not in ["s", "w", "g"]:
    print("Invalid choice! Please enter s, w, or g.")

else:
    result = game_winner(user_choice, computer_choice)

    print(f"Computer chose: {computer_choice}")
    print(f"User chose: {user_choice}")

    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
    else:
        print("Computer wins!")

    print(f"Result: {result}")
