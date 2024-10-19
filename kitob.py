class Kitob:
    def __init__(self, name, author, price):
        self.name = name 
        self.author = author
        self.price = price
    
    def info(self):
        return f"""
Kitob nomi: {self.name}
Kitob yozuvchisi: {self.author}
Kitob narx: {self.price}
"""