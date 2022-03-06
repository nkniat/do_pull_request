from usun_puste import *
from ile import *
from ile_a import *

path = 'C://Users//kamusial//Desktop//rolling_stones.txt'
with open (path, 'r') as file:
  content = file.readlines()
  content2 = file.read()

#funkcja usuwająca puste linie   "usun_puste"
content_bez_pustych = usun_puste(content)

#funkcja licząca ilość wystapień litery "a"     "ile_a"
print('Litera "a" wystepuje ', ile_a(content2),' razy')
      
#funkcja licząca ilość wystapień wskazanej litery     "ile"
print('Litera ' ,'x', ' wystepuje ', ile(content2, 'x'),' razy')

#funkcja biorąca "content" i zapisująca wszystkie linie w jednej liście     "razem"
content_razem = razem(content)

