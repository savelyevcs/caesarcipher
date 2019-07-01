class CaesarCipherASCII():
    '''
        This class is a special realize of caesar cipher

        THE SPECIAL METHODS:
        __init__(text = None, shift = None) -> class initialization
        __repr__() -> returns encrypted or decrypted result

        THE PERSONAL METHODS:
        encrypt() -> text encrypting
        decrypt() -> text decrypting
        bunch() -> returns encrypted and decrypted value
        encrypted() -> returns encrypted value
        decrypted() -> returns decrypted value
    '''
    _ascii_lower = list('abcdefghijklmnopqrstuvwxyz')
    _ascii_upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def __init__(self, text = None, shift = None):
        if None in (text, shift):
            raise TypeError('<text> or <shift> argument not defined')

        self.text = text
        self.shift = shift
        self._en_buffer = self._de_buffer = ''

    def encrypt(self):
        for i in self.text:
            if not i.isalpha(): 
                self._en_buffer += i
            elif i in CaesarCipherASCII._ascii_upper:
                next_index = (
                    CaesarCipherASCII._ascii_upper.index(i) + self.shift
                ) % 26

                self._en_buffer += CaesarCipherASCII._ascii_upper[next_index]
            elif i in CaesarCipherASCII._ascii_lower:
                next_index = (
                    CaesarCipherASCII._ascii_lower.index(i) + self.shift
                ) % 26

                self._en_buffer += CaesarCipherASCII._ascii_lower[next_index]
    
    def decrypt(self):
        for i in self._en_buffer:
            if not i.isalpha():
                self._de_buffer += i
            elif i in CaesarCipherASCII._ascii_upper:
                prev_index = (
                    CaesarCipherASCII._ascii_upper.index(i) - self.shift
                ) % 26

                self._de_buffer += CaesarCipherASCII._ascii_upper[prev_index]
            elif i in CaesarCipherASCII._ascii_lower:
                prev_index = (
                    CaesarCipher._ascii_lower.index(i) - self.shift
                ) % 26

                self._de_buffer += CaesarCipher._ascii_lower[prev_index]

    @property
    def encrypted(self):
        if self._en_buffer == '':
            return 'The buffer is empty'

        return self._en_buffer

    @property
    def decrypted(self):
        if self._de_buffer == '':
            return 'The buffer is empty'

        return self._de_buffer
    
    @property
    def bunch(self):
        return {
            'encrypted': self._en_buffer,
            'decrypted': self._de_buffer
        }
