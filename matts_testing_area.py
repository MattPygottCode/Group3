#To do list
# Test with random keys
# Implement encrypting files
# The same for vigenere cipher
#preserve case of input
# add verbose
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


#key=int(input("Input key: "))
#print(caesar_cipher_encrypt("JamesWentForAWalk",key))
#print(caesar_cipher_decrypt(caesar_cipher_encrypt("JamesWentForAWalk",key),key))


#vigenere cipher

#-------------------testing-------------------



print(caesar_cipher_encrypt("James walked his dog called Jeremy!",2))
print(caesar_cipher_decrypt(caesar_cipher_encrypt("James walked his dog called Jeremy!",2),2))