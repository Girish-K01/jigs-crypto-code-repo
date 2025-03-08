# **JIGS: A Modular Parallel Encryption and Authentication Pipeline for Secure Messaging**

## **Overview**  
JIGS (jigsaw) is a **hybrid secure messaging architecture** designed to balance **security and efficiency**. It integrates:  
- **ECDH key exchanges** for forward secrecy  
- **Nonce-based AES-128 encryption** for data confidentiality  
- **Parallel processing** to enhance speed and performance  

### **Performance Highlights**  
Through experimental results, we observed a **96.67% performance improvement**, demonstrating that parallel encryption significantly enhances processing speed while maintaining security.  

**Key Findings:**  
- **Non-parallelized version:**  
  - Sender: **51.21s processing time**, **5.51 KB/s throughput**  
  - Receiver: **641.39s processing time**, **0.74 KB/s throughput**  
- **Parallelized version:**  
  - Sender: **3.22s processing time**, **59.38 KB/s throughput**  
  - Receiver: **16.08s processing time**, **12.00 KB/s throughput**  
  
The results show that parallel processing drastically improves performance, especially for sending operations. However, due to a higher payload, the receiver remains slower than the sender.  

---

## **Features**  
- **Strong Security:** Uses modern cryptographic standards (ECDH, AES-128).  
- **Forward Secrecy:** Ensures past communications remain secure.  
- **Parallel Processing:** Optimized for speed with a modular design.  

---

## **Installation & Usage**  
### **1. Clone the Repository**  
```sh
git clone https://github.com/your-username/jigs.git
cd jigs
```

### **2. Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **3. Run the Program**  
```sh
python execute.py
```
- This script automatically starts the **server**, introduces a delay, and then launches the **client**.  

---

## **Recommended Execution Environment**  
For optimal performance, run the program in a **Linux distribution** such as **Ubuntu**. Windows users should use **WSL (Windows Subsystem for Linux)**, and macOS users should ensure Python’s multiprocessing behaves as expected.

### **Operating System Compatibility**  
- **Linux:** Fully supported. Multiprocessing works as expected.  
- **Windows (WSL):** Recommended for Windows users. Some features may not work on native Windows Python.  
- **macOS:** Multiprocessing is generally supported, but behavior may vary.  

---

## **Experimenting with Different File Sizes**  
- The `data_files` folder contains pre-generated files of various sizes, created using `generatexkb.py`.  
- Generate new files with:  
  ```sh
  python generatexkb.py
  ```  
  - The generated file is saved in the `data_files` directory.  

### **Changing the File to be Processed**  
Modify **line 79** in the code:
```python
with open("./data_files/onekb.txt") as file:
    message = file.read().encode("utf-8")
```
Replace `onekb.txt` with the desired filename.  

---

## **Docker Support**  
JIGS supports **Docker**, allowing users to run it without manual dependency installations or system configuration issues.

### **Benefits of Dockerization:**  
- **Portable:** Runs consistently across different environments.  
- **Dependency-Free:** Avoids compatibility issues.  
- **Efficient:** Simplifies execution and testing.  

### **1. Pulling and Running the Docker Container from Docker Hub**  
```sh
docker pull girishk4913/jigs:latest
```

Run the container:
```sh
docker run --rm girishk4913/jigs:latest
```
- The default input file is `./data_files/onekb.txt`.  

---

### **2. Running the Container with a Custom Input File**  
Users can pass an **environment variable (`INPUT_FILE`)** to use a different input file:
```sh
docker run --rm -e INPUT_FILE="/app/data_files/customfile.txt" girishk4913/jigs:latest
```
- Replace `customfile.txt` with the **actual filename** inside the container.  

---

### **3. Allocating Dedicated Resources (Memory, CPU, GPU)**  
#### **Example: Running with 2 CPUs and 4GB RAM**  
```sh
docker run --rm --memory=4g --cpus=2 -e INPUT_FILE="/app/data_files/customfile.txt" girishk4913/jigs:latest
```
---

### **4. Building and Running the Container Locally**  
If preferred, users can **build and run** the Docker container locally:
```sh
docker build -t my-jigs-app .
```
Run it:
```sh
docker run --rm my-jigs-app
```

Run it with a custom file:
```sh
docker run --rm -e INPUT_FILE="/app/data_files/customfile.txt" my-jigs-app
```

---

### **5. Using Local Files from Host Machine**  
To process a local file, mount it inside the container:
```sh
docker run --rm -v /path/to/localfile.txt:/app/data_files/customfile.txt -e INPUT_FILE="/app/data_files/customfile.txt" girishk4913/jigs:latest
```
- Replace `/path/to/localfile.txt` with the actual file path on your machine.  

---

## **Final Summary**  
| **Action** | **Command** |
|------------|------------|
| Pull the image | `docker pull girishk4913/jigs:latest` |
| Run default container | `docker run --rm girishk4913/jigs:latest` |
| Run with a custom file | `docker run --rm -e INPUT_FILE="/app/data_files/customfile.txt" girishk4913/jigs:latest` |
| Allocate memory & CPU | `docker run --rm --memory=4g --cpus=2 -e INPUT_FILE="/app/data_files/customfile.txt" girishk4913/jigs:latest` |
| Build locally | `docker build -t my-jigs-app .` |
| Run locally | `docker run --rm my-jigs-app` |
| Use local files | `docker run --rm -v /path/to/localfile.txt:/app/data_files/customfile.txt -e INPUT_FILE="/app/data_files/customfile.txt" girishk4913/jigs:latest` |

---

## **License**  
This project is licensed under **[CC BY-NC 4.0](LICENSE.md)** (Attribution-NonCommercial 4.0 International).