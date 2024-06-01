
# # linux terminal
# dpkg -s send2trash &> /dev/null

# if [ $? -ne 0 ]; then
#     echo "send2trash is not installed. Installing now..."
#     sudo apt-get update
#     sudo apt-get install python3-send2trash
# else
#     echo "send2trash is already installed."
# fi

# python code
import importlib.util
import subprocess

package_name = 'send2trash'

spec = importlib.util.find_spec(package_name)
if spec is None:
    print(f"{package_name} is not installed. Installing now...")
    subprocess.check_call(['pipenv', 'install', package_name])
    print(f"{package_name} has been installed.")
else:
    print(f"{package_name} is already installed.")
