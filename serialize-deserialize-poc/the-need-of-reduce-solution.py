import pickle


class MyClass(object):
    def __init__(self, file_path="1337-msg.txt"):
        self._file_name = file_path
        self.some_file_opened = open(self._file_name, 'wb')

    def __reduce__(self):
        return self.__class__, (self._file_name,)


my_object = MyClass()
pickled_object = pickle.dumps(my_object)
print(repr(pickled_object))
