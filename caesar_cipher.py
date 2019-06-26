import sys
import os
import string

class CaesarCipher():
    '''
        That the class is a special realize of caesar cipher

        THE SPECIAL METHODS:
        __init__(text, shift) type: main -> class initialization
        __repr__() type: return -> encrypted or decrypted result

        THE PERSONAL METHODS:
        encrypt() type: process -> text encrypting
        decrypt() type: process -> text decrypting
        get_result() type: return -> encrypted or decrypted result
        get_shift() type: return -> shift
    '''
    _ascii_letters = string.ascii_letters
    _ascii_lowercase_letters = string.ascii_lowercase
    _ascii_uppercase_letters = string.ascii_uppercase
    _ascii_unsigned_letters = '`~!#$%^&*()_+-={}[]:";\'<>,.?/\@1234567890 '

    def __init__(self, text, shift):
        self.text = list(text)
        self.shift = shift

    def __repr__(self):
        return ''.join(self.text)

    def encrypt(self):
        for i in range(len(self.text)):
            if self.text[i] in list(CaesarCipher._ascii_unsigned_letters):
                continue
            else:
                self.text[i] = chr(ord(self.text[i]) + self.shift)

    def decrypt(self):
        for i in range(len(self.text)):
            if self.text[i] in list(CaesarCipher._ascii_unsigned_letters):
                continue
            else:
                self.text[i] = chr(ord(self.text[i]) - self.shift)

    def get_result(self):
        return ''.join(self.text)

    def get_shift(self):
        return self.shift
