import secrets
import string
from pathlib import Path

uppercase_letter = string.ascii_uppercase
lowercase_letter = string.ascii_lowercase
digits = "0123456789"
symbols = "~!@#$%^&*()_+-=[]{}\\|;:'\",./?"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letter
if lower:
    all += lowercase_letter
if nums:
    all += digits
if syms:
    all += symbols

length = 17
amount = 1

for x in range(amount):
    password = "".join(secrets.choice(all) for _ in range(length))

    print("========================================")
    print("GENERATED PASSWORD: ", password)
    print("========================================")
    choice = input("\n >> Import Password? [i]: ").lower()

    if choice == "i":
        file_path = Path.home() / "Downloads" / "py_generated_password.txt"

        with open(file_path, "a", encoding="utf-8") as file:
            file.write(password + "\n")

        print("----------------------------------------")
        print("GENERATED PASSWORD SAVED!")
        print(f"Location: {file_path}", )
        print("----------------------------------------")

    else:
       print("IMPORT FAILED: ")