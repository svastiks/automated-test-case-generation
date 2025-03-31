from openai import OpenAI
import os

def compare_test_cases(evosuite_file, openai_file, report_file):
    """
    Compares test cases from EVOSuite and OpenAI and generates a report.
    
    Args:
        evosuite_file (str): Path to the EVOSuite test cases file.
        openai_file (str): Path to the OpenAI test cases file.
        report_file (str): Path to the output report file.
    """
    # Initialize the OpenAI client
    client = OpenAI()

    # Read the test cases from both files
    with open(evosuite_file, "r") as f:
        evosuite_test_cases = f.read()

    with open(openai_file, "r") as f:
        openai_test_cases = f.read()

    # Define the input for the model
    input_text = f"""
    Compare the following two sets of test cases and generate a detailed report:
    
    EVOSuite Test Cases:
    {evosuite_test_cases}
    
    OpenAI Test Cases:
    {openai_test_cases}
    
    Report the differences, identify missing test cases in EVOSuite, and suggest improvements.
    """

    # Call the OpenAI API
    response = client.responses.create(
        model="gpt-4o",  # Use the appropriate model
        input=input_text
    )

    # Extract the report
    report = response.output_text.strip()

    # Write the report to the output file
    with open(report_file, "w") as f:
        f.write(report)

    print(f"Comparison report written to {report_file}")


# Example usage
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
evosuite_file = os.path.join(desktop_path, "evo_suite_test_cases.txt")  # EVOSuite test cases file
openai_file = os.path.join(desktop_path, "openai_test_cases.txt")  # OpenAI test cases file
report_file = os.path.join(desktop_path, "comparison_report.txt")  # Output report file

compare_test_cases(evosuite_file, openai_file, report_file)
