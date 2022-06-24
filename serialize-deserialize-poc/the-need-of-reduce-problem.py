import pickle


class MyClass(object):
    def __init__(self, file_path="1337-msg.txt"):
        self._file_name = file_path
        self.some_file_opened = open(self._file_name, 'wb')


my_test = MyClass()
saved_object = pickle.dumps(my_test)
print(repr(saved_object))

