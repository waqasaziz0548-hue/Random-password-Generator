import random
import string

print("======Random Password Generator=======")

length = int(input("Enter Password Length: "))

characters = string.ascii_letters + string.digits

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:", password)
