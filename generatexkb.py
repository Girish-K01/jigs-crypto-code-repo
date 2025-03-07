import os
import random
import string
import inflect

# Initialize inflect engine for number-to-word conversion
p = inflect.engine()

def generate_text(size_in_kb):
    size_in_bytes = size_in_kb * 1024  # Convert KB to bytes
    text = ''.join(random.choices(string.ascii_letters + string.digits, k=size_in_bytes))
    return text

def number_to_words(number):
    return p.number_to_words(number).replace(" ", "").replace("-", "")

# User-defined file size (in KB)
size_in_kb = int(input("Enter the file size in KB: "))  # Change this value as needed

# Convert size to words (e.g., 5 -> "five")
size_word = number_to_words(size_in_kb)

# Generate file content
text_data = generate_text(size_in_kb)

# Define the folder path
folder_path = "./data_files/"

# Ensure the folder exists
os.makedirs(folder_path, exist_ok=True)

# Define the full file path
file_path = os.path.join(folder_path, f"{size_word}kb.txt")

# Save it to the file
with open(file_path, 'w') as f:
    f.write(text_data)

print(f"File '{file_path}' generated successfully!")
