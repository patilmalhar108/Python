# Harsh Quiz Guess (Python)
# Enter a list of numbers, judge chooses one, Harsh guesses.
# Prints a suitable message if guess is higher/lower/correct.

import random

def parse_numbers(s: str):
    # Accepts: "1 2 3", "1,2,3", "1, 2  3" etc.
    tokens = []
    cur = ""
    for ch in s:
        if ch.isdigit() or ch in "-.":
            cur += ch
        else:
            if cur:
                tokens.append(cur)
                cur = ""
    if cur:
        tokens.append(cur)

    nums = []
    for t in tokens:
        try:
            n = float(t)
            if n.is_integer():
                n = int(n)
            nums.append(n)
        except ValueError:
            pass

    # remove duplicates, keep order
    seen = set()
    unique = []
    for n in nums:
        if n not in seen:
            unique.append(n)
            seen.add(n)
    return unique

def main():
    print("Harsh Quiz Guess")
    print("Enter a list of numbers (comma or space separated). Example: 2, 7, 10, 15, 21")

    list_text = input("List: ").strip()
    numbers = parse_numbers(list_text)

    if not numbers:
        print("No valid numbers found. Please try again.")
        return

    print(f"\nYour list ({len(numbers)} numbers): {numbers}")

    choice = input("Judge chooses (type 'r' for random OR enter position 1..N): ").strip().lower()
    if choice == "r":
        chosen = random.choice(numbers)
    else:
        try:
            pos = int(choice)
            if pos < 1 or pos > len(numbers):
                print("Invalid position.")
                return
            chosen = numbers[pos - 1]
        except ValueError:
            print("Invalid input.")
            return

    # Guess
    guess_text = input("Harsh's guess: ").strip()
    try:
        guess = float(guess_text)
        if guess.is_integer():
            guess = int(guess)
    except ValueError:
        print("Invalid guess (not a number).")
        return

    # Compare and print suitable message
    if guess == chosen:
        print(f"Correct! Harsh wins. (guess={guess}, chosen={chosen})")
    elif guess > chosen:
        print(f"Too high! Your guess ({guess}) is higher than the original number ({chosen}).")
    else:
        print(f"Too low! Your guess ({guess}) is smaller than the original number ({chosen}).")

if __name__ == "__main__":
    main()