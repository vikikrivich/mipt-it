def generate_rsa_keys():
    p = 3
    q = 7
    e = 5
    d = 17
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    pub_key = (e, n)
    private_key = (d, n)
    
    return pub_key, private_key


pub_key, private_key = generate_rsa_keys()
print(pub_key, private_key)


class CryptoBase:
    @staticmethod
    def mod_pow(m, e, n):
        result = m**e % n
        return result


class Encryptor(CryptoBase):
    def __init__(self, pub_key):
        self.pub_key = pub_key
    
    def __call__(self, message):
        e, n = self.pub_key
        return self.mod_pow(message, e, n)


class Decryptor(CryptoBase):
    def __init__(self, private_key):
        self.private_key = private_key
    
    def __call__(self, ciphertext):
        d, n = self.private_key
        return self.mod_pow(ciphertext, d, n)


num = 19
encrypted =  Encryptor(pub_key)(num)
decrypted = Decryptor(private_key)(encrypted)
print(f"{num} -> {encrypted} -> {decrypted}")
