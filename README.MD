# PIN Brute-Force Guessing Script

This Python script attempts to brute-force a **3-digit PIN** by sending HTTP POST requests to a local server (`127.0.0.1:8888`). 
It systematically tries PINs from `000` to `999` until the correct one is found.

## Features
- Uses **Python's `socket` library** for network communication.
- Sends **HTTP POST** requests with PIN guesses.
- Implements **automatic formatting** for 3-digit PINs.
- Introduces a **1-second delay** between attempts to prevent server overload.
- Stops once the correct PIN is found.

## Solution Process

### **1. Establish Connection with the Server**
- The script creates a **TCP/IP socket** using Python's `socket` library.
- It **connects to the target server** running on `127.0.0.1:8888`.

### **2. Format the PIN & Construct the Request**
- The PIN is **formatted as a 3-digit string** (`001`, `002`, ..., `999`).
- An **HTTP POST request** is manually constructed:
  - Includes headers (`Content-Type`, `Content-Length`, etc.).
  - Encodes the PIN in **form-urlencoded format** (`magicNumber=PIN`).
  - Sends the request to `/verify`.

### **3. Send the PIN & Receive Response**
- The formatted request is sent via `socket.sendall()`.
- The server responds, and the script **extracts the reply**.

### **4. Analyze the Response**
- If `"Incorrect number"` is **not** in the response, the correct PIN has been found.
- The script **prints the correct PIN** and **stops execution**.

### **5. Introduce a Delay & Continue Guessing**
- If the PIN is **incorrect**, the script waits **1 second** before trying the next PIN.
- The process **repeats** for all PINs from `000` to `999`.

## Requirements
- Python 3.x
- A server running on **localhost (`127.0.0.1`)** listening on **port 8888**.

## Installation
1. Clone or download the script.
2. Ensure your server is running on **localhost (`127.0.0.1`)**.
3. Run the script using:
   ```bash
   python pin.py
