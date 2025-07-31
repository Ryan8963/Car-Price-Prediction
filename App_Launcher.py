import subprocess
import time
import webbrowser

process = subprocess.Popen(["streamlit", "run", "app.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

time.sleep(3)

url = "http://localhost:8501"

print(f"Streamlit app is running at {url}")

webbrowser.open(url)
