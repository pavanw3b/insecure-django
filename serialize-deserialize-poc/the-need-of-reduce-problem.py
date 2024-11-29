import pickle


class MyClass(object):
    def __init__(self, file_path="1337-msg.txt"):
        # Enter the code from 11.a
        
        print() # You may delete this line


my_test = MyClass()
saved_object = pickle.dumps(my_test, )
print(repr(saved_object))

