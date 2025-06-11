import os

name = input("What's your name? \n")
color = input("What's your favorite color? \n")

file_path = os.path.abspath("example.txt")
print(f"Saving file to: {file_path}")

with open(file_path, 'w') as file:
    file.write(f"{name} created this file.\n")
    file.write(f"Their favorite color is {color}.")