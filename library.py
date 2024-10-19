from kitob import Kitob

class Library:
    def __init__(self, name):
        self.__kassa = 0
        self.name = name
        self.kitob_royxat = {}

    def kitob_qosh(self, obj:Kitob, miqdor):
        if obj.name not in self.kitob_royxat:
            self.kitob_royxat[obj.name] = {
                'miqdor':miqdor,
                'price':obj.price*3,
                'author':obj.author
            }
        else:
            self.kitob_royxat[obj.name]['miqdor'] += miqdor

    def kitob_sot(self, book_name):
        if book_name in self.kitob_royxat and  self.kitob_royxat[book_name]['miqdor'] != 0:
            self.kitob_royxat[book_name]['miqdor']-=1
            self.__kassa +=  self.kitob_royxat[book_name]['price']

    def info(self):
        print(f"""
Kitoblar: {self.kitob_royxat}""")