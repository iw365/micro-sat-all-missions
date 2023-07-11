def caesar_decrypt(ciphertext, shift):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha(): #check if string is valid
            ascii_offset = ord('A') if char.isupper() else ord('a') #apply offset
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset) #decrpyt with key, accounting for overflow
            plaintext += decrypted_char #add to plaintext
        else:
            plaintext += char
    return plaintext

ciphertext = "JEJAHPEIAOHPDENPU" #string obtained with microbit-recieve_message.hex
for shift in range(0, 255): #wide range of results (not really necessary as will repeat every 26 shifts)
    plaintext = caesar_decrypt(ciphertext, shift)
    print(plaintext, shift)