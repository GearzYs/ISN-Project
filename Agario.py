from tkinter import *
from random import *

# Mise en place du Canvas

import ctypes
user32 = ctypes.windll.user32
screensizex = user32.GetSystemMetrics(0)
screensizey = user32.GetSystemMetrics(1)

fenetre= Tk()
fenetre.geometry("1280x1024")
fenetre.title("Agar.io")
fenetre.attributes("-fullscreen", True)
c=Canvas(fenetre,width=screensizex,height=screensizey,background='black')
c.pack()

# Création des variables
    # Joueur
        # Coordonnées du curseur :  
x,y=c.winfo_pointerxy()
x= c.canvasx(x)
y= c.canvasy(y)
        # Attribution coordonées du curseur => position de la boule joueur
playerx=x
playery=y
playerd=10
        # Création de la boule joueur
playerboule=c.create_oval(playerx,playery,playerx+playerd,playery+playerd,fill="red")

    # Bots
        # Listes
            # Coordonnées au hasard des boules
hasardx=[]
hasardy=[]
            # Diamètre des boules
d=[]
            # Déplacement des boules
dx=[]
dy=[]
            # Les boules
Boule=[]
            # Couleurs des boules
couleurs=["blue","green","cyan","magenta","yellow","white"]
            # Nombre de boules
nombreboule=300

# Création des boules

for i in range(nombreboule):
    hasardx.append(randint(20,screensizex-20))
    hasardy.append(randint(20,screensizey-20))
    d.append(randint(0,20))
    dx.append(randint(-2,2))
    dy.append(randint(-2,2))
    Boule.append(c.create_oval(hasardx[i],hasardy[i],hasardx[i]+d[i],hasardy[i]+d[i],fill=choice(couleurs)))

# Création des fonctions

    # Fonction permettant de déplacer la boule joueur

def joueur():
    global playerx, playery, playerboule, playerd
    x,y=c.winfo_pointerxy()
    x= c.canvasx(x)
    y= c.canvasy(y)
    playerx=x
    playery=y
    c.coords(playerboule,playerx,playery,playerx+playerd,playery+playerd)
    fenetre.after(10,joueur)

    # Fonction permettant de déplacer les boules

def boules():
    global hasardx, hasardy, d, Boule, dx, dy, nombreboule
    for i in range(nombreboule):
        hasardx[i]=hasardx[i]+dx[i]
        hasardy[i]=hasardy[i]+dy[i]
        if hasardx[i]>=screensizex or hasardx[i]<=0 :
            dx[i]=-dx[i]
        if hasardy[i]>=screensizey or hasardy[i]<=0 :
            dy[i]=-dy[i]
        c.coords(Boule[i],hasardx[i],hasardy[i],hasardx[i]+d[i],hasardy[i]+d[i])
    fenetre.after(10,boules)

def ajout():
    global hasardx, hasardy, d, Boule, dx, dy, nombreboule
    for i in range(10):
        nombreboule=nombreboule+1
        hasardx.append(randint(20,screensizex-20))
        hasardy.append(randint(20,screensizey-20))
        d.append(40)
        dx.append(randint(-2,2))
        dy.append(randint(-2,2))
        Boule.append(c.create_oval(hasardx[i],hasardy[i],hasardx[i]+d[i],hasardy[i]+d[i],fill=choice(couleurs)))

def annuler():
    global hasardx, hasardy, d, Boule, dx, dy, nombreboule
    nombreboule=nombreboule-1
    for i in range(10):
        hasardx.pop(nombreboule)
        hasardy.pop(nombreboule)
        d.pop(nombreboule)
        dx.pop(nombreboule)
        dy.pop(nombreboule)
        Boule.append(c.delete(nombreboule+1))
        nombreboule=nombreboule-1
    nombreboule=nombreboule+1

supprimer=Button(fenetre,text="Annuler les 10 Boules",command=annuler)
supprimer.place(x=screensizex-120,y=screensizey-25)

ajouter=Button(fenetre,text="Ajouter 10 Boules",command=ajout)
ajouter.place(x=screensizex-100,y=0)

boules()
joueur()

fenetre.mainloop()
