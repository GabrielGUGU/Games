import pgzrun

WIDTH = 600
HEIGHT = 400

TITLE = "Clicker Animal"
FPS = 30

# Objects
walrus = Actor('walrus', (480, 200))
crocodile = Actor('crocodile', (120, 200))
hippo = Actor('hippo', (300, 200))
animal = Actor("giraffe", (150, 250))
background = Actor("background")
bonus_1 = Actor("bonus", (450, 100))
bonus_2 = Actor("bonus", (450, 200))
bonus_3 = Actor("bonus", (450, 300))
play = Actor("play", (300, 100))
cross = Actor("cross", (580, 20))
tienda = Actor("tienda", (300, 200))
coleccion = Actor("coleccion", (300, 300))

# Variables
puntaje = 100000
click = 1
modo = 'menu'
precio_1 = 15
precio_2 = 200
precio_3 = 600
animals = []

def draw():
    screen.clear()
    if modo == 'menu':
        background.draw()
        play.draw()
        screen.draw.text(str(puntaje), center=(30, 20), color="white", fontsize=36)  # Fixed
        tienda.draw()
        coleccion.draw()
   
    elif modo == 'juego':    
        background.draw()
        animal.draw()
        screen.draw.text(str(puntaje), center=(150, 100), color="white", fontsize=96)  # Fixed
        bonus_1.draw()
        screen.draw.text("+1$ cada 2s", center=(450, 80), color="black", fontsize=20)
        screen.draw.text(str(precio_1), center=(450, 110), color="black", fontsize=20)  # Fixed
        bonus_2.draw()
        screen.draw.text("+15$ cada 2s", center=(450, 180), color="black", fontsize=20)
        screen.draw.text(str(precio_2), center=(450, 210), color="black", fontsize=20)  # Fixed
        bonus_3.draw()
        screen.draw.text("+50$ cada 2s", center=(450, 280), color="black", fontsize=20)
        screen.draw.text(str(precio_3), center=(450, 310), color="black", fontsize=20)  # Fixed
        cross.draw()
    
    elif modo == 'tienda':
        background.draw()
        crocodile.draw()
        screen.draw.text("500$", (120, 300), color="white", fontsize=36)
        hippo.draw()
        screen.draw.text("2500$", (300, 300), color="white", fontsize=36)
        walrus.draw()
        screen.draw.text("7000$", (480, 300), color="white", fontsize=36)
        cross.draw()
        screen.draw.text(str(puntaje), center=(30, 20), color="white", fontsize=36)  # Fixed
    
    elif modo == 'collection':
        background.draw()
        for a in animals:
            a.draw()
        cross.draw()
        screen.draw.text(str(puntaje), center=(30, 20), color="white", fontsize=36)  # Fixed
        screen.draw.text("+2$", (120, 300), color="white", fontsize=36)
        screen.draw.text("+3$", (300, 300), color="white", fontsize=36)
        screen.draw.text("+4$", (480, 300), color="white", fontsize=36)

def el_bonus_1():
    global puntaje
    puntaje += 1

def el_bonus_2():
    global puntaje
    puntaje += 15

def el_bonus_3():
    global puntaje
    puntaje += 50

def on_mouse_down(button, pos):
    global puntaje, modo, precio_1, precio_2, precio_3, click

    if button == mouse.LEFT:
        if modo == 'juego':
            if animal.collidepoint(pos):
                puntaje += click
                animal.y = 200
                animate(animal, tween='bounce_end', duration=0.5, y=250)
            elif bonus_1.collidepoint(pos) and puntaje >= precio_1:
                clock.schedule_interval(el_bonus_1, 2) 
                puntaje -= precio_1
                precio_1 *= 2
            elif bonus_2.collidepoint(pos) and puntaje >= precio_2:
                clock.schedule_interval(el_bonus_2, 2)
                puntaje -= precio_2
                precio_2 *= 2
            elif bonus_3.collidepoint(pos) and puntaje >= precio_3:
                clock.schedule_interval(el_bonus_3, 2)
                puntaje -= precio_3
                precio_3 *= 2
            elif cross.collidepoint(pos):
                modo = 'menu'

        elif modo == 'menu':
            if play.collidepoint(pos):
                modo = 'juego'
            elif tienda.collidepoint(pos):
                modo = 'tienda'
            elif coleccion.collidepoint(pos):
                modo = 'collection'

        elif modo == 'tienda':
            if cross.collidepoint(pos):
                modo = 'menu'
            elif crocodile.collidepoint(pos) and puntaje >= 500:
                animal.image = 'crocodile'
                puntaje -= 500
                click = 2
                animals.append(crocodile)
            elif hippo.collidepoint(pos) and puntaje >= 2500:
                animal.image = 'hippo'
                puntaje -= 2500
                click = 3
                animals.append(hippo)
            elif walrus.collidepoint(pos) and puntaje >= 7000:
                animal.image = 'walrus'
                puntaje -= 7000
                click = 4
                animals.append(walrus)

        elif modo == 'collection':
            if cross.collidepoint(pos):
                modo = 'menu'
            elif crocodile.collidepoint(pos) and crocodile in animals:
                animal.image = 'crocodile'
                click = 2
            elif hippo.collidepoint(pos) and hippo in animals:
                animal.image = 'hippo'
                click = 3
            elif walrus.collidepoint(pos) and walrus in animals:
                animal.image = 'walrus'
                click = 4

pgzrun.go()
