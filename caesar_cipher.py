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
    _ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    _ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, text, shift):
        self.text = list(text)
        self.shift = shift
        self._buffer = []

    def __repr__(self):
        return ''.join(self.text)

    def encrypt(self):
        for i in self.text:
            if not i.isalpha(): 
                self._buffer.append(i)
                continue
            elif i in list(CaesarCipher._ascii_uppercase):
                shifted_index = (
                    CaesarCipher._ascii_uppercase.index(i) + self.shift
                ) % len(CaesarCipher._ascii_uppercase)

                self._buffer.append(
                    CaesarCipher._ascii_uppercase[shifted_index]
                )
            elif i in list(CaesarCipher._ascii_lowercase):
                shifted_index = (
                    CaesarCipher._ascii_lowercase.index(i) + self.shift
                ) % len(CaesarCipher._ascii_lowercase)

                self._buffer.append(
                    CaesarCipher._ascii_lowercase[shifted_index]
                )

    def get_result(self):
        return ''.join(self._buffer)

    def get_shift(self):
        return self.shift
