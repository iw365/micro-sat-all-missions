def caesar_decrypt(ciphertext, shift):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

ciphertext = "JEJAHPEIAOHPDENPU"
for shift in range(0, 255):
    plaintext = caesar_decrypt(ciphertext, shift)
    print(plaintext, shift)