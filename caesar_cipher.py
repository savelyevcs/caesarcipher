class CaesarCipher():
    '''
        This class is a special realize of caesar cipher

        THE SPECIAL METHODS:
        __init__(text = None, shift = None) -> class initialization
        __repr__() -> returns encrypted or decrypted result

        THE PERSONAL METHODS:
        encrypt() -> text encrypting
        decrypt() -> text decrypting
        get_result() -> returns encrypted or decrypted value
        get_encrypted_result() -> returns encrypted value
        get_decrypted_result() -> returns decrypted value
    '''
    _ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    _ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, text = None, shift = None):
        if not any((text, shift)):
            raise Exception('You did not enter one of the values')
            return

        self.text = list(text)
        self.shift = shift
        self.encrypt_buffer = ''
        self.decrypt_buffer = ''

    def encrypt(self):
        for i in self.text:
            if not i.isalpha(): 
                self.encrypt_buffer += i
            elif i in list(CaesarCipher._ascii_uppercase):
                next_index = (
                    CaesarCipher._ascii_uppercase.index(i) + self.shift
                ) % 26

                self.encrypt_buffer += CaesarCipher._ascii_uppercase[next_index]
            elif i in list(CaesarCipher._ascii_lowercase):
                next_index = (
                    CaesarCipher._ascii_lowercase.index(i) + self.shift
                ) % 26

                self.encrypt_buffer += CaesarCipher._ascii_lowercase[next_index]
    
    def decrypt(self):
        for i in self.encrypt_buffer:
            if not i.isalpha():
                self.decrypt_buffer += i
            elif i in list(CaesarCipher._ascii_uppercase):
                prev_index = (
                    CaesarCipher._ascii_uppercase.index(i) - self.shift
                ) % 26

                self.decrypt_buffer += CaesarCipher._ascii_uppercase[prev_index]
            elif i in list(CaesarCipher._ascii_lowercase):
                prev_index = (
                    CaesarCipher._ascii_lowercase.index(i) - self.shift
                ) % 26

                self.decrypt_buffer += CaesarCipher._ascii_lowercase[prev_index]

    def get_encrypted_result(self):
        return self.encrypt_buffer

    def get_decrypted_result(self):
        return self.decrypt_buffer
    
    def get_result(self):
        return {
            'encrypted': self.encrypt_buffer,
            'decrypted': self.decrypt_buffer
        }
