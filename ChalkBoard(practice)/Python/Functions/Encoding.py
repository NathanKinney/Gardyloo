import string




# def encrypt(text,shift):
#     encrypted_text = list(range(len(text)))
#     alphabet = string.ascii_lowercase
#
#     first_half = alphabet[:shift]
#     second_half = alphabet[shift:]
#
#     shifted_alphabet = second_half+first_half
#
#     for i,letter in enumerate(text.lower()):
#         if letter in alphabet:
#             original_index = alphabet.index(letter)
#             new_letter = shifted_alphabet[original_index]
#             encrypted_text[i] = new_letter
#         else:
#             encrypted_text[i] = letter
#
#     return ''.join(encrypted_text)
#
# print(encrypt('get this message to the server', 13))

def decrypt(text, shift):
    decrypted_text = list(range(len(text)))
    alphabet = string.ascii_lowercase

    first_half = alphabet[shift:]
    second_half = alphabet[:shift]

    shifted_alphabet = second_half+first_half

    for i,letter in enumerate(text.lower()):
        if letter in alphabet:
            index = alphabet.index(letter)
            original_letter = alphabet[index]
            decrypted_text[i] = original_letter
        else:
            decrypted_text[i] = letter

    return ''.join(decrypted_text)

print(decrypt('trg guvf zrffntr gb gur freire', 13))