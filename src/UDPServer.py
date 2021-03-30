# -*- coding: utf-8 -*-
"""
@author: manuandru
"""

import socket
import config

ip = config.ip
port = config.port

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.bind((ip, port))

while True:
    byte = udp_socket.recv(1024)
    print(byte.decode())