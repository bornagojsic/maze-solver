import random

class Tocka:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Tocka(x, y)

def printpolje(labirint):
    for red in labirint:
        for el in red:
            if el == None:
                print("x ", end = "")
            else:
                print(f"{el} ", end="")
        print("", end = "\n")


def generiraj_vektor(vektor_razlike):
    if (vektor_razlike.x == 0 and vektor_razlike.y == 1):
        return '→'
    if (vektor_razlike.x == 0 and vektor_razlike.y == -1):
        return '←'
    if (vektor_razlike.x == 1 and vektor_razlike.y == 0):
        return '↓'
    if (vektor_razlike.x == -1 and vektor_razlike.y == 0):
        return '↑'
    return 'x'

def generiraj_susjede(stack, posjeceno, m, n):
    trenutna_tocka = stack[-1]
    x = trenutna_tocka.x
    y = trenutna_tocka.y
    susjedi = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if abs(dx) + abs(dy) <= 1 and 0 <= x + dx < m and 0 <= y + dy < n:
                if not posjeceno[x + dx][y + dy] and not Tocka(x + dx, y + dy) in stack:
                    susjedi.append(Tocka(x + dx, y + dy))
    print(list(map(str, susjedi)))
    if susjedi == []:
        stack.pop()
        susjedi = generiraj_susjede(stack, posjeceno, m, n)
    return susjedi

def generiraj_put(m, n):
    polje = [['.' for _ in range(n)] for _ in range(m)]
    posjeceno = [[0 for _ in range(n)] for _ in range(m)]
    start = random.randint(0, n - 1)
    stack = [Tocka(0, start)]
    trenutna_tocka = stack[-1]
    while (trenutna_tocka.x != m - 1):
        x = trenutna_tocka.x
        y = trenutna_tocka.y
        print(f"{x=}, {y=}")
        posjeceno[x][y] = 1
        susjedi = generiraj_susjede(stack, posjeceno, m, n)
        stack.append(random.choice(susjedi))
        trenutna_tocka = stack[-1]
    stack.append(Tocka(m, stack[-1].y))
    print(list(map(str, stack)))
    for i, tocka in enumerate(stack[:-1]):
        vektor_razlike = stack[i + 1] - tocka
        print(tocka, stack[i + 1], vektor_razlike, generiraj_vektor(vektor_razlike))
        polje[tocka.x][tocka.y] = generiraj_vektor(vektor_razlike)
    return polje  


def main():
    m = int(input("m: "))
    n = int(input("n: "))
    put = generiraj_put(m, n)
    printpolje(put)

if __name__ == '__main__':
    main()