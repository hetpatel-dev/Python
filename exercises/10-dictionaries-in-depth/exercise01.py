# Exercise 1: Basic CRUD — Phonebook
# Build a menu-driven phonebook using a dict.

phonebook = {}

while True:
    print("\nPhonebook Menu")
    print("=============")
    print("1. Add contact")
    print("2. Lookup contact")
    print("3. Delete contact")
    print("4. List all")
    print("5. Count entries")
    print("6. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        number = input("Phone: ")
        phonebook[name] = number
        print("Contact added.")

    elif choice == "2":
        name = input("Name: ")
        # Use .get() to safely look up the number
        number = phonebook.get(name)
        if number:
            print(f"{name}: {number}")
        else:
            print(f"{name}: Not found.")

    elif choice == "3":
        name = input("Name: ")
        if name in phonebook:
            del phonebook[name]
            print(f"{name} deleted.")
        else:
            print(f"{name}: Not found.")

    elif choice == "4":
        if phonebook:
            for name, number in phonebook.items():
                print(f"{name}: {number}")
        else:
            print("Phonebook is empty.")

    elif choice == "5":
        print(f"Total contacts: {len(phonebook)}")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-6.")
