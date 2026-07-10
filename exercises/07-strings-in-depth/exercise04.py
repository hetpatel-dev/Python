# Exercise 4: CSV Parser
# Hardcode a CSV line: "Alice,25,Engineer,New York"
# Parse it with split(), then join it back with " | " as separator.

line = "Alice,25,Engineer,New York"
fields = line.split(",")
final = " | ".join(fields)

print(f"Original: {line}")
print(f"Parsed: {fields}")
print(f"Joined: {final}")
