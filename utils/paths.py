import os
import platform

def ask_for_path():
    user_home = os.path.expanduser('~')
    system = platform.system()

    if system == 'Windows':
        default_path = os.path.join(user_home, 'Desktop')
    elif system == 'Darwin':  # macOS
        default_path = os.path.join(user_home, 'Desktop')
    else:
        default_path = os.path.join(user_home, 'Desktop')

    path_to_store_models = input(f"Enter the path to store models (default: {default_path}): ").strip()

    if not path_to_store_models:
        return default_path

    if os.path.isdir(path_to_store_models):
        return path_to_store_models
    else:
        print(f"Invalid path entered. Using default path: {default_path}")
        return default_path

path = ask_for_path()
print("Using path:", path)
