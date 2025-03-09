from random import randint

while True:
    num = randint(1, 100)
    attempt = 10

    while attempt > 0:
        inputNum = int(input("Enter a number: "))

        if inputNum < num:
            print("Too low")
        elif inputNum > num:
            print("Too high")
        else:
            print("You guessed it right!")
            break

        attempt -= 1

        if attempt == 0:
            print("You lost. Want to play again?")
            reply = input("Yes or No? ").strip().lower()
            if reply not in ("y", "yes", "ok"):
                print("Thanks for playing!")
                exit()
