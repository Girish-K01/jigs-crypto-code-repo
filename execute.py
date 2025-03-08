import subprocess
import time
import os

# Define the paths to your sender and receiver scripts
server_script = 'server.py'  # Server (receiver) script
client_script = 'client.py'  # Client (sender) script

# Get the input file path from the environment variable (default to onekb.txt)
input_file = os.getenv("INPUT_FILE", "./data_files/onekb.txt")

# Run the server script (receiver) in a new process
server_process = subprocess.Popen(['python3', server_script])

# Wait for the server to start up before running the client
time.sleep(2)  # Adjust the sleep time if needed

# Run the client script (sender) with the input file
client_process = subprocess.Popen(['python3', client_script, input_file])

# Wait for both processes to complete
server_process.wait()
client_process.wait()
