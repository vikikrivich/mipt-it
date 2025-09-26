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

def mod_pow(m, e, n):
    result = m**e % n
    
    return result

test_res = mod_pow(19, pub_key[0], pub_key[1])
print(test_res)

def euler(m, e, n):
    return mod_pow(m, e, n)

encrypt = euler(19, pub_key[0], pub_key[1])
print(encrypt)


class Crypto:
    def __init__(self, pub_key, private_key):
        self.pub_key = pub_key
        self.private_key = private_key
        self.encrypt = self.Encryptor(pub_key)
        self.decrypt = self.Decryptor(private_key)
    
    class Encryptor:
        def __init__(self, pub_key):
            self.pub_key = pub_key
        
        def __call__(self, message):
            e, n = self.pub_key
            return mod_pow(message, e, n)
    
    class Decryptor:
        def __init__(self, private_key):
            self.private_key = private_key
        
        def __call__(self, ciphertext):
            d, n = self.private_key
            return mod_pow(ciphertext, d, n)
        
crypto = Crypto(pub_key, private_key)

test_numbers = [5, 19, 8]
for num in test_numbers:
    encrypted = crypto.encrypt(num)
    decrypted = crypto.decrypt(encrypted)
    print(f"{num} -> {encrypted} -> {decrypted}")

print()

