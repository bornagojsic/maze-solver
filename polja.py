class Polje:
    def __init__(self, izlazi):
        self.izlazi = izlazi

class Izlazi:
    def __init__(self, gore, desno, dolje, lijevo):
        self.gore = gore
        self.desno = desno
        self.dolje = dolje
        self.lijevo = lijevo
        self.lista_izlaza = [self.gore, self.desno, self.dolje, self.lijevo]

    def __str__(self):
        return f"{self.gore}:{self.desno}:{self.dolje}:{self.lijevo}"
    
    def get(self):
        return [self.gore, self.desno, self.dolje, self.lijevo]


def rotiraj_izlaze(izlazi):
    [gore, desno, dolje, lijevo] = izlazi.get()
    izlazi = Izlazi(lijevo, gore, desno, dolje)
    return izlazi


def rotiraj(izlazi, n = 1):
    for _ in range(n):
        izlazi = rotiraj_izlaze(izlazi)
    return izlazi

# . . .
# . . .
# . . .
class Polje0(Polje):
    def __init__(self):
        izlazi = Izlazi(gore = False,
                        desno = False,
                        dolje = False,
                        lijevo = False)
        super(Polje0, self).__init__(izlazi)
    
    def __str__(self):
        return '.'

# . x .
# . x .
# . x .    
class Polje1(Polje):
    def __init__(self):
        izlazi = Izlazi(gore = True,
                        desno = False,
                        dolje = True,
                        lijevo = False)
        super(Polje1, self).__init__(izlazi)
    
    def __str__(self):
        return "|"

# . . .
# x x x
# . . .
class Polje2(Polje1):
    def __init__(self):
        super(Polje2, self).__init__()
        self.izlazi = rotiraj(self.izlazi)
    
    def __str__(self):
        return "─"

# . x .
# . x x
# . . .
class Polje3(Polje):
    def __init__(self):
        izlazi = Izlazi(gore = True,
                        desno = True,
                        dolje = False,
                        lijevo = False)
        super(Polje3, self).__init__(izlazi)

    def __str__(self):
        return "└"

# . . .
# . x x
# . x .
class Polje4(Polje3):
    def __init__(self):
        super(Polje4, self).__init__()
        self.izlazi = rotiraj(self.izlazi)
    
    def __str__(self):
        return "┌"

# . . .
# x x .
# . x .
class Polje5(Polje3):
    def __init__(self):
        super(Polje5, self).__init__()
        self.izlazi = rotiraj(self.izlazi, 2)
    
    def __str__(self):
        return "┐"

# . x .
# x x .
# . . .
class Polje6(Polje3):
    def __init__(self):
        super(Polje6, self).__init__()
        self.izlazi = rotiraj(self.izlazi, 3)
    
    def __str__(self):
        return "┘"

# . x .
# . x x
# . x .
class Polje7(Polje):
    def __init__(self):
        izlazi = Izlazi(gore = True,
                        desno = True,
                        dolje = True,
                        lijevo = False)
        super(Polje7, self).__init__(izlazi)

    def __str__(self):
        return "├"

# . . .
# x x x
# . x .
class Polje8(Polje7):
    def __init__(self):
        super(Polje8, self).__init__()
        self.izlazi = rotiraj(self.izlazi)
    
    def __str__(self):
        return "┬"

# . x .
# x x .
# . x .
class Polje9(Polje7):
    def __init__(self):
        super(Polje9, self).__init__()
        self.izlazi = rotiraj(self.izlazi, 2)
    
    def __str__(self):
        return "┤"

# . x .
# x x x
# . . .
class Polje10(Polje7):
    def __init__(self):
        super(Polje10, self).__init__()
        self.izlazi = rotiraj(self.izlazi, 3)
    
    def __str__(self):
        return "┴"

# . x .
# x x x
# . x .
class Polje11(Polje):
    def __init__(self):
        izlazi = Izlazi(gore = True,
                        desno = True,
                        dolje = True,
                        lijevo = True)
        super(Polje11, self).__init__(izlazi)

    def __str__(self):
        return "┼"


def inicijaliziraj_polje(i):
    global inicijalizirano_polje
    exec(f"inicijaliziraj_polje = Polje{i}()", globals())
    return inicijaliziraj_polje


polja = [Polje0(), Polje1(), Polje2(), Polje3(), Polje4(), Polje5(), Polje6(), Polje7(), Polje8(), Polje9(), Polje10(), Polje11()]