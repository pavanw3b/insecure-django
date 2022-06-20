import pickle
from base64 import b64decode


def insecure_deserialize():
    with open("user.pickle", "rb") as file:
        user = pickle.load(file)
        print("Full Name: %s and Country: %s" % (user['full_name'], user['country']))


if __name__ == '__main__':
    insecure_deserialize()
