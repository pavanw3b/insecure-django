from base64 import b64encode
import pickle


def just_serialize():
    user = {"full_name": "Pavan Mohan", "country": "India"}
    serialized_user = b64encode(pickle.dumps(user))
    print(serialized_user)


if __name__ == '__main__':
    just_serialize()
