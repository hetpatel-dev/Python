# Exercise 5: Countdown with while and break
# Count down from a number, allow early stop via "stop".

start = int(input("Start: "))
while start >= 0:
    reply = input(f"{start} (press Enter to continue, or type 'stop') ")
    if reply == "stop":
        print(f"Stopped at {start}")
        break
    else:
        start = start - 1
