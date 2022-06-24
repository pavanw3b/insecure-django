import pickle
from base64 import b64decode


def insecure_deserialize():
    pickle_file = "user.pickle"
    with open(pickle_file, "rb") as file:
        print("Deserializing %s" % pickle_file)
        user = pickle.load(file)  # INSECURE!
        print("First Name: %s and Last Name: %s" % (user['first_name'], user['last_name']))


if __name__ == '__main__':
    insecure_deserialize()
