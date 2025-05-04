import subprocess

def run_test_scripts(script_names):
    for script in script_names:
        try:
            result = subprocess.run(['python', script], check=True, capture_output=True, text=True)
            print(f"Output of {script}:\n{result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while running {script}:\n{e.stderr}")

if __name__ == "__main__":
    phase1 = ['automation_followups.py'] 
    # test_scripts = ['login_test.py', 'another_test_script.py'] 
    run_test_scripts(phase1)
    input("Press Enter to exit...")
