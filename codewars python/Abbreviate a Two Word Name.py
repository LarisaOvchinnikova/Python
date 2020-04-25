def abbrevName(name):
    name = name.upper()
    return f"{name[0]}.{name[name.index(' ') + 1]}"