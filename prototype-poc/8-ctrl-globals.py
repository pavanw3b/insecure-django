# Check solutions.py for answers

def merge(src, dst):
    # Recursive merge function
    for k, v in src.items():
        if hasattr(dst, '__getitem__'):
            if dst.get(k) and type(v) == dict:
                merge(v, dst.get(k))
            else:
                dst[k] = v
        elif hasattr(dst, k) and type(v) == dict:
            merge(v, getattr(dst, k))
        else:
            setattr(dst, k, v)


class Bird:
    def __init__(self):
        pass


class NotAccessibleClass:
    pass


not_accessible_variable = "value"

if __name__ == '__main__':
    merge({
            '__class__': {
                '__init__': {
                    '__globals__': {
                        'not_accessible_variable': 'Polluted variable',
                        'NotAccessibleClass': {
                            '__qualname__': 'PollutedClass'
                        }
                    }
                }
            }
    }, Bird())

    print(not_accessible_variable)
    print(NotAccessibleClass)
