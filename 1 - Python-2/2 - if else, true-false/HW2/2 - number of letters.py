name = input("What's your name? ")
if len(name) > 6:
    print(f"Wow! {name}, your name has lot of letters: {len(name)}")
else:
    print(f"Hello, {name}! Your name has only {len(name)} letters! ")