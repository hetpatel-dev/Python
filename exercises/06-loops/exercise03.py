# Exercise 3: Prime Number Finder
# Use for/else to find all primes between 2 and n.

# prime number is number > 1 which can only evenly devided by 1 and itself.

n = int(input("Enter n: "))
primes = []

for m in range(2, n + 1):
    for x in range(2, m):
        if m % x == 0:
            print(f"{m} equals {x} * {m//x}")
            break
    else:
        # no factor found — m is prime
        print(f"{m} is a prime number")
        primes.append(m)

print(primes)
