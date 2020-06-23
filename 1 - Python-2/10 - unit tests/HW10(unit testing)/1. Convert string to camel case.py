https://www.codewars.com/kata/517abf86da9663f1d2000003
def to_camel_case(text):
    text = text.replace("-"," ").replace("_"," ").split()
    return "".join([el.title() if i > 0 else el for i, el in enumerate(text)])

print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))