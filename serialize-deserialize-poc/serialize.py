import pickle


def just_serialize():
    character = {"first_name": "Bruce", "last_name": "Banner"}
    print(" ---- The Object ----")
    print(character)
    serialized_character = pickle.dumps(character)
    print(" ---- The Serialized Data ----")
    print(serialized_character)


if __name__ == '__main__':
    just_serialize()
