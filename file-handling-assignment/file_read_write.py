# file_read_write.py

def modify_file(input_file, output_file):
    try:
        with open(input_file, "r") as f:
            content = f.readlines()

        # Example modification: Add line numbers
        modified_content = [f"{i+1}: {line}" for i, line in enumerate(content)]

        with open(output_file, "w") as f:
            f.writelines(modified_content)

        print(f"✅ File modified and saved as {output_file}")

    except FileNotFoundError:
        print("❌ Error: Input file not found.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")


# Run example
modify_file("input.txt", "output.txt")
