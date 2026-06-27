import random
import time

TIME_LIMIT = 30


def generate_question():
    operator = random.choice(["+", "-", "*", "/"])

    if operator == "+":
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        answer = a + b

    elif operator == "-":
        a = random.randint(1, 100)
        b = random.randint(1, a)   # Ensures positive result
        answer = a - b

    elif operator == "*":
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        answer = a * b

    else:  # Division
        b = random.randint(1, 12)
        answer = random.randint(1, 12)
        a = b * answer             # Ensures integer division
        answer = a // b

    return a, b, operator, answer


def play_game():
    score = 0
    correct = 0
    wrong = 0
    total = 0

    print("=" * 40)
    print("      TIMED MATH CHALLENGE")
    print("=" * 40)
    print(f"You have {TIME_LIMIT} seconds.")
    print("Answer as many questions as possible!")
    input("\nPress Enter to Start...")

    start_time = time.time()

    while True:
        if time.time() - start_time >= TIME_LIMIT:
            break

        a, b, op, answer = generate_question()

        remaining = int(TIME_LIMIT - (time.time() - start_time))

        print(f"\nTime Left : {remaining} sec")
        print(f"Question {total + 1}")

        try:
            user = int(input(f"{a} {op} {b} = "))
        except ValueError:
            print("Invalid Input!")
            wrong += 1
            total += 1
            continue

        total += 1

        if user == answer:
            print("Correct!")
            score += 10
            correct += 1
        else:
            print(f"Wrong! Correct Answer: {answer}")
            wrong += 1


    print("\n" + "=" * 40)
    print("          TIME'S UP!")
    print("=" * 40)
    print(f"Questions Attempted : {total}")
    print(f"Correct Answers     : {correct}")
    print(f"Wrong Answers       : {wrong}")
    print(f"Final Score         : {score}")
    print("=" * 40)


while True:
    play_game()

    again = input("\nPlay Again? (y/n): ").lower()

    if again != "y":
        print("\nThanks for Playing!")
        break