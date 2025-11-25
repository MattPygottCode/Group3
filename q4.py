#create bigrams
#perform one letter into one or more bigrams 
#do vigenere encryption
#transfer bigram mapping into a key
#decode and obtain the original message

import random
import string

#generate bigrams 
def generate_bigrams():
    letters = string
    letters = "ABCDEFGHIJKLNMOPQRSTUVWXYZ"
    all_bigrams = []
    for a in letters:
        for b in letters:
            if a != b:
                all_bigrams.append(a+b)
    return all_bigrams


#seprate bigrams into each letter
def bigrams_mapping(total_bigrams = 400):
    letter_frequency = {
        'E': 0.127, 'T': 0.091, 'A': 0.0812, 'O': 0.0768, 
        'I': 0.0757,'N': 0.0723, 'S': 0.0651, 'R': 0.0628, 'H': 0.0505, 
        'L': 0.0407, 'D': 0.0382, 'C': 0.0334, 'U': 0.0273, 'M': 0.0251, 
        'W': 0.0168, 'F': 0.024, 'G': 0.0187, 'Y': 0.0166, 'P': 0.0214, 
        'B': 0.0148, 'V': 0.0105, 'K': 0.0054, 'X': 0.0023,'J': 0.0016,
        'Q': 0.0012, 'Z': 0.0009
    }
    letters = "ABCDEFGHIJKLNMOPQRSTUVWXYZ"
    all_bigrams = generate_bigrams()
    random.shuffle(all_bigrams)

    sizes = {}
    for ch in letters:
        sizes[ch] = letter_frequency[ch] * total_bigrams

    bigrams_per_letter = {}
    for ch in letters:
        num = round(sizes[ch])
        if num < 1:
            num = 1
        bigrams_per_letter[ch] = num

    map_bigrams = {}
    index = 0
    for ch in letters:
        k = bigrams_per_letter[ch]
        map_bigrams[ch] = all_bigrams[index : index + k]
        index += k
    return map_bigrams

#test
#map = bigrams_mapping()
#print(map["E"])

#randomly encode before Vigenère encryption
def message_encode(message, map_bigrams):
    message = message.upper()
    message = message.replace(" ", "")
    encoded = ""

    for ch in message:
        if ch in map_bigrams:
            bigram_list = map_bigrams[ch]
            chosen_bigram = random.choice(bigram_list)
            encoded = encoded + chosen_bigram
        else:
            print("Error")
            return None
        
    return encoded

#test
#mapping = {
#    "H": ["TR", "AB"],
#    "E": ["LM"],
#    "L": ["XY", "PO"],
#    "O": ["GH", "QZ"]
#}

#print(message_encode("HELLO", mapping))

#bigrams to letters
def inverse_mapping(map_bigrams):
    inverse = {}
    for letter in map_bigrams:
        bigrams_list = map_bigrams[letter]

        for code in bigrams_list:
            inverse[code] = letter

    return inverse

#decode part
def bigrams_decode(encoded, map_bigrams):
    inverse = inverse_mapping(map_bigrams)

    if len(encoded) % 2 != 0:
        print("error")
        return None
    
    decoded_text = ""
    for i in range(0, len(encoded), 2):
        bg = encoded[i: i + 2]
        decoded_text += inverse[bg]

    return decoded_text
        
#test
mapping = bigrams_mapping(400)
messages = [
    "HELLO",
    "THIS IS A TEST",
]
for msg in messages:
    print(msg)

    encoded_bigram = message_encode(msg, mapping)
    print(encoded_bigram)

    decoded_text = bigrams_decode(encoded_bigram, mapping)
    print(decoded_text) 