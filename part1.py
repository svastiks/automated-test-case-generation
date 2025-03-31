# from openai import OpenAI
# client = OpenAI()

# completion = client.chat.completions.create(
#     model="gpt-4o",
#     messages=[
#         {
#             "role": "user",
#             "content": "Hey, help me analyze some test cases for the code I'm writing."
#         }
#     ]
# )

# print(completion.choices[0].message.content)

import os
import re

def extract_evosuite_test_cases(evosuite_dir, output_file):
    """
    Extracts test cases from EVOSuite-generated Java files and writes them to a .txt file.
    
    Args:
        evosuite_dir (str): Path to the directory containing EVOSuite-generated test files.
        output_file (str): Path to the output .txt file.
    """
    test_cases = []

    # Iterate through all Java files in the EVOSuite directory
    for root, _, files in os.walk(evosuite_dir):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    content = f.read()
                    # Extract test methods using regex
                    methods = re.findall(r"public void (test\w+)\(\) \{.*?\}", content, re.DOTALL)
                    for method in methods:
                        test_cases.append(method)

    # Write the extracted test cases to the output file
    with open(output_file, "w") as f:
        for test_case in test_cases:
            f.write(test_case + "\n")

    print(f"Extracted {len(test_cases)} test cases to {output_file}")


# Example usage
evosuite_dir = "path/to/evosuite/generated/tests"
output_file = "evosuite_test_cases.txt"
extract_evosuite_test_cases(evosuite_dir, output_file)
