# error_handling_lab.py

def read_file_with_handling():
    filename = input("📂 Enter the filename to read: ")

    try:
        with open(filename, "r") as file:
            print("✅ File content:\n")
            print(file.read())
    except FileNotFoundError:
        print("❌ Error: File does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


# Run function
read_file_with_handling()
