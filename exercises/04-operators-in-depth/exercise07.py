# Exercise 7: Leap Year Detector
# A year is a leap year if divisible by 4, and NOT by 100, UNLESS also by 400.

year = int(input("Enter a year: "))

is_leap = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

if is_leap:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
