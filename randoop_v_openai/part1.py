import os

def copy_randoop_to_txt(randoop_dir, output_file):
    """
    Reads all .java files from the given directory and writes their contents 
    into a single .txt file.
    
    Args:
        randoop_dir (str): Path to the directory containing .java files.
        output_file (str): Path to the output .txt file.
    """
    with open(output_file, "w", encoding="utf-8") as out_f:
        # Iterate through all files in the provided directory
        for root, _, files in os.walk(randoop_dir):
            for file in files:
                if file.endswith(".java"):
                    java_path = os.path.join(root, file)
                    try:
                        with open(java_path, "r", encoding="utf-8") as in_f:
                            content = in_f.read()
                            # Optionally add a header comment for each file
                            out_f.write(f"// File: {file}\n")
                            out_f.write(content + "\n\n")
                        print(f"Copied: {java_path}")
                    except Exception as e:
                        print(f"Error reading {java_path}: {e}")
    print(f"All .java files have been copied to {output_file}")

if __name__ == "__main__":
    # Hardcoded path to the folder containing Randoop-generated .java files
    randoop_dir = "/Users/svastik/Documents/Svastik/Courses/WINTER 2025/EECS 4313/project/Money-Maven/Money-Maven/src/randoop_tests"  # Replace this with your folder path

    # Create the output directory on the desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_dir = os.path.join(desktop_path, "randoop_vs_open_ai")
    os.makedirs(output_dir, exist_ok=True)

    # Set the output file path
    output_file = os.path.join(output_dir, "randoop_test_cases.txt")

    copy_randoop_to_txt(randoop_dir, output_file)
