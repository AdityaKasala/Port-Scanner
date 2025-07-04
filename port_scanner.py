# Importing socket lib for network programming and datetime lib for time & date stamps 
import socket 
from datetime import datetime

# input for jupyter notebook(compatibility and ease), if using any other then import sys and use sys.argv for more flexibility
target = input("Enter the IP address or hostname: ")

#try and exception for error handling 
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Error: Hostname could not be resolved. Please check the input")
    target_ip = None

# output pattern
if target_ip:
    print("=" *45)
    print(f"Scan Target: {target} ({target_ip})")
    print("Scanning started at: " + str(datetime.now()))
    print("=" * 45)
    try:
        for port in range(1, 1025):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port} is open.")
                s.close()
    except KeyboardInterrupt:
        print("\nScan interrupted by user")
    except socket.error:
        print("\nNetwork error occured")
else:
    print("Scan aborted due to invalid target.")
