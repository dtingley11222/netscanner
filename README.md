# netscanner

Network Scanner is a Python script that uses Scapy to scan a specified IP range and discover devices on the network.

## Prerequisites

Before you run the script, make sure you have Python installed on your system. You will also need to install the required libraries. You can install them using pip:

```bash
pip install -r requirements.txt
```
For Windows users, you may need to install Npcap separately to enable packet capturing. You can download Npcap from npcap.org.

Usage
Clone the repository:


```git clone https://github.com/yourusername/network-scanner.git
cd network-scanner```
Install dependencies:


```pip install -r requirements.txt```

Run the script:
```python network_scanner.py```

Enter the target IP address range when prompted.
Saving Output
The script allows you to save the scan results to a text file. After scanning, you will be prompted if you want to save the output to output.txt.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to the Scapy team for their powerful packet manipulation library.
Feel free to customize the README to include more details about your project, such as features, usage examples, or any other relevant information.
