import random

class TresEnRaya:
    def __init__(self, j1, j2):
        self.j1 = j1
        self.j2 = j2
        self.t = [" "] * 9
        self.turno = "X"
        self.nombre = j1
  

    def mostrar(self):
        print()
        for i in range(9):
            if self.t[i] == " ":
                print(i + 1, end=" ")
            else:
                print(self.t[i], end=" ")
            if (i + 1) % 3 == 0:
                print()

    def jugar(self, pos):
        if pos < 1 or pos > 9:
            return False
        if self.t[pos - 1] != " ":
            return False
        self.t[pos - 1] = self.turno
        return True

    def ganador(self):
        g = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        for c in g:
            if self.t[c[0]] == self.t[c[1]] == self.t[c[2]] != " ":
                self.ganador = self.turno
                return True
        return False

    def lleno(self):
        for i in range(9):
            if self.t[i] == " ":
                return False
        return True

    def reiniciar(self):
        self.t = [" "] * 9
        self.ganador = None

def cargar():
    try:
        with open("historial.txt", "r") as f:
            return eval(f.read())
    except:
        return {}

def guardar(h):
    with open("historial.txt", "w") as f:
        f.write(str(h))

def ver_historial(h):
    print("\n--- HISTORIAL ---")
    for nombre, puntos in h.items():
        print(f"{nombre}: {puntos}")

def jugar_partida(juego, h):
    while True:
        juego.mostrar()
        print(f"Turno: {juego.nombre} ({juego.turno})")
        p = input("Posicion (1-9): ")
        try:
            p = int(p)
        except:
            print("Numero invalido")
            continue
        if not juego.jugar(p):
            print("Movimiento invalido")
            continue
        if juego.ganador():
            juego.mostrar()
            print(f"¡{juego.nombre} GANA!")
            if juego.nombre in h:
                h[juego.nombre] = h[juego.nombre] + 1
            else:
                h[juego.nombre] = 1
            break
        if juego.lleno():
            juego.mostrar()
            print("EMPATE")
            break
        if juego.turno == "X":
            juego.turno = "O"
            juego.nombre = juego.j2
        else:
            juego.turno = "X"
            juego.nombre = juego.j1

# PROGRAMA PRINCIPAL
h = cargar()
print("=== TRES EN RAYA ===")

while True:
    print("\n1. Jugar")
    print("2. Ver historial")
    print("3. Salir")
    op = input("Elige: ")
    
    if op == "1":
        n1 = input("Jugador 1: ")
        n2 = input("Jugador 2: ")
        juego = TresEnRaya(n1, n2)
        if random.choice([True, False]):
            juego.nombre = n1
            juego.turno = "X"
        else:
            juego.nombre = n2
            juego.turno = "O"
        print(f"Comienza: {juego.nombre}")
        jugar_partida(juego, h)
        
        while True:
            r = input("Otra partida? (s/n): ").lower()
            if r == "s":
                juego.reiniciar()
                if random.choice([True, False]):
                    juego.nombre = n1
                    juego.turno = "X"
                else:
                    juego.nombre = n2
                    juego.turno = "O"
                print(f"Comienza: {juego.nombre}")
                jugar_partida(juego, h)
            elif r == "n":
                break
            else:
                print("Escribe s o n")
    
    elif op == "2":
        ver_historial(h)
    
    elif op == "3":
        guardar(h)
        print("Hasta luego")
        break
    
    else:
        print("Opcion invalida")