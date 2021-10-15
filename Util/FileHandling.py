from os import path
import sys

def file_read_bytes(path):
    file = open(path, 'rb')
    byteData = file.read()
    file.close()
    return byteData

def file_write_bytes(path, bytes):
    file = open(path, 'wb')
    file.write(bytes)
    file.close()