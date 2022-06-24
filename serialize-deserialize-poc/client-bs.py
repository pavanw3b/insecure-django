from base64 import b64encode
import pickle


def just_serialize():
    my_object = {"full_name": "Pavan Mohan", "country": "India"}
    pickled_object = pickle.dumps(my_object)
    pickled_object = b64encode(pickled_object)
    print(pickled_object.decode("utf-8"))


if __name__ == '__main__':
    just_serialize()
