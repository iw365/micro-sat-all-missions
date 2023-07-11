
# import string

# ciphertext = 'hello'
# letter_frequency = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']

# #def frequency_analysis(ciphertext):
# # Create a dictionary to store the frequency of each character
# frequency = {}
# for char in ciphertext:
#     if char.isalpha():  # Consider only alphabetical characters
#         char = char.lower()  # Convert to lowercase for simplicity
#         if char in frequency:
#             frequency[char] += 1
#         else:
#             frequency[char] = 1

# print(frequency)

# sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

# print(sorted_freq)

# mapping = {}
# for i, (char, freq) in enumerate(sorted_freq):
#     mapping[char] = string.ascii_lowercase[i]
# print(mapping)

import string

alphabet = string.ascii_lowercase
ciphertext = 'JEJAHPEIAOHPDENPU'
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

    # wordset = open('words.txt', 'r')
    # for word in words:
    #     wordcount = 0
    #     if word in wordset:
    #         wordcount += 1
    #     print(wordcount)
    # wordset.close()

    plaintext = ''