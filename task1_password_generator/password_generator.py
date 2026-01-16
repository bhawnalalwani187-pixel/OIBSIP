import random
import string

print("🔐 Random Password Generator")

length = int(input("Enter password length: "))

use_letters = input("Include letters? (y/n): ").lower()
use_numbers = input("Include numbers? (y/n): ").lower()
use_symbols = input("Include symbols? (y/n): ").lower()

characters = ""

if use_letters == "y":
    characters += string.ascii_letters   # a-z A-Z

if use_numbers == "y":
    characters += string.digits           # 0-9

if use_symbols == "y":
    characters += string.punctuation      # !@#$%^&*

if characters == "":
    print("❌ Please select at least one character type")
else:
    password = ""
    for i in range(length):
        password += random.choice(characters)

    print("✅ Generated Password:", password)
