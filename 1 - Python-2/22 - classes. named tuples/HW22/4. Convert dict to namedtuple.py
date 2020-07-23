from collections import namedtuple

def convert(obj):
    Person = namedtuple("Person", ["name", "phone_number", "age"])
    return Person(*obj.values())

data = {
    'name': 'Kathleen Stanton',
    'phone_number': '+1 (501)-376-9814',
    'age': 20}

print(convert(data))

