# Check solutions.py for answers

class Bird:
    pass


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


if __name__ == '__main__':
    parrot_details = {
        "name": "Poly",
        "DOB": "24-06-2022",
        "owner": {
            "name": "Peppa's Granny"
        },
        "__class__": {
            "__qualname__": "Polluted"
        }
    }

    my_bird = Bird()
    print(vars(my_bird))

    merge(parrot_details, my_bird)

    print(vars(my_bird))
    print(my_bird)

    print(my_bird.__class__.__qualname__)

    print(Bird)
    print(Bird.__qualname__)

