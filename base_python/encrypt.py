import Cryptodome.PublicKey.RSA
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import pkcs1_15
from Cryptodome.Hash import SHA256

class rsa:


    def __init__(self, key = None):
        if key == None:
            self.private_key, self.public_key  = self.generate_key_pair()
        else:
            self.private_key, self.public_key = self.generate_from_existing_key(key)

    def generate_from_existing_key(self, key):
        a = ""
        b = ""
        return a, b

    def test_if_key_is_right(self):
        if type(self.public_key) != RSA.RsaKey:
            self.public_key = Cryptodome.PublicKey.RSA.importKey(self.public_key)
        if type(self.private_key) != RSA.RsaKey:
            self.private_key = Cryptodome.PublicKey.RSA.import_key(self.private_key)
        print(type(self.private_key))

    def return_keys(self):
        return self.private_key.export_key().decode('utf-8'), self.public_key.export_key().decode('utf-8')

    def generate_key_pair(self):
        # Erzeugt ein RSA-Schlüsselpaar (öffentlich und privat)
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        return private_key, public_key

    def rsa_sign(self, plaintext):
        self.test_if_key_is_right()
        # Signiert den Text mit dem privaten RSA-Schlüssel
        h = SHA256.new(plaintext.encode('utf-8'))
        signature = pkcs1_15.new(self.private_key).sign(h)
        return signature

    def rsa_verify(self, plaintext, signature):
        self.test_if_key_is_right()
        # Verifiziert den Text mit dem öffentlichen RSA-Schlüssel und der Signatur
        h = SHA256.new(plaintext.encode('utf-8'))
        try:
            pkcs1_15.new(self.public_key).verify(h, signature)
            return True
        except (ValueError, TypeError):
            return False

if __name__ == "__main__":

    r = rsa()
    # Beispieltext
    text = "Hallo, dies ist eine Nachricht!"

    # Schlüsselpaar generieren
    private_key, public_key = r.generate_key_pair()

    # Text signieren
    signature = r.rsa_sign(private_key, text)
    print("Signatur:", signature)

    # Text verifizieren
    verified = r.rsa_verify(public_key, text, signature)
    print("Verifizierung erfolgreich:", verified)
