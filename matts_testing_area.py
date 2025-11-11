# To do list
# Test with random keys
# Implement encrypting files
# Write an encrypt to file function that preserves new lines

#imports
import os


#Global variables
global alphabet_upper
alphabet_upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
global alphabet_lower
alphabet_lower=alphabet_upper.lower()


#input cleaning function

def clean_text(g_in_text,preserve_case=True,verbose=False):
    in_text=g_in_text#make a local copy
    out_text=""
    if verbose:
        print("Input text is: ", in_text)
    for i in range (0,len(in_text)): #run through all characters and add them if they are in the alphabet
        if in_text[i] in alphabet_lower:
            out_text+=in_text[i]
        elif in_text[i] in alphabet_upper:
            out_text+=in_text[i]
    if verbose:
        print("Text without spaces, symbols, numbers ",out_text)
    if not(preserve_case): #if we aren't preserving the case then we convert it all to upper case
        out_text=str(out_text.upper())
        if verbose:
            print("Case not preserved so convert it to uppercase ",out_text)
    return out_text


#caesar cipher

def caesar_cipher_encrypt(g_plain_text,g_key,verbose=False):

    #plain_text should be fed in as a string, key should be any integer although it only is unique from 0,26

    plain_text=g_plain_text #creating local copies of arguments
    key=g_key # g for given
    cipher_text=""

    plain_text=clean_text(plain_text) #clean the input

    for i in range (0,len(plain_text)):
        if plain_text[i] in alphabet_upper:
            position_in_alphabet=alphabet_upper.index(plain_text[i])
            cipher_text+=alphabet_upper[(position_in_alphabet+key)%26]
        else: #if adding support for spaces later add it below and change the clean_text function to suppport this
            position_in_alphabet=alphabet_lower.index(plain_text[i])
            cipher_text+=alphabet_lower[(position_in_alphabet+key)%26]
    return cipher_text

def caesar_cipher_decrypt(g_cipher_text,g_key):
    #assume as the data has been ciphered it is clean
    cipher_text=g_cipher_text #creating local copies of arguments
    key=g_key # g for given
    plain_text=""

    for i in range (0,len(cipher_text)):
        if cipher_text[i] in alphabet_upper:
            position_in_alphabet=alphabet_upper.index(cipher_text[i])
            plain_text+=alphabet_upper[(position_in_alphabet-key)%26]
        else: #if adding support for spaces later add it below and change the clean_text function to suppport this
            position_in_alphabet=alphabet_lower.index(cipher_text[i])
            plain_text+=alphabet_lower[(position_in_alphabet-key)%26]
    return plain_text


#vigenere cipher

def v_cipher_encrypt(g_plain_text,g_key,verbose=False):
    plain_text=clean_text(g_plain_text)
    key=clean_text(g_key,preserve_case=False)
    cipher_text=""

    #for each letter in plain text message we perform a caesar cipher on it using the ith char in key
    for i in range (0,len(plain_text)):
        ith_key=alphabet_upper.index(key[i%len(key)])
        if verbose:
            print("Ith key is", ith_key)
        cipher_text+=caesar_cipher_encrypt(plain_text[i],ith_key)
    return cipher_text

def v_cipher_decrypt(g_cipher_text, g_key,verbose=False):
    cipher_text=clean_text(g_cipher_text)#assume the cipher text is clean
    key=clean_text(g_key,preserve_case=False)
    plain_text=""

    #for each letter in cipher text we decrypt using caesar cipher with key corresponding to the char position
    for i in range(0, len(cipher_text)):
        ith_key=alphabet_upper.index(key[i%len(key)])
        if verbose:
            print("Ith key is",ith_key)
        plain_text+=caesar_cipher_decrypt(cipher_text[i],ith_key)
    return plain_text


#-------------------testing-------------------

# -------------------MATT-------------------

# Here, we can read and encrypt the plain text
# We then put the encrypted outcome into the cipher_text file (which was originally empty)

#temp=v_cipher_encrypt("James walked his dog called Jeremy!","Hjksdhjksahfjhdakjvhuieshdhfjkdvkjhdvkjhkjlahefliu")
#print(temp)
#print(v_cipher_decrypt(temp,"Hjksdhjksahfjhdakjvhuieshdhfjkdvkjhdvkjhkjlahefliu"))

file_plain_text=open("text_files/plain_text.txt","r")
file_cipher_text=open("text_files/cipher_text.txt","w")
file_cipher_text.write(caesar_cipher_encrypt(file_plain_text.read(),3))

# -------------------BO-------------------
# Here, I'm playing around with printing the encrpyted pain text
# Rather than creating a new text file, which is probably better practice...

# file_plain_text=open("text_files/plain_text.txt","r")
# cipher = caesar_cipher_encrypt(file_plain_text.read(), 3)
# print(cipher)

# -------------------MATT-------------------
# This is back to Matt's code

file_plain_text.close()
file_cipher_text.close()
