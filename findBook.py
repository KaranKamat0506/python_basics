#Program to check if a book exists in your collection of books 

collection=["The Good Investor","Steve Jobs","Elon Musk","The Alchemist"]
booktobeChecked=input("Enter book name: ")
for book in collection:
    if book==booktobeChecked:
        print("Yes,we do have the book.")
        break
else:
    print("No, I dont have that book.")

    