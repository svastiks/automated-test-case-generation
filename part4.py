from openai import OpenAI
import os
from fpdf import FPDF

def generate_improved_test_cases_and_report(evosuite_file, openai_file, report_file, output_java_file, output_report_pdf):
    """
    Generates improved test cases based on the comparison report and the two sets of test cases,
    and generates a final report explaining the improvements in PDF format.
    
    Args:
        evosuite_file (str): Path to the EVOSuite test cases file.
        openai_file (str): Path to the OpenAI test cases file.
        report_file (str): Path to the comparison report file.
        output_java_file (str): Path to the output .java file for improved test cases.
        output_report_pdf (str): Path to the output .pdf file for the final report.
    """
    # Initialize the OpenAI client
    client = OpenAI()

    # Read the EVOSuite test cases
    with open(evosuite_file, "r") as f:
        evosuite_test_cases = f.read()

    # Read the OpenAI test cases
    with open(openai_file, "r") as f:
        openai_test_cases = f.read()

    # Read the comparison report
    with open(report_file, "r") as f:
        comparison_report = f.read()

    # Define the input for generating improved test cases
    input_text_for_test_cases = f"""
    You are a software testing expert. Based on the following inputs, generate an improved set of JUnit test cases:
    
    EVOSuite Test Cases:
    {evosuite_test_cases}
    
    OpenAI Test Cases:
    {openai_test_cases}
    
    Comparison Report:
    {comparison_report}
    
    Combine the strengths of both sets of test cases, address any missing areas mentioned in the report, 
    and generate a final set of JUnit test cases in proper Java syntax.
    """

    # Call the OpenAI API to generate improved test cases
    response_test_cases = client.responses.create(
        model="gpt-4o",  # Use the appropriate model
        input=input_text_for_test_cases
    )

    # Extract the improved test cases
    improved_test_cases = response_test_cases.output_text.strip()

    # Write the improved test cases to the output .java file
    with open(output_java_file, "w") as f:
        f.write(improved_test_cases)

    print(f"Improved test cases written to {output_java_file}")

    # Define the input for generating the final report
    input_text_for_report = f"""
    You are a software testing expert. Based on the following inputs, generate a detailed report explaining:
    1. Why the new and final test cases are better.
    2. Which features were picked from the EVOSuite test cases and the OpenAI test cases.
    3. How the missing areas mentioned in the comparison report were addressed.
    
    EVOSuite Test Cases:
    {evosuite_test_cases}
    
    OpenAI Test Cases:
    {openai_test_cases}
    
    Comparison Report:
    {comparison_report}
    
    Improved Test Cases:
    {improved_test_cases}
    """

    # Call the OpenAI API to generate the final report
    response_report = client.responses.create(
        model="gpt-4o",  # Use the appropriate model
        input=input_text_for_report
    )

    # Extract the final report
    final_report = response_report.output_text.strip()

    # Write the final report to a PDF file
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add the report content to the PDF
    pdf.multi_cell(0, 10, final_report)

    # Save the PDF
    pdf.output(output_report_pdf)

    print(f"Final report written to {output_report_pdf}")


# Example usage
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
evosuite_file = os.path.join(desktop_path, "evo_suite_test_cases.txt")  # EVOSuite test cases file
openai_file = os.path.join(desktop_path, "openai_test_cases.txt")  # OpenAI test cases file
report_file = os.path.join(desktop_path, "comparison_report.txt")  # Comparison report file
output_java_file = os.path.join(desktop_path, "ImprovedTestCases.java")  # Output .java file
output_report_pdf = os.path.join(desktop_path, "FinalReport.pdf")  # Output .pdf file for the final report

generate_improved_test_cases_and_report(evosuite_file, openai_file, report_file, output_java_file, output_report_pdf)
