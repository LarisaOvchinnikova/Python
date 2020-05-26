def divide(a, b):
    try:
        result = a/b
        if result < 0:
            raise ValueError("Cannot be negative")
        return result
    except ZeroDivisionError as err:
        print(err)
        return 0

def add(a, b):
    return a + b

def main():
    print(add(2,3))
    pass

if __name__ == "__main__":
    main()
    print("Hello from imported", __name__)