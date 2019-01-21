def ces_cyp_decode(text, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    decoded_text=""
    for char in text:
        if char not in alphabet:
            decoded_text += char
        elif char in alphabet:
            index = alphabet.find(char,26,53)
            decoded_text += alphabet[index+offset]
    return decoded_text
#add more logic to detect other problems
