# -*- coding: utf-8 -*-
"""
@author: manuandru
"""

import socket
import config

ip = config.ip
port = config.port

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

name = input('Insert name: ')

i = 0

while True:
    message = input('Insert message: ')
    udp_socket.sendto((f'{name}: {message}').encode(), (ip, port))
    