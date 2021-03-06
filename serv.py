import os
import socket
import sys


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 2222))
server_socket.listen(10)

while True:
    conn, addr = s.accept()
    child_pid = os.fork()
    if child_pid == 0:
        request = conn.recv(1024)
        conn.send(request.upper())
        print '(child {}) {} : {}'.format(conn.getpeername(), request)
        conn.close()
        sys.exit()
    else:
        conn.close()

addr.close()
