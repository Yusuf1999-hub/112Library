from kitob import Kitob
from library import Library
from xodim import Xodim


b1 = Kitob('Atom odatlari', 'Kimdur', 12000)
b2 = Kitob("O'tgan kunlar", "Abdulla Qodiriy", 15000)
b3 = Kitob("EAT THAT FROG", "JACH ULU", 745820)
b4 = Kitob("Ichindagi ichingdadur", "Jaloliddin Rumiy", 30000)

a = Library("Alisher Navoiy")

x1 = Xodim("Karim", a)

x1.add_book(b1, 5)
x1.sell_book("Atom odatlari")


a.info()