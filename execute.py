import subprocess
import time

# Define the paths to your sender and receiver scripts
server_script = 'server.py'  # Server (receiver) script
client_script = 'client.py'    # Client (sender) script

# Run the server script (receiver) in a new process
server_process = subprocess.Popen(['python', server_script])

# Wait for the server to start up before running the client
time.sleep(2)  # Adjust the sleep time if needed

# Run the client script (sender) in a new process
client_process = subprocess.Popen(['python', client_script])

# Wait for both processes to complete
server_process.wait()
client_process.wait()
