from openai import OpenAI
import os

def compare_test_cases(randoop_file, openai_file, report_file):
    """
    Compares test cases from Randoop and OpenAI and generates a report in Markdown format.
    
    Args:
        randoop_file (str): Path to the Randoop test cases file.
        openai_file (str): Path to the OpenAI test cases file.
        report_file (str): Path to the output report file (.md).
    """
    # Initialize the OpenAI client
    client = OpenAI()

    # Read the test cases from both files
    with open(randoop_file, "r") as f:
        randoop_test_cases = f.read()

    with open(openai_file, "r") as f:
        openai_test_cases = f.read()

    # Define the input for the model
    input_text = f"""
    Compare the following two sets of test cases and generate a detailed report in Markdown format:
    
    Randoop Test Cases:
    {randoop_test_cases}
    
    OpenAI Test Cases:
    {openai_test_cases}
    
    Report the differences, identify missing test cases in Randoop, and suggest improvements.
    Make sure to use 3 code snippets for each approach (OpenAI and Randoop).
    Additionally, use a good amount of emojis to make the report more engaging.
    """

    # Call the OpenAI API
    response = client.responses.create(
        model="gpt-4o",  # Use the appropriate model
        input=input_text
    )

    # Extract the report
    report = response.output_text.strip()

    # Write the report to the output Markdown file
    with open(report_file, "w") as f:
        f.write(report)

    print(f"Comparison report written to {report_file}")


if __name__ == "__main__":
    # Create the output directory on the desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_dir = os.path.join(desktop_path, "randoop_vs_open_ai")
    os.makedirs(output_dir, exist_ok=True)

    # Set file paths
    randoop_file = os.path.join(output_dir, "randoop_test_cases.txt")
    openai_file = os.path.join(output_dir, "openai_test_cases.txt")
    report_file = os.path.join(output_dir, "comparison_report.md")

    compare_test_cases(randoop_file, openai_file, report_file)
