# Exercise 7: Caesar Cipher
# Ask user for a message and a shift value. Use ord() and chr() to shift each
# letter by the shift amount. Preserve case. Leave non-letters unchanged.

# code i wrote after uderstanding caesar cipher

def encrypt(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                c = chr((ord(char) - 65 + shift) % 26 + 65)
                result += c
            else:
                c = chr((ord(char) - 97 + shift) % 26 + 97)
                result += c
        else:
            result += char
    return result


def decrypt(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                c = chr((ord(char) - 65 - shift) % 26 + 65)
                result += c
            else:
                c = chr((ord(char) - 97 - shift) % 26 + 97)
                result += c
        else:
            result += char
    return result


message = input("Enter message: ").strip()
shift = int(input("Enter shift: ").strip())
encrypted = encrypt(message, shift)
print(f"Encrypted: {encrypted}")
decrypted = decrypt(encrypted, shift)
print(f"Decrypted: {decrypted}")


# below is for reference and understanding

# """
# Caesar Cipher Implementation
# ============================
# A simple substitution cipher where each letter is shifted by a fixed number
# of positions in the alphabet.

# How it works:
# - Each letter is replaced by another letter fixed number of positions away
# - Wraps around the alphabet (Z → A, z → a)
# - Non-alphabetic characters (numbers, symbols, spaces) remain unchanged
# - Decryption uses the same algorithm with opposite shift direction

# Example:
# - "HELLO" with shift 3 → "KHOOR"
# - 'H' (position 7) + 3 = 'K' (position 10)
# """

# # ASCII Constants for reference:
# # Uppercase letters: A=65, B=66, ..., Z=90 (range of 26)
# # Lowercase letters: a=97, b=98, ..., z=122 (range of 26)
# #
# # To convert to 0-25 range: subtract 65 (uppercase) or 97 (lowercase)
# # To convert back to ASCII: add 65 (uppercase) or 97 (lowercase)


# def encrypt(message, shift):
#     """
#     Encrypt a message using Caesar cipher.

#     Args:
#         message (str): The plaintext message to encrypt
#         shift (int): Number of positions to shift each letter (0-25)

#     Returns:
#         str: The encrypted ciphertext

#     Algorithm:
#         For each character:
#             1. Check if it's a letter (A-Z or a-z)
#             2. If yes, shift it by the specified amount
#             3. Wrap around if shift goes past 'Z' or 'z'
#             4. If not a letter, keep it unchanged

#     Example:
#         >>> encrypt("Hello, World!", 3)
#         'Khoor, Zruog!'
#     """
#     result = ""

#     for char in message:
#         if char.isalpha():
#             if char.isupper():
#                 # Uppercase: 'A'=65, convert to 0-25 range, shift, wrap, convert back
#                 # Formula: (char - 65 + shift) % 26 + 65
#                 c = chr((ord(char) - 65 + shift) % 26 + 65)
#                 result += c
#             else:
#                 # Lowercase: 'a'=97, convert to 0-25 range, shift, wrap, convert back
#                 # Formula: (char - 97 + shift) % 26 + 97
#                 c = chr((ord(char) - 97 + shift) % 26 + 97)
#                 result += c
#         else:
#             # Non-alphabetic character: keep as-is (spaces, punctuation, numbers)
#             result += char

#     return result


# def decrypt(message, shift):
#     """
#     Decrypt a message encrypted with Caesar cipher.

#     Args:
#         message (str): The ciphertext to decrypt
#         shift (int): The shift value used during encryption

#     Returns:
#         str: The decrypted plaintext

#     Algorithm:
#         Same as encryption but with opposite shift direction.
#         Uses subtraction instead of addition to reverse the shift.

#     Example:
#         >>> decrypt("Khoor, Zruog!", 3)
#         'Hello, World!'
#     """
#     result = ""

#     for char in message:
#         if char.isalpha():
#             if char.isupper():
#                 # Uppercase: reverse shift (subtract instead of add)
#                 # Formula: (char - 65 - shift) % 26 + 65
#                 c = chr((ord(char) - 65 - shift) % 26 + 65)
#                 result += c
#             else:
#                 # Lowercase: reverse shift (subtract instead of add)
#                 # Formula: (char - 97 - shift) % 26 + 97
#                 c = chr((ord(char) - 97 - shift) % 26 + 97)
#                 result += c
#         else:
#             # Non-alphabetic character: keep as-is
#             result += char

#     return result


# def main():
#     """
#     Main function to run the Caesar cipher program.

#     Prompts user for:
#         1. Message to encrypt
#         2. Shift value (0-25)

#     Outputs:
#         - Encrypted message
#         - Decrypted message (to verify correctness)
#     """
#     print("Caesar Cipher")
#     print("=" * 40)

#     # Get input from user
#     message = input("Enter message: ").strip()
#     shift = int(input("Enter shift (0-25): ").strip())

#     # Validate shift value
#     if not (0 <= shift <= 25):
#         print("Error: Shift must be between 0 and 25")
#         return

#     # Perform encryption and decryption
#     encrypted = encrypt(message, shift)
#     decrypted = decrypt(encrypted, shift)

#     # Display results
#     print("\nResults:")
#     print("-" * 40)
#     print(f"Original:  {message}")
#     print(f"Encrypted: {encrypted}")
#     print(f"Decrypted: {decrypted}")

#     # Verify correctness
#     if decrypted == message:
#         print("\n✓ Success! Decryption matches original message.")
#     else:
#         print("\n✗ Error! Decryption doesn't match original message.")


# # Run the program
# if __name__ == "__main__":
#     main()
