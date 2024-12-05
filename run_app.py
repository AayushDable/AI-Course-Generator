import subprocess

def run_streamlit():
    cmd = ["streamlit", "run", "app.py"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Error running Streamlit app:\n{stderr.decode('utf-8')}")
    else:
        print(f"Streamlit app exited successfully:\n{stdout.decode('utf-8')}")

if __name__ == "__main__":
    run_streamlit()
