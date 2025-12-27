#!/usr/bin/env python3
"""
Network Scanner Project
Students: [Your names here]
Date: [Date]
"""

import socket
import sys

# Detta är en TCP server. Det är bara va de är.
# TCP server kan exempelvis vara en webbserver, då den opererar på TCP protokollet.

# Socket är en process inuti datorn som kan ta emot anslutningen.
# Vi väljer vilken typ av anslutning som kommer komma in (ipv4, SOCK.STREAM)
# Vilken port och adress vi vill binda det till
# Sen lyssnar vi på adressen 
# Vi tar emot responsen


##### TCP Protokoll delen ###
def start_server(host="0.0.0.0", port=8080):
    #AF_INET = skapar en TCP/IP socket ipv4 familj, SOCK_STREAM = strömmande socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # För att undvika "Adress already in use" Error
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Man behöver binda socket till en host och en port
    server_socket.bind((host, port))
    
    # Lyssnar på addressen och porten som är definerade ovan
    server_socket.listen()


##### Protokollet vi har definierat ####
    # Vi vill kontinuerligt lyssna, därför börjar vi med en While loop
    
    try:
        while True:
            print("Waiting for a connection ...")
            client_socket, client_address = server_socket.accept()

            # Ta emot data. Vi behöver definera storleken på en buffert (1024 bytes)
            try:
                print(f"Connection from {client_address}")
                data = client_socket.recv(1024)

                # Kollar om vi fått någon data. 
                # Denna data är "raw". Vi vill decoda vår data
                # För att klienten ska kunna skicka tillbaks ett svar behöver vi berätta vilken
                #   socket den ska använda
                if data: 
                    response = data.decode("utf-8")
                    if response == "ping\n":
                        client_socket.sendall("pong\n.encode(utf-8)")

            finally:
                client_socket.close()
                
    # Om något går fel, skriv ett felmeddelande och socket.close
    except Exception:
        print("Something went wrong!")

    # Ifall man gör t.ex "ctrl + c", blir det inte en stor error, utan "goodbye"
    #   istället. Det ser bara lite finare ut när man stoppar koden och får ett
    #   meddelande istället för massor av error meddelanden.
    except KeyboardInterrupt:
        print("goodbye!")


    # går annars allt som det ska så är det också socket.close
    finally:
        server_socket.close()




if __name__ == "__main__":
    start_server()