#!/usr/bin/env python3
"""
Network Scanner Project
Students: [Your names here]
Date: [Date]
"""

import socket
import sys

def start_client(host="0.0.0.0", port=8080):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1) # avslutar med exit code 1
    finally:
        pass



if __name__ == 