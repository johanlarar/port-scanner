#!/usr/bin/env python3
"""
Network Scanner Project
Students: [Your names here]
Date: [Date]
"""

import socket
import sys


target = "scanme.nmap.org" # webbplatsen vi vill skanna.

try:
    for port in range(80,90):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Skapar en ny socket, AF_INET och SOCK_STREAM är default
        socket.setdefaulttimeout(1) # Gör att default timeout sätts till 1 sekund.

        result = s.connect_ex((target,port)) # Ansluter. Får tillbaks 0 ifall anslutning lyckades.

        if result == 0: # Ger resultatet av anslutningen 0?
            print(f"port {port} is open") # Om anslutningen ger 0, är porten öppen.
            s.close() # Man bör tydligen stänga efter sig. Egentligen ska man tydligen använda shutdown med, men i praktik gör folk inte det.

        else:
            print(f"port {port} is closed") # Annars är den stängd.
            s.close()

except socket.error: # Om det skulle det ske en socket.error
    print("error")
    sys.exit()


# Om man bara exikverar sitt program så kommer "__name__" vara = "__main__"
# Bestämmer om en fil ska köras direkt, om den är importerad eller ej.

if __name__ == "__main__":
    pass

