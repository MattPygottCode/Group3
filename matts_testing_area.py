#To do list
# Test with random keys
# Implement encrypting files
# The same for vigenere cipher
# Add input checks
#preserve case of input
# add verbose
global alphabet_upper
alphabet_upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
global alphabet_lower
alphabet_lower=alphabet_upper.lower()

#input cleaning function

def clean_text(g_in_text,preserve_case=True,verbose=False):
    in_text=g_in_text
    out_text=""
    if verbose:
        print("Input text is: ", in_text)
    if not(preserve_case):
        if verbose:
            print("Case not preserved so convert it to uppercase")
        in_text.upper()
    for i in range (0,len(in_text)):
        if in_text[i] in alphabet_lower:
            out_text+=in_text[i]
        elif in_text[i] in alphabet_upper:
            out_text+=in_text[i]
    return out_text


#caesar cipher

def caesar_cipher_encrypt(g_plain_text,g_key):#need to remove spaces and punctuation

    #plain_text should be fed in as a string, key should be any integer although it only is unique from 0,26

    plain_text=g_plain_text.upper() #creating local copies of arguments
    key=g_key # g for given
    cipher_text=""
    

    for i in range (0,len(plain_text)):
        position_in_alphabet=alphabet_upper.index(plain_text[i])
        cipher_text+=alphabet_upper[(position_in_alphabet+key)%26]
    return cipher_text

def caesar_cipher_decrypt(g_cipher_text,g_key):
    cipher_text=g_cipher_text.upper() #creating local copies of arguments
    key=g_key # g for given
    plain_text=""

    for i in range (0,len(cipher_text)):
        position_in_alphabet=alphabet_upper.index(cipher_text[i])
        plain_text+=alphabet_upper[(position_in_alphabet-key)%26]
    return plain_text


#key=int(input("Input key: "))
#print(caesar_cipher_encrypt("JamesWentForAWalk",key))
#print(caesar_cipher_decrypt(caesar_cipher_encrypt("JamesWentForAWalk",key),key))


#vigenere cipher

#-------------------testing-------------------

print(clean_text("AbcJIOjoiHiohIOo",verbose=True))