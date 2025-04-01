import os

def copy_java_to_txt(evosuite_dir, output_file):
    """
    Reads all .java files from the given directory and writes their contents 
    into a single .txt file.
    
    Args:
        evosuite_dir (str): Path to the directory containing .java files.
        output_file (str): Path to the output .txt file.
    """
    with open(output_file, "w", encoding="utf-8") as out_f:
        # Iterate through all files in the provided directory
        for root, _, files in os.walk(evosuite_dir):
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
    # Hardcoded path to the folder containing .java files
    evosuite_dir = "/Users/svastik/Documents/Svastik/Courses/WINTER 2025/EECS 4313/project/Money-Maven/Money-Maven/src/test/java/maven"  # Replace this with your folder path

    # Determine the desktop path and set the output file path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_file = os.path.join(desktop_path, "evo_suite_test_cases.txt")

    copy_java_to_txt(evosuite_dir, output_file)
