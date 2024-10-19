from library import Library

class Xodim:
    def __init__(self, name, obj: Library):
        self.kutubxona = obj 
        self.name = name

    def add_book(self, obj, miqdor):
        self.kutubxona.kitob_qosh(obj, miqdor)

    def sell_book(self, name):
        self.kutubxona.kitob_sot(name)