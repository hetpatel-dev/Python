# Exercise 5: Bitwise Flag Reader
# Imagine a system where permissions are stored as a single integer,
# with each bit representing a permission:
#   1 = READ    (bit 0)
#   2 = WRITE   (bit 1)
#   4 = EXECUTE (bit 2)
#   8 = DELETE  (bit 3)

READ    = 1
WRITE   = 2
EXECUTE = 4
DELETE  = 8

def check_perms(p):
    print(f"\nPermissions: {p} (binary: {p:04b})")
    if p & READ:
        print("  READ enabled")
    if p & WRITE:
        print("  WRITE enabled")
    if p & EXECUTE:
        print("  EXECUTE enabled")
    if p & DELETE:
        print("  DELETE enabled")

# Example: permissions = 5  (binary: 0101 → READ + EXECUTE)
check_perms(5)

# permissions = 3  (binary: 0011 → WRITE + READ)
check_perms(3)

# permissions = 15  (binary: 1111 → all)
check_perms(15)

# permissions = 10  (binary: 1010 → DELETE + WRITE)
check_perms(10)

# BONUS: Use bitwise OR to combine READ + WRITE + DELETE
combined = READ | WRITE | DELETE
print(f"\nBONUS: READ | WRITE | DELETE = {combined}")
