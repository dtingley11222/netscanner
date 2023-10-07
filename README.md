markdown
Copy code
# Network Scanner

Network Scanner is a Python script that uses Scapy to scan a specified IP range and discover devices on the network.

## Prerequisites

Before you run the script, make sure you have Python installed on your system. You will also need to install the required libraries. You can install them using pip:

```
pip install -r requirements.txt
```
For Windows users, you may need to install Npcap separately to enable packet capturing. You can download Npcap from npcap.org.

# Getting Started

Clone the repository:


```git clone https://github.com/dtingley11222/netscanner```

```cd network-scanner```

# Install dependencies:


```pip install -r requirements.txt```

# Usage
Run the script and enter the target IP address range when prompted.


```python network_scanner.py```


The script will scan the specified IP range and display the available devices on the network.

# Saving Output
The script allows you to save the scan results to a text file. After scanning, you will be prompted if you want to save the output to output.txt.

# Contributing
If you want to contribute to this project and make it better, your help is welcome. Open an issue or submit a pull request explaining the changes you'd like to make.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments
Thanks to the Scapy team for their powerful packet manipulation library.
