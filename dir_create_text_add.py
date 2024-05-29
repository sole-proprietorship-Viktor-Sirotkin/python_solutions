from pathlib import Path

directory_path = Path("/home/vik/Projects/Python/python_solutions")
file_path = directory_path / "hello.txt"

file_path.parent.mkdir(parents=True, exist_ok=True)

with file_path.open("a") as file:
    file.write("hello world\n")

print(f"File {file_path} has been created or appended to.")

try:
    content = file_path.read_text()
    print(f"Content of {file_path}:\n{content}")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
