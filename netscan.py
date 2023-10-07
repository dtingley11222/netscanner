import ipaddress
from scapy.all import ARP, Ether, srp
import os

def clear_screen():
    # Clear the screen in IDLE by printing newlines
    print('\n' * 100)

def save_to_file(clients):
    with open("output.txt", "w") as file:
        file.write("Available devices on the network:\n")
        file.write("IP" + " " * 18 + "MAC\n")
        for client in clients:
            file.write("{:16}   {}\n".format(client['ip'], client['mac']))
        print("Output saved to 'output.txt'.")

while True:
    clear_screen()  # Clear the screen in IDLE
    # Get target IP address from user input and validate it
    while True:
        target_ip = input("Enter the target IP address (IPv4 or IPv6 format, with optional CIDR notation, e.g., 192.168.1.1/24). Type 'quit' to exit: ")

        if target_ip.lower() == 'quit':
            exit(0)  # Exit the program if the user types 'quit'
        try:
            network = ipaddress.ip_network(target_ip, strict=False)
            break  # Exit the loop if the input is a valid IP address or network
        except ValueError:
            print("Invalid IP address or network format. Please try again.")

    # Create ARP packet
    arp = ARP(pdst=str(network))

    # Ethernet broadcast packet created
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    clients = []

    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    print("Available devices on the network:")
    print("IP" + " " * 18 + "MAC")
    for client in clients:
        print("{:16}   {}".format(client['ip'], client['mac']))

    # Ask the user if they want to save the output to a file
    save_output = input("Do you want to save the output to 'output.txt'? (yes/no): ").lower()
    if save_output == 'yes':
        save_to_file(clients)

    # Ask the user if they want to run the program again
    run_again = input("Do you want to run the program again? (yes/no): ").lower()
    if run_again != 'yes':
        break
