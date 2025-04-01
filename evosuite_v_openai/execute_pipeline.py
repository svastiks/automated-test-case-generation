import subprocess

def run_script(script_name):
    try:
        print(f"Running {script_name}...")
        result = subprocess.run(["python3", script_name], check=True, text=True, capture_output=True)
        print(f"Output from {script_name}:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error while running {script_name}:\n{e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred while running {script_name}: {e}")

def main():
    scripts = ["evosuite_v_openai/part1.py", "evosuite_v_openai/part2.py", "evosuite_v_openai/part3.py", "evosuite_v_openai/part4.py"]
    for script in scripts:
        run_script(script)

if __name__ == "__main__":
    main()
