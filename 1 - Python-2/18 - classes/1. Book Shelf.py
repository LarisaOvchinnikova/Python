class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def get_title(self):
        return f"Title: {self.title}"

    def get_author(self):
        return f"Author: {self.author}"


HP = Book("Harry Potter", "J.K. Rowling" )

print(HP.get_title())
print(HP.get_author())

TS = Book("The Adventures of Tom Sawyer", "Mark Twain")

print(TS.get_title())
print(TS.get_author())

GWW = Book("Gone with the Wind", "Margaret Mitchell")

print(GWW.get_title())
print(GWW.get_author())