# -*- coding: utf-8 -*-
"""
Created on Thu May  4 10:26:24 2023

@author: sridh
"""
import re
def generate_matrix(key):
    key = key.upper().replace("J", "I") 
    key = re.sub(r"[^A-Z]", "", key)  
    key += "ABCDEFGHIKLMNOPQRSTUVWXYZ" 
    matrix = [key[i:i+5] for i in range(0, 25, 5)]
    return matrix
def encrypt(message, matrix):
    message = message.upper().replace("J", "I") 
    message = re.sub(r"[^A-Z]", "", message)
    message = re.sub(r"(.)\1", r"\1X\1", message)
    message = message if len(message) % 2 == 0 else message + "Z"
    ciphertext = ""
    for i in range(0, len(message), 2):
        a, b = message[i], message[i+1]
        row1, col1 = divmod(matrix.index(a), 5)
        row2, col2 = divmod(matrix.index(b), 5)
        if row1 == row2:
            ciphertext += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1 == col2:
            ciphertext += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    return ciphertext
matrix = generate_matrix("MFHIJKUNOPQZVWXYELARGDSTBC")
message = "Must see you over Cadogan West. Coming at once."
ciphertext = encrypt(message, matrix)
print("Playfair matrix:")
for row in matrix:
    print(row)
print("\nPlaintext: ", message)
print("Ciphertext:", ciphertext)