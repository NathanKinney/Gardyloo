import string
import random

class Encryption():

    def __init__(self,seed):

        random.seed(seed)
        self.seed = seed

        self.encrypted_phrase = ''

        self.true_alphabet = list(string.ascii_lowercase)
        self.rand_alphabet = random.sample(self.true_alphabet, len(self.true_alphabet))

    def encryption(self,message):

        output = ''

        for i in range(len(message)):
            output += message[i]
            output += random.sample(self.true_alphabet, 1)[0]

        self.encrypted_phrase = output[::-1]

        encrypted_phase_two = list(range(len(self.encrypted_phrase)))

        for i, letter in enumerate(self.encrypted_phrase.lower()):
            if letter in self.true_alphabet:
                index = self.true_alphabet.index(letter)
                encrypted_phase_two[i] = self.rand_alphabet[index]
            else:
                encrypted_phase_two[i] = letter

        self.encrypted_phrase[i] = ''.join(encrypted_phase_two)
        return self.encrypted_phrase



    def decryption(self, message, seed):
        random.seed(seed)

        session_rand_alphabet = random.sample(self.true_alphabet, len(self.true_alphabet))

        decrypted_message = list(range(len(message)))

        for i, letter in enumerate(message.lower()):

            if letter in self.true_alphabet:
                index = session_rand_alphabet.index(letter)
                decrypted_message[i] = self.true_alphabet[index]
            else:
                decrypted_message[i] = letter
        decrypted_message = ''.join(decrypted_message)[::-1]

        return decrypted_message[::2]


