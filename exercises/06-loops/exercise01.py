# Exercise 1: Sum and Average
# Ask the user for numbers one at a time. Keep asking until they enter "done". Then print the sum, count, and average of all numbers entered. Skip non-numeric input with a warning (use try/except).

numbers = []
while True:
    try:
        reply = input("Enter a number (or 'done'): ")
        if reply == "done":
            if len(numbers):
                print(
                    f"sum: {sum(numbers):<4} count: {len(numbers):<4} average: {sum(numbers) / len(numbers):<4.2f}")
                break
            else:
                break
        else:
            numbers.append(int(reply))
    except ValueError:
        print("Warning: not a valid number!")
