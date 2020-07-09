class Book:
  title = ""
  author = ""
  def get_title(self):
    return f"Title: {self.title}"
  def get_author(self):
    return f"Author: {self.author}"

HP = Book()
HP.title = "Harry Potter"
HP.author = "J.K. Rowling"
print(HP.get_title())
print(HP.get_author())

TS = Book()
TS.title = "The Adventures of Tom Sawyer"
TS.author = "Mark Twain"
print(TS.get_title())
print(TS.get_author())

GWW = Book()
GWW.title = "Gone with the Wind"
GWW.author = "Margaret Mitchell"
print(GWW.get_title())
print(GWW.get_author())