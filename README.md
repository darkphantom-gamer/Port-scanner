# Port Scanner Tool  

> **WARNING:** This tool is intended for educational purposes only. I am not responsible for any misuse, unauthorized activities, or damages caused by this tool. Use it responsibly and only on networks you own or have explicit permission to scan.  

---

## 🛠️ Features  

- Fast and efficient port scanning  
- Detects open ports and services  
- Customizable scan range  
- Easy-to-use interface  

---

## 🚀 Getting Started  

### Prerequisites  

Ensure you have the following installed:  
- Python 3.x  
- Required Python libraries (flask)

### Installation For Linux (Windows not tested)

1. Clone the repository:

       git clone https://github.com/yourusername/port-scanner.git
       cd port-scanner
   
2. Install dependencies:

         pip install flask
         sudo apt install nmap
         sudo apt install python3-venv
3. Create a virtual enviroment
```
    python3 -m venv myenv
```
4. active the enviroment
```
    source myenv/bin/activate
   ```
6. launch it
```
    python3 scanner.py
```
7. Open Browser and go to:
  ```
   localhost:127.0.0.1:1000
```
OR 
````
      127.0.0.1:1000
````
OR
   ````
    <your private ip>:1000
  ````
![proof](https://github.com/darkphantom-gamer/Port-scanner/blob/a6cf5fb7c33c27bdef97e45f5bab714375fa0d96/scan1.png)
![proof](https://github.com/darkphantom-gamer/Port-scanner/blob/ebe30a7c9392d8cf7c68685c8244f6844f6e4edc/scan2.png)
8. You can change the Dockerfile and Docker-compose.yml if ur an expert :)

🖥️ Usage
Run the port scanner with:

         python port_scanner.py --target <IP/Domain> --ports <Port Range>
Example:
```
python port_scanner.py --target 192.168.1.1 --ports 1-1024
```
📂 Project Structure
```
port-scanner/
├── port_scanner.py    # Main script
├── Dockerfile   # Dockerfile
├── README.md          # Documentation
└── LICENSE            # License details
```
⚙️ Arguments
Argument	Description	Example
--target	Target IP address or domain	192.168.1.1
--ports	Port range to scan	1-65535
🧑‍💻 Contribution
Contributions are welcome!

Fork the repository
Create your feature branch: git checkout -b feature/YourFeature
Commit your changes: git commit -m 'Add some feature'
Push to the branch: git push origin feature/YourFeature
Open a pull request
📜 License
This project is licensed under the MIT License.

🛡️ Disclaimer
This tool is designed for ethical purposes. Ensure you have explicit permission before using it on any network. Unauthorized scanning can result in severe consequences.
#Have a Great Day Mate :3
