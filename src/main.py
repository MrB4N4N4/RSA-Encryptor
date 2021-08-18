from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii, os, glob

PATH = os.getcwd() + "\\..\\test"

# Generate RSA keys.
pri_key = RSA.generate(2048)
pub_key = pri_key.publickey()

# enc/dec functions ex) enc.encrypt(msg)
enc = PKCS1_OAEP.new(pub_key)
dec = PKCS1_OAEP.new(pri_key)

for file_path in glob.glob(PATH + "\\*.txt"):
    with open(file_path, "rb") as f:
        file_name = file_path.split("\\")[-1].split(".")[0]
        plain = f.read()
        encrypted = enc.encrypt(plain)

        print file_name + ".txt"
        print "Plain>"
        print plain
        print "Encrypted>"
        print encrypted

        with open("..\\test\\"+file_name+".cryp.txt", "wb") as c:
            c.write(encrypted)

for file_path in glob.glob(PATH + "\\*.cryp.txt"):
    with open(file_path, "rb") as f:
        file_name = file_path.split("\\")[-1].split(".")[0]
        encrypted = f.read()
        decrypted = dec.decrypt(encrypted)

        print file_name, ".cryp.txt"
        print "Decrypted>"
        print decrypted

        with open("..\\test\\"+file_name+".dec.txt", "w") as d:
            d.write(decrypted)
