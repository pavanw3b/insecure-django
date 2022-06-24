from base64 import b64encode
import pickle


def just_serialize():
    character = {"first_name": "Bruce", "last_name": "Banner"}
    pickled_object = pickle.dumps(character)
    pickled_object = b64encode(pickled_object)
    print(pickled_object.decode("utf-8"))


if __name__ == '__main__':
    just_serialize()
