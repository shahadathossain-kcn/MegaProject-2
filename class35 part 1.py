# Stack Data Structure
# push and pop
books = []
books.append("Learn C")
books.append("Learn C++")
books.append("Learn Jave")
books.append("Learn Python")
books.append("Learn PHP")
books.append("Learn Camal")

print(books)

books.pop()
print(books)
print("Now the top book is: ", books[-1])

books.pop()
if not books:
    print("No books left :) ")
