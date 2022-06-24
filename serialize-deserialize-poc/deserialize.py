import pickle


def just_deserialize():
    content = b'\x80\x04\x95/\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\nfirst_name\x94\x8c\x05Bruce\x94\x8c\tlast_name\x94\x8c\x06Banner\x94u.'
    print(" ---- The Data before deserialization ----")
    print(content)
    pickled_object = pickle.loads(content)
    print(" ---- The Object after deserialization ----")
    print(pickled_object)


if __name__ == '__main__':
    just_deserialize()
