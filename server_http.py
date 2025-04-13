import socket  # allows use of socket features
import time
"""
Author: Torin McDonald
Class: OSU CS370 Intro to Networks
Project: Programming Project 1 Sockets and HTTP
Part 3 - The world's simplest HTTP server

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
        internl/ppointers at
        https://www.internalpointers.com/post/making-http-requests-sockets-python
        retrieved on April 12, 2025
        Used to confirm how to use sockets for HTTP GET requests and for how to
        print the received data in a nicer format using the decode() funciton
        and to better explain the use of AF_INET.
    5) GeeksforGeeks' Socket Programming in Python at
        https://www.geeksforgeeks.org/socket-programming-python/
        retrievied on April 12, 2025. Used as further reference material
    6) Part 1 code
"""
HOST = "127.0.0.1"  # A standard loop back interface address (localhost)
PORT = 4253        # Post to listen on must be 1024 or higher

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            recv_data = conn.recv(1024)
            if not recv_data:
                break
            print("Received: ", recv_data.decode())
            data = "HTTP/1.1 200 OK\r\n"\
                "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
                "<html>Congratulations!  You've downloaded the first Wireshark lab file!</html>\r\n"
            print("Sending>>>>>>>>\n", data, "\n <<<<<<<<")
            conn.sendall(data.encode())
            conn.close()
            exit()
