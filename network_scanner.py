#!/usr/bin/env python3
"""
Network Scanner Project
Students: [Philip, Edvin,]
Date: [Date]
"""

import sys
import socket


target = input("vilken sida vill du scanna?: ") # webbplatsen vi vill skanna.
range_start = int(input("Välj intervallets start tal: ")) # väljer första porten som ska skannas
range_end = int(input("välj intervallets slut tal: ")) # väljer sista porten som ska skannas
timeout = int(input("Hur länge tills timeout?(sec): "))# väljer hur länge den ska vänta på svar
open_ports = 0
socket.setdefaulttimeout(timeout) #sätte en timeout för varje port


with open("result.txt", "a", encoding="utf-8") as f:
    f.seek(0) ## Flyttar file pointern till början av filen
    f.truncate() ## Tar bort allt som ligger efter file pointerns position
    f.write(f"Target: {target} \nRange: {range_start} - {range_end}\nTimeout: {timeout}s\n\nResult:\n")
f.close()

print(f"\nPortScanner\nMål: {target}\nIntervall: {range_start}-{range_end}\nTimeout: {timeout}s\n")

try:
    for port in range(range_start,range_end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Skapar en ny socket, AF_INET och SOCK_STREAM är default
        result = s.connect_ex((target,port)) # Ansluter. Får tillbaks 0 ifall anslutning lyckades.

        if result == 0 and port != 80: #om resultatet är 0 så utför den koden
            open_ports += 1 #räknar öppna portar
            request = s.recv(1024) #hämtar banner
            print(f"Port {port}/{range_end}: ÖPPEN - {request}") #talar om ifall porten är öppen och ger en banner för den
            s.close()#stänger socketen
            with open("result.txt", "a", encoding="utf-8") as f: #öppnar result.txt med rätt inställningar
                f.write(f"Port {port}: OPEN, Protocol Service Name: {request}\n") #skriver i result.txt
            f.close()

        elif result == 0 and port == 80: #ifall porten är 80
            open_ports += 1 #räknar öppna portar
            print(f"Port {port}/{range_end}: ÖPPEN - HTTP") #talar om att port 80 använder HTTP
            with open("result.txt", "a", encoding="utf-8") as f: #skriver resultatet i result.txt
                f.write(f"Port {port}: OPEN, Protocol Service Name: HTTP\n")
            f.close()
        

        else:
            print(f"Port {port}/{range_end}: STÄNGD") #talar om att porten är stängd
            s.close()
            with open("result.txt", "a", encoding="utf=8") as f:
                f.write(f"Port {port}: ClOSED\n")
            f.close()
                
                
    print(f"\nSkanning slutförd.\n\n{open_ports} öppna portar.\nResultat sparat i result.txt\n") #talar om hur många öppna portar som fanns
    with open("result.txt", "a", encoding="utf-8") as f:
        f.write(f"\nOpen ports: {open_ports}")
    f.close()


except socket.error: # Om det skulle det ske en socket.error
    print("error")
    sys.exit() 


# Om man bara exikverar sitt program så kommer "__name__" vara = "__main__"
# Bestämmer om en fil ska köras direkt, om den är importerad eller ej.

if __name__ == "__main__":
    pass

