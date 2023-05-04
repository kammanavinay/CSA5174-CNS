# -*- coding: utf-8 -*-
"""
Created on Thu May  4 10:20:13 2023

@author: sridh
"""
key = "PT109"
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
ciphertext = "KXJEY UREBE ZWEHE WRYTU HEYFS KREHE GOYFI WTTTU OLKSY CAJPO BOTEI ZONTX BYBNT GONEY CUZWR GDSON SXBOU YWRHE BAAHY USEDQ"

table = [[0 for j in range(5)] for i in range(5)]
key = key.replace("J", "I")
key += alphabet
for i in range(25):
    row = i // 5
    col = i % 5
    table[row][col] = key[i]
def find_position(letter):
    row = 0
    col = 0
    for i in range(5):
        for j in range(5):
            if table[i][j] == letter:
                row = i
                col = j
    return row, col
def encrypt_bigram(bigram):
    row1, col1 = find_position(bigram[0])
    row2, col2 = find_position(bigram[1])
    if row1 == row2:
        encrypted_bigram = table[row1][(col1 + 1) % 5] + table[row2][(col2 + 1) % 5]
    elif col1 == col2:
        encrypted_bigram = table[(row1 + 1) % 5][col1] + table[(row2 + 1) % 5][col2]
    else:
        encrypted_bigram = table[row1][col2] + table[row2][col1]
    return encrypted_bigram
def decrypt_bigram(bigram):
    row1, col1 = find_position(bigram[0])
    row2, col2 = find_position(bigram[1])
    if row1 == row2:
        decrypted_bigram = table[row1][(col1 - 1) % 5] + table[row2][(col2 - 1) % 5]
    elif col1 == col2:
        decrypted_bigram = table[(row1 - 1) % 5][col1] + table[(row2 - 1) % 5][col2]
    else:
        decrypted_bigram = table[row1][col2] + table[row2][col1]
    return decrypted_bigram
ciphertext = ciphertext.replace(" ", "")
ciphertext = ciphertext.upper()
bigrams = []
for i in range(0, len(ciphertext), 2):
    bigrams.append(ciphertext[i:i+2])
plaintext = ""
for bigram in bigrams:
    plaintext += decrypt_bigram(bigram)
print("Plaintext:", plaintext)