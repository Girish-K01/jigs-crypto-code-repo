# **JIGS: A Modular Parallel Encryption and Authentication Pipeline for Secure Messaging**  

## **Overview**  
JIGS (jigsaw) is a **hybrid secure messaging architecture** designed to balance security and efficiency. It leverages:  
- **ECDH key exchanges** for forward secrecy  https://github.com/Girish-K01/jigs-crypto-code-repo/blob/main/README.md
- **Nonce-based AES-128 encryption** for data confidentiality  
- **Parallel processing** to improve performance  

Through experimental results, we observed a **96.67% performance improvement**, demonstrating that parallel encryption significantly enhances processing speed without compromising security.  

## **Features**  
- **Strong Security:** Uses modern cryptographic standards (ECDH, AES-128).  
- **Forward Secrecy:** Ensures past communications remain secure.  
- **Parallel Processing:** Optimized for speed with modular design.  

## **Installation & Usage**  
1. Clone the repository:  
   ```sh
   git clone https://github.com/your-username/jigs.git
   cd jigs
   ```
2. Install dependencies:  
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the program:**  
   ```sh
   python execute.py
   ```  
   This script will first launch the **server**, introduce a delay, and then start the **client**, eliminating the need for manual execution.  

### **Operating System Compatibility**  
- **Linux:** Fully supported. The program uses multiprocessing, which works as expected.  
- **Windows:** May encounter errors or lack support for multiprocessing.  
- **macOS:** Multiprocessing is generally supported, but behavior may vary based on Python implementation.  

### **Experimenting with Different File Sizes**  
- The `data_files` folder contains pre-generated files of various sizes, created using `generatexkb.py`.  
- Users can generate new files of any size by running:  
  ```sh
  python generatexkb.py
  ```  
  The generated file will be saved in the `data_files` directory.  

### **Changing the File to be Processed**  
To modify the input file, change **line 79** in the code:
   ```python
   with open("./data_files/onekb.txt") as file:
       message = file.read().encode("utf-8")
   ```  
Replace `onekb.txt` with the desired filename.  

## **Performance & Security**  
- **Speed Gain:** Parallel processing improves performance by **96.67%**.  
- **Security Analysis:** The architecture has been validated to resist key compromise and message tampering.  
- **Execution Timing:** The file `newcryptotimes.txt` contains execution times (5 runs) for sender and receiver across different file sizes, measured on **WSL Ubuntu 20.02 with an Intel i7 10th generation CPU**.  

## **License**  
This project is licensed under **[CC BY-NC 4.0](LICENSE)** (Attribution-NonCommercial 4.0 International).  

## **Contributing**  
Contributions are welcome! Please follow the [contributing guidelines](CONTRIBUTING.md).