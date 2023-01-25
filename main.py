import random

print("Guessing Number Generator between 1 and 1,000")
num_set = random.randint(1, 1000)

counter = 0

while True:
    counter += 1
    num_in = int(input("Enter a number: "))
    if num_in == num_set:
        print("Congrats! You are a winner 🥳🥳 ")
        break
    elif num_in > num_set:
        print("Your number is too high")
        print()
        continue
    elif num_in < num_set:
        print("Your number is too low")
        print()
    elif num_in < 0:
        print("Your entered a negative number")
        exit()
print()
print("You guessed after %s tries " % counter)
