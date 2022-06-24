from base64 import b64decode
import pickle


def just_deserialize():
    content = b'gASVLwAAAAAAAAB9lCiMCmZpcnN0X25hbWWUjAVCcnVjZZSMCWxhc3RfbmFtZZSMBkJhbm5lcpR1Lg=='
    content = b64decode(content)
    user_data = pickle.loads(content)
    print(user_data)


if __name__ == '__main__':
    just_deserialize()
