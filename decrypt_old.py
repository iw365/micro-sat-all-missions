import string

alphabet = string.ascii_lowercase
ciphertext = 'JEJAHPEIAOHPDENPU' # 
plaintext = ''

for key in range(0, 127):
    for c in ciphertext:
        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            plaintext += new_character
        else:
            plaintext += c
    plaintext = plaintext.replace('$', ' ')
    print(f'\n\n{plaintext}\n\n')
    words = plaintext.split()
    print(words)

    wordset = open('words.txt', 'r')
    for word in words:
        wordcount = 0
        if word in wordset:
            wordcount += 1
        print(wordcount)
    wordset.close()

    plaintext = ''