import os

def save_text(filename, text):
    try:
        with open(filename, 'w') as f:
            f.write(text)
        print(f"Text saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")

def load_text(filename):
    try:
        with open(filename, 'r') as f:
            text = f.read()
            return text
    except FileNotFoundError:
        print("File not found.")
        return ""
    except Exception as e:
        print(f"Error loading file: {e}")
        return ""

def main():
    filename = "my_notepad.txt"
    while True:
        print("\nOptions:")
        print("1. Write/Edit Text")
        print("2. Load Text")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            text = input("Enter your text: ")
            save_text(filename, text)
        elif choice == '2':
            text = load_text(filename)
            print("\nLoaded text:\n")
            print(text)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
