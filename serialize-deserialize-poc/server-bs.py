from base64 import b64decode
import pickle


def insecure_deserialize():
    content = b'gASVIAAAAAAAAAB9lCiMCmZpcnN0X25hbWWUTowJbGFzdF9uYW1llE51Lg=='
    content = b64decode(content)
    user_data = pickle.loads(content)
    print(user_data)


if __name__ == '__main__':
    insecure_deserialize()
