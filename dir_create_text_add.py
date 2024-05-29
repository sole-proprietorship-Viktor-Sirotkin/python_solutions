# Define the file path
from pathlib import Path

# Define the directory path
directory_path = Path("/home/vik/Projects/Python/python_solutions")

file_path = directory_path / "hello.txt"

# Check if the file exists
if not file_path.is_file():
    # If the file does not exist, create it and write to it
    with open(file_path, "w") as file:
        file.write("hello world\n")
    print(
        f"File {file_path} has been created and 'hello world' has been written to it."
    )
else:
    # If the file exists, append to it
    with open(file_path, "a") as file:
        file.write("hello world\n")
    print(f"File {file_path} already exists. 'hello world' has been appended to it.")
