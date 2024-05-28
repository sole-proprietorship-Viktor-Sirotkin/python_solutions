import os


def create_directory(directory_path):
    """
    Creates a new directory at the specified path.

    Args:
        directory_path (str): The path of the directory to be created.

    Raises:
        FileExistsError: If the directory already exists.
    """
    directory_path = os.path.expanduser(directory_path)
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        raise FileExistsError(f"The directory {directory_path} already exists.")
    os.makedirs(directory_path)


directory_path = "~/Projects/Python/python_solutions/my_first_directory/my_second_directory/my_third_directory"
try:
    create_directory(directory_path)
    print(f"Directory {directory_path} created successfully.")
except FileExistsError as e:
    print(e)
