# Exercise 3: Short-Circuit Detective
# Predict what each expression will evaluate to, then uncomment and run to check.
# For each one, write a comment explaining WHY Python stopped where it did.

def a():
    print("  -> a() called")
    return False

def b():
    print("  -> b() called")
    return True

def c():
    print("  -> c() called")
    return False

# 1.
print("--- 1. b() or c() ---")
result = b() or c()
print(f"Result: {result}")
# b() returns True, or short-circuits — c() never runs.

# 2.
print("--- 2. a() and b() or c() ---")
result = a() and b() or c()
print(f"Result: {result}")

# 3.
print("--- 3. a() or b() and c() ---")
result = a() or b() and c()
print(f"Result: {result}")

# 4.
print("--- 4. (a() or b()) and c() ---")
result = (a() or b()) and c()
print(f"Result: {result}")

# 5.
print("--- 5. Values only ---")
print(f"0 and 'hello'  = {0 and 'hello'}")     # 0 — 0 is falsy, short-circuits
print(f"3 or 'hello'   = {3 or 'hello'}")      # 3 — 3 is truthy, short-circuits
print(f"0 or 'hello'   = {0 or 'hello'}")      # hello — 0 is falsy, evaluates 'hello'
print(f"'' or 42       = {'' or 42}")          # 42 — '' is falsy
print(f"'' and 42      = '{'' and 42}'")       # '' — '' is falsy, short-circuits
print(f"3 and 0 and 5  = {3 and 0 and 5}")     # 0 — 3 is truthy, 0 is falsy, short-circuits
print(f"3 and 4 and 5  = {3 and 4 and 5}")     # 5 — all truthy, returns last value
