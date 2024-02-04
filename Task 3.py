import sys
from pathlib import Path
from colorama import Fore, Style

def visualize_directory_structure(directory_path, indent=0):
    current_directory = Path(directory_path)

    if not current_directory.exists() or not current_directory.is_dir():
        print(f"{Fore.RED}Error: Directory '{directory_path}' not found.{Style.RESET_ALL}")
        return
    items = sorted(current_directory.iterdir())

    for item in items:
        print(" " * indent, end="")

        if item.is_dir():
            print(f"{Fore.BLUE}{item.name}/")
            visualize_directory_structure(item, indent + 2)  
        else:
            print(f"{Fore.GREEN}{item.name}")

    print(Style.RESET_ALL, end="")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        visualize_directory_structure(directory_path)