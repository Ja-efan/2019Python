# 07092019
# __repr__() 메소트 활용 : 객체가 가진 정보를 한 줄로 반환

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn

    def __repr__(self):
        return "ISBN : " + self.title + "; TITLE : " + self.title


book = Book("The Python Turtoral", "0123456")
print(book)
