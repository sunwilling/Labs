class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return self.title, self.author, self.year
Wap = Book("War and peace","Tolstoy",1869)
print(Wap.get_info())

    
    
