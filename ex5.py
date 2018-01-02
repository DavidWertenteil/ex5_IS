__author__ = 'ronza'
import socket as sck

import time

# #create an INET, STREAMing socket
# socket = sck.socket(
#     sck.AF_INET, sck.SOCK_STREAM)
# #now connect to the web server on port 80
# # - the normal http port
# socket.connect(("127.0.0.1", 1234))

string = "Bad password!"
test = ['0'] * 8
msg = ''
max_time = 1

while string == "Bad password!":
    s = ''
    a=s.join(test)
    socket = sck.socket(
    sck.AF_INET, sck.SOCK_STREAM)
    socket.connect(("127.0.0.1", 1234))
    socket.recv(1024)
    s_t = time.time()
    socket.send(a)
    strings = socket.recv(1024)
    e_t = time.time()

    if test[len(msg)] == '0':
        max_time = abs(s_t - e_t)
    print(max_time,"               " ,s_t - e_t)
    if max_time > abs(s_t - e_t):
        msg += test[len(msg)]
        print(test)
    else:
        test[len(msg)] = chr(ord(test[len(msg)]) + 1)
    socket.close()

print(strings)