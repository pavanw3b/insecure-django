import pickle


def just_serialize():
    pickle_file = "user.pickle"
    character = {"first_name": "Tony", "last_name": "Stark"}
    print("Pickling the below object:")
    print(character)
    with open(pickle_file, "wb") as file:
        pickle.dump(character, file)
    print("Pickled to: %s" % pickle_file)


if __name__ == '__main__':
    just_serialize()
