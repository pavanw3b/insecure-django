import pickle


def just_serialize_attacker():
    pickle_file = "attacker-user.pickle"
    # Change the below line from 10.a
    character = {}  # Remember to change this line!
    print(pickle.dumps(character))
    print("Pickling the below object:")
    print(character)
    with open(pickle_file, "wb") as file:
        pickle.dump(character, file)
    print("Pickled to: %s" % pickle_file)

if __name__ == '__main__':
    just_serialize_attacker()


