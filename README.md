# **JIGS: A Modular Parallel Encryption and Authentication Pipeline for Secure Messaging**  

## **Overview**  
JIGS (Jointly Integrated Guard System) is a **hybrid secure messaging architecture** designed to balance security and efficiency. It leverages:  
- **ECDH key exchanges** for forward secrecy  
- **Nonce-based AES-128 encryption** for data confidentiality  
- **Parallel processing** to improve performance  

Through experimental results, we observed a **96.67% performance improvement**, demonstrating that parallel encryption significantly enhances processing speed without compromising security.  

## **Features**  
- **Strong Security:** Uses modern cryptographic standards (ECDH, AES-128).  
- **Forward Secrecy:** Ensures past communications remain secure.  
- **Parallel Processing:** Optimized for speed with modular design.  
- **Parallel processing** to improve performance  

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
3. Run the server and client:  
   ```sh
   python server.py
   python client.py
   ```

## **Performance & Security**  
- **Speed Gain:** Parallel processing improves performance by **96.67%**.  
- **Security Analysis:** The architecture has been validated to resist key compromise and message tampering.  

## **License**  
This project is licensed under **[CC BY-NC 4.0](LICENSE)** (Attribution-NonCommercial 4.0 International).  

## **Contributing**  
Contributions are welcome! Please follow the [contributing guidelines](CONTRIBUTING.md).
