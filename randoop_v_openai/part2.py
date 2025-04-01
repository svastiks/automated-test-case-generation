from openai import OpenAI
import os

def generate_test_cases_with_openai(java_class_file, output_file):
    """
    Generates test cases for a Java class using OpenAI API and writes them to a .txt file.
    
    Args:
        java_class_file (str): Path to the file containing the Java class content.
        output_file (str): Path to the output .txt file.
    """
    # Initialize the OpenAI client
    client = OpenAI()

    # Read the Java class content from the file
    with open(java_class_file, "r") as f:
        java_class_content = f.read()

    # Define the input for the model
    input_text = f"""
    You are a software testing expert. Generate JUnit test cases for the following Java class:
    
    {java_class_content}
    """

    # Call the OpenAI API
    response = client.responses.create(
        model="gpt-4o",  # Use the appropriate model
        input=input_text
    )

    # Extract the generated test cases
    test_cases = response.output_text.strip()

    # Write the test cases to the output file
    with open(output_file, "w") as f:
        f.write(test_cases)

    print(f"Generated test cases written to {output_file}")

if __name__ == "__main__":
    # Hardcoded path to the Java class file
    java_class_file = "/Users/svastik/Documents/Svastik/Courses/WINTER 2025/EECS 4313/project/Money-Maven/Money-Maven/src/main/java/maven/Money.java"  # Replace this with the actual path to your Java class file

    # Create the output directory on the desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_dir = os.path.join(desktop_path, "randoop_vs_open_ai")
    os.makedirs(output_dir, exist_ok=True)

    # Set the output file path
    output_file = os.path.join(output_dir, "openai_test_cases.txt")

    generate_test_cases_with_openai(java_class_file, output_file)