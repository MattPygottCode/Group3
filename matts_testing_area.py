#To do list
# Test with random keys
# Implement encrypting files
# The same for vigenere cipher
# Add input checks

#caesar cipher

def caesar_cipher_encrypt(g_plain_text,g_key):#need to remove spaces and punctuation

#plain_text should be fed in as a string, key should be any integer although it only is unique from 0,26

    plain_text=g_plain_text.upper() #creating local copies of arguments
    key=g_key # g for given
    cipher_text=""
    global alphabet
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range (0,len(plain_text)):
        position_in_alphabet=alphabet.index(plain_text[i])
        cipher_text+=alphabet[(position_in_alphabet+key)%26]
    return cipher_text

def caesar_cipher_decrypt(g_cipher_text,g_key):
    cipher_text=g_cipher_text.upper() #creating local copies of arguments
    key=g_key # g for given
    plain_text=""
    global alphabet
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range (0,len(cipher_text)):
        position_in_alphabet=alphabet.index(cipher_text[i])
        plain_text+=alphabet[(position_in_alphabet-key)%26]
    return plain_text


#key=int(input("Input key: "))
#print(caesar_cipher_encrypt("JamesWentForAWalk",key))
#print(caesar_cipher_decrypt(caesar_cipher_encrypt("JamesWentForAWalk",key),key))


#vigenere cipher


