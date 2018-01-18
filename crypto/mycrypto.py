import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
from crypto.fileoperations import myfile  # internal function


def generate_key_pair():
    random_generator = Random.new().read
    key = RSA.generate(2048, random_generator)  # generate pub and priv key
    publickey = key.publickey().exportKey('PEM')  # pub key export for exchange
    privatekey = key.exportKey('PEM')
    myfile.writefile("testSecret.key", privatekey.decode("utf-8"))
    myfile.writefile("testPublic.key", publickey.decode("utf-8"))
    print('public key: \n{0}'.format(publickey.decode("utf-8")))


def encrypt_and_write(message, keyname, write_to):
    public_key_str = myfile.readfile(keyname)
    publickey = RSA.importKey(public_key_str)
    encrypted_text = publickey.encrypt(message.encode('utf-8'), 32)
    myfile.writefile(write_to, str(encrypted_text))
