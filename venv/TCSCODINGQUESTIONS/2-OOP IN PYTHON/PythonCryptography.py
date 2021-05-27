#https://www.geeksforgeeks.org/fernet-symmetric-encryption-using-cryptography-module-in-python/
# The function is expected to return a LIST.
# The function accepts following parameters:
#  1. STRING keyval
#  2. STRING textencr
#  3. Byte-code textdecr
#
from cryptography.fernet import Fernet


def encrdecr(keyval, textencr, textdecr):
    mainl = []
    # key=Fernet.generate_key()
    # value of key is assigned to a variable
    f = Fernet(keyval)
    token = f.encrypt(textencr)
    mainl.append(token)
    d = f.decrypt(textdecr)
    mainl.append(d.decode())
    return mainl


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    file = open('key.key', 'rb')
    key = file.read()  # The key will be type bytes
    file.close()

    keyval = key

    textencr = str(input()).encode()

    textdecr = str(input()).encode()

    result = encrdecr(keyval, textencr, textdecr)
    bk = []
    f = Fernet(key)
    val = f.decrypt(result[0])
    bk.append(val.decode())
    bk.append(result[1])

    fptr.write(str(bk) + '\n')

    fptr.close()