# Exercise 2: Multiplication Table
# Print an n×n multiplication table using nested for loops.

n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j:^4}", end=" ")
    print()
