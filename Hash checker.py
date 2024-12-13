import os
import hashlib
import json

HASH_STORE_FILE = "file_hashes.json"

def load_hashes():
    """Load existing hashes from the store file."""
    if os.path.exists(HASH_STORE_FILE):
        with open(HASH_STORE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    """Save updated hashes to the store file."""
    with open(HASH_STORE_FILE, "w") as f:
        json.dump(hashes, f, indent=4)

def calculate_hash(file_path):
    """Calculate the hash of a file."""
    hash_algo = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_algo.update(chunk)
        return hash_algo.hexdigest()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def process_file(file_path, hashes):
    """Process a single file: check if it is new, changed, or unchanged."""
    new_hash = calculate_hash(file_path)
    if new_hash is None:
        return

    if file_path in hashes:
        if hashes[file_path] == new_hash:
            print(f"UNCHANGED: {file_path}")
        else:
            print(f"CHANGED: {file_path}")
    else:
        print(f"NEW FILE: {file_path}")

    # Update the hash record
    hashes[file_path] = new_hash

def process_folder(folder_path, hashes):
    """Process all files in a folder recursively."""
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            process_file(file_path, hashes)

def main():
    print("Select an option:")
    print("1. Process a single file")
    print("2. Process all files in a folder")
    print("3.exit")

    option = input("Enter your choice (1/2/3): ").strip()
    hashes = load_hashes()

    while option != "3":
        if option == "1":
            file_path = input("Enter the full path to the file: ").strip()
            if os.path.isfile(file_path):
                process_file(file_path, hashes)
            else:
                print("Invalid file path.")
        elif option == "2":
            folder_path = input("Enter the full path to the folder: ").strip()
            if os.path.isdir(folder_path):
                process_folder(folder_path, hashes)
            else:
                print("Invalid folder path.")
        else:
            print("Invalid option.")

        print("\nSelect an option:")
        print("1. Process a single file")
        print("2. Process all files in a folder")
        print("3.exit")
        option = input("Enter your choice (1/2/3): ").strip()

    save_hashes(hashes)

if __name__ == "__main__":
    main()
