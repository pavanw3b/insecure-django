import pickle
from base64 import b64decode


def insecure_deserialize():
    content = 'gASVMQAAAAAAAAB9lCiMCWZ1bGxfbmFtZZSMC1BhdmFuIE1vaGFulIwHY291bnRyeZSMBUluZGlhlHUu'
    pickled_object = pickle.loads(b64decode(content))
    print(pickled_object)


if __name__ == '__main__':
    insecure_deserialize()
