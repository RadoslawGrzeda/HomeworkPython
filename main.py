'''
[LAB 1-CZESC]
1. Mamy zadaną listę [4, 4, 4, 2, 2, 3, 5, 6, 7, 8, 7, 5, 4, 3, 2, 4]., Proszę BEZ używania pętli wyznaczyć
element listy, który powtarza się najczęściej.
2. Napisz program w Pythonie, aby utworzyć krotkę.
3. Napisz program w Pythonie, aby utworzyć krotkę z różnymi typami danych.
4. Napisz program w Pythonie, który utworzy krotkę liczb i wyświetli tylko jeden element.
5. Napisz program w Pythonie, aby przekonwertować krotkę na słownik.
6. Napisz program, w którym będą wykonywanie operacje dodawania i odejmowania na liczbach całko-
witych.
7. Napisz program imitujący dialog dwóch postaci.

[LAB 2-CZESC]
1. Napisz program drukujący podaną liczbę x (np. ośmiocyfrową) w odwrotnej kolejności.
2. Napisz program, który wypisze piętnaście pierwszych wielokrotności liczby 3.
3. Napisz program, który wpisze wszystkie dzielniki naturalne podanej wcześniej liczby n.
4. Napisz program rysujący prostokąt z gwiazdek o wymiarach n × m.
'''

#[LAB 1-CZESC]

#1
l=[4, 4, 4, 2, 2, 3, 5, 6, 7, 8, 7, 5, 4, 3, 2, 4];
mod=max(l,key=l.count)
print(mod)
#2
k=(1,2,3,3,5,1)
print(k)
#3
k=(1,2,3,'ALA',[1,2,3],{'a'})
print(k)
#4
k=(1,2,3,4,5,6)
print(k[1])
#5
k=(1,2,3,'ALA',[1,2,3],{'a'})
s={}
for i in range(len(k)):
   s[i]=k[i]
print(s)
#6
x=1_120_231
y=6_512
print(x-y)
print(x+y)
##
con=True;
# while con:
#
#     x = input('Osoba1: ')
#     y = input('Osoba2: ')
#     if x=='STOP' or y=='STOP':
#         con=False
    # print(y)
'''
1. Napisz program drukujący podaną liczbę x (np. ośmiocyfrową) w odwrotnej kolejności.
2. Napisz program, który wypisze piętnaście pierwszych wielokrotności liczby 3.
3. Napisz program, który wpisze wszystkie dzielniki naturalne podanej wcześniej liczby n.
4. Napisz program rysujący prostokąt z gwiazdek o wymiarach n × m.
'''
#[LAB 2-CZESC]
#1
# x=input('Podaj cyfre')
# x=x[::-1]
# print(x)
#2
l=[]
for i in range(1,16):
    l.append(i*3);
print(l)
#3