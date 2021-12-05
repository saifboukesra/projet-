import math
import numpy as np #est une bibliothèque numérique apportant le support efficace  de routines mathématiques de haut niveau (fonctions spéciales, algèbre linéaire, statistiques
import matplotlib.pyplot as plt # effectue un certain nombre de traitements pour préparer l'affichage du graphique

t= np.arange(0, 10, 0.01);
pi= math.pi


def getwave():
    AM=float(input("Donner amplitude:"))
    FM=float(input("Donner la frequence:"))
    return AM,FM

def affich(wave):
    plt.plot(t, wave)  #est utilisée pour créer une nouvelle figure
    plt.title('Modulation') #est utilisée pour afficher le titre de la visualisation représentée
    plt.xlabel('Temp')  #l'axe (x) en fonction de temp
    plt.ylabel('Amplitude ') #l'axe (y) en fonction de temp
    plt.grid(True, which='both', color='green', linestyle='--', linewidth=0.5) #est  utilisée pour configurer les lignes de la grille.
    plt.axhline(y=0, color='k') #est utilisée pour ajouter une ligne horizontale sur l'axe
    plt.show()
 #calcule de la Modulation d'amplitude à double bande sans porteuse (DBSP)
def mod_sp(ams,fms,amp,fmp,k=1):

    s=(k*amp*ams*np.cos(2*pi*fms*t))*np.cos(2*pi*fmp*t)
    return s
#calcule de la Modulation d'amplitude à double bande avec porteuse (DBAP)
def mod_ap(ams,fms,amp,fmp,k=1):
    s=amp*(1+k*ams*np.cos(2*pi*fms*t))*np.cos(2*pi*fmp*t)
    return s


"""
main program
"""

print("Representation de la figure Mdulation [AM]")
print("[1]-Modulation d'amplitude à double bande sans porteuse (DBSP)")
print("[2]-Modulation d'amplitude à double bande avec porteuse (DBAP)")
ch = int(input("\nvotre choix: "))
while True:
    if ch == 1:
        print("Signal: ")
        ams, fms = getwave()
        print("Porteuse: ")
        amp, fmp = getwave()
        affich(mod_sp(ams, fms, amp, fmp, k=1))
        break
    elif ch == 2:
        print("Signal: ",end="")
        ams, fms = getwave()
        print("Porteuse: ",end="")
        amp, fmp = getwave()
        affich(mod_ap(ams, fms, amp, fmp, k=1))
        break
    else:
        print("ERREUR")
        break

print("Bye!")