import os
from datetime import datetime

def create_diary_entry(file_path, add_timestamp=False):
    try:
        entry = input("Write your diary entry: \n")
        if add_timestamp:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            entry = f"[{timestamp}]\n{entry}"

        with open(file_path, 'a') as file:
            file.write(entry + "\n\n")
        print("Entry saved successfully!")
    except PermissionError:
        print("Permission denied. Unable to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_previous_entries(file_path):
    try:
        if not os.path.exists(file_path):
            print("No diary entries found.")
            return

        with open(file_path, 'r') as file:
            entries = file.read()
        if entries.strip():
            print("\nPrevious Entries:\n")
            print(entries)
        else:
            print("No diary entries found.")
    except PermissionError:
        print("Permission denied. Unable to read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_path = "diary.txt"
    while True:
        print("\n--- Personal Diary ---")
        print("1. Create a new entry")
        print("2. View previous entries")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_timestamp = input("Add timestamp to entry? (yes/no): ").strip().lower() == "yes"
            create_diary_entry(file_path, add_timestamp)
        elif choice == "2":
            view_previous_entries(file_path)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
