import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

class AESCipher(object):

    def __init__(self, key): 
        self.bs = AES.block_size
        if isinstance(key, bytes):
            self.key = hashlib.sha256(key).digest()
        else:
            self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        if isinstance(raw, bytes):
            return base64.b64encode(iv + cipher.encrypt(raw))
        else:
            return base64.b64encode(iv + cipher.encrypt(raw.encode()))
        

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        #return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))

    def _pad(self, s):
        if not isinstance(s, bytes):
            return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)
        else:
            return s + ((self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)).encode()

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]