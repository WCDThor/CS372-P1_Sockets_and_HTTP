import socket  # allows use of socket features
"""
Author: Torin McDonald
Class: OSU CS370 Intro to Networks
Project: Programming Project 1 Sockets and HTTP
Part 1 - Using a socket to GET a file
"""

# Code used toc reate sockets based on CS361 assignment 4 code which is
# based on code found at https://realpython.com/python-sockets/

"""
Sources:
    1) I used code from my CS361 Assignment 4, which had code copied from,
        adopted from, and based on source 2. Used for everything but how to
        decode the response and how to turn HOST into something more usable
    2) Real Python's Socket Programming in Python (Guide) from
        https://realpython.com/python-sockets/#echo-client  Re-retrieved on
        April 12, 2025. See use in Source 1.
    3) Python Software Foundation's documentation at
        https://docs.python.org/3/library/socket.html retrieved on
        April 12, 2025.
        Used for the socket.gethostbyname(hostname) function to
    4) Making HTTP requests with sockets in Python (Triangles) from
        internal/pointers at
        https://www.internalpointers.com/post/making-http-requests-sockets-python
        retrieved on April 12, 2025
        Used to confirm how to use sockets for HTTP GET requests and for how to
        print the received data in a nicer format using the decode() function
        and to better explain the use of AF_INET.
    5) GeeksforGeeks' Socket Programming in Python at
        https://www.geeksforgeeks.org/socket-programming-python/
        retrieved on April 12, 2025. Used as further reference material
"""

HOST = "gaia.cs.umass.edu"  # Server's hostname
# socket.gethostbyname() from Sources 3 and 4
hostIp = socket.gethostbyname(HOST)
PORT = 80     # Usually HTTP runs on port 80


message = "GET /wireshark-labs/INTRO-wireshark-file1.html \
HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"
message_bytes = message.encode('utf-8')
# AF_INET the socket family. AF_INET is used to indicate we are using internet
# protocol IPV4
# Using sock_stream for TCP which is what HTTP uses
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((hostIp, PORT))
    s.send(message_bytes)
    data = s.recv(1024)  # size of buffer for received data

print("Request: ", message)
print("Received: ", data.decode())  # .decode() from Source 4.
