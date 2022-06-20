import pickle


def just_serialize():
    user = {"full_name": "Pavan Mohan", "country": "India"}
    with open("user.pickle", "wb") as file:
        pickle.dump(user, file)


if __name__ == '__main__':
    just_serialize()
