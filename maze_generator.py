import random
import io
from polja import *

def printlab(labirint):
    for red in labirint:
        for el in red:
            if el == None:
                print("x ", end = "")
            else:
                print(f"{el} ", end="")
        print("", end = "\n")

def printlabf(labirint):
    with io.open("maze.txt", 'w', encoding="utf8") as f:
        for red in labirint:
            for el in red:
                if el == None:
                    f.write("x ")
                else:
                    f.write(f"{el} ")
            f.write("\n")

def printlabf2(labirint):
    with io.open("maze.txt", 'w', encoding="utf8") as f:
        for red in labirint:
            for el in red:
                if el == None:
                    f.write("x")
                else:
                    f.write(str(el))
            f.write("\n")

def printmog(mogucnosti):
    for red in mogucnosti:
        for lista in red:
            print("[", end = "")
            for el in lista:
                print(f" {el}", end = "")
            print("], ", end = "")
        print("", end = "\n")

class Tocka:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"


def provjeri_mogucnosti(mogucnosti, polje, indeks):
    izlaz_polja = polje.izlazi.lista_izlaza[(indeks + 2) % 4]


    """  print(list(map(str, mogucnosti)))
    for i in range(len(mogucnosti)):
        print(mogucnosti[i]) """

    izbrisi_mogucnosti = []

    for i in range(len(mogucnosti)):
        if mogucnosti[i].izlazi.lista_izlaza[indeks] != izlaz_polja:
            izbrisi_mogucnosti.append(mogucnosti[i])

    ### DEBUGGING
    """ print(list(map(str, mogucnosti)))
    print(list(map(str, izbrisi_mogucnosti))) """

    for i in izbrisi_mogucnosti:
        mogucnosti.remove(i)

    """     for mogucnost in mogucnosti:
        print(indeks, mogucnost, polje)
        print(mogucnost.izlazi.lista_izlaza[indeks], izlaz_polja, mogucnost.izlazi.lista_izlaza[indeks] == izlaz_polja)
        if mogucnost.izlazi.lista_izlaza[indeks] != izlaz_polja:
            mogucnosti.remove(mogucnost) """
    #mogucnosti = [mogucnost for mogucnost in mogucnosti if mogucnost.izlazi.lista_izlaza[indeks] == izlaz_polja]

def postavi_polje(labirint, mogucnosti, x, y, polje):
    labirint[x][y] = polje
    mogucnosti[x][y] = []
    if (x > 0):
        provjeri_mogucnosti(mogucnosti[x-1][y], polje, 2)
        """ for mogucnost in mogucnosti[x-1][y]:
            if mogucnost.izlazi.dolje != polje.izlazi.gore:
                mogucnosti[x-1][y].remove(mogucnost) """
    if (y > 0):
        provjeri_mogucnosti(mogucnosti[x][y-1], polje, 1)
        """ for mogucnost in mogucnosti[x][y-1]:
            if mogucnost.izlazi.desno != polje.izlazi.lijevo:
                mogucnosti[x][y-1].remove(mogucnost) """
    if (x < len(labirint) - 1):
        provjeri_mogucnosti(mogucnosti[x+1][y], polje, 0)
        """ 
        for mogucnost in mogucnosti[x+1][y]:
            if mogucnost.izlazi.gore != polje.izlazi.dolje:
                mogucnosti[x+1][y].remove(mogucnost) """
    if (y < len(labirint[0]) - 1):
        provjeri_mogucnosti(mogucnosti[x][y+1], polje, -1)
        """
        for mogucnost in mogucnosti[x][y+1]:
            if mogucnost.izlazi.lijevo != polje.izlazi.desno:
                mogucnosti[x][y+1].remove(mogucnost) """
    return labirint, mogucnosti


def odaberi_tocku(tocke_na_redu, mogucnosti):
    mogucnosti_na_redu = list(map(lambda tocka: mogucnosti[tocka.x][tocka.y], tocke_na_redu))
    duljine_mogucnosti = list(map(len, mogucnosti_na_redu))
    odabrana_tocka = tocke_na_redu[duljine_mogucnosti.index(min(duljine_mogucnosti))]
    return odabrana_tocka


def generiraj_labirint(m, n):
    labirint = [[None] * n for _ in range(m)]
    mogucnosti = [[[inicijaliziraj_polje(i) for i in range(11 + 1)] for _ in range(n)] for _ in range(m)]
    mogucnosti[0] = [[inicijaliziraj_polje(i) for i in [0, 2, 8]] for _ in range(n)] ## gore su moguci '.' , '─' i '┬' 
    mogucnosti[m - 1] = [[inicijaliziraj_polje(i) for i in [0, 2, 10]] for _ in range(n)] ## dolje su moguci '.' , '─' i '┴'
    for i in range(m):
        mogucnosti[i][0] = [inicijaliziraj_polje(i) for i in [0, 1, 7]] ## lijevo su moguci '.' , '|' i '├'

    tocke_na_redu = [Tocka(0, 0)]

    while (tocke_na_redu):
        trenutna_tocka = odaberi_tocku(tocke_na_redu, mogucnosti)
        ### DEBUGGING
        """ print(f"{trenutna_tocka}, {list(map(str, tocke_na_redu))}")
        printlab(labirint)
        printmog(mogucnosti)
        input() """
        tocke_na_redu.remove(trenutna_tocka)
        x, y = trenutna_tocka.x, trenutna_tocka.y
        ## za sada je odabir iduceg polja nasumican izmedu svih mogucih
        if (mogucnosti[x][y]):
            odabrano_polje = random.choice(mogucnosti[x][y])
            labirint, mogucnosti = postavi_polje(labirint, mogucnosti, x, y, odabrano_polje)
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if 0 <= x + dx < m and 0 <= y + dy < n and mogucnosti[x + dx][y + dy]:
                        tocke_na_redu.append(Tocka(x + dx, y + dy))
        ### DEBUGGING
        """ else:
            printlab(labirint)
            printmog(mogucnosti)
            input("ERROR") """
   
    return labirint, mogucnosti


def main():
    m = int(input("m: "))
    n = int(input("n: "))
    labirint, mogucnosti = generiraj_labirint(m, n)
    printlabf2(labirint)
    printmog(mogucnosti)


if __name__ == '__main__':
    main()