import tkinter
from N1Dokkan import *

class Ui: # No need to inherit 'object' in Python 3
    def __init__(self, root):
        self.root = root
        root.title("N1 - Module Dokkan")

    def Suppr_bouton(self):
        self.Bouton.place_forget()

    def Permutbouton_Demarrer(self):
        ControlStream()
        self.Suppr_bouton(self)
        self.Creer_bouton(Nom2, Texte, Commande2)

    def Bouton_Demarrer(self):
        self.Nombouton = Demarrer
        self.Nombouton = tkinter.Button(self.root, text='Démarrer Stream')
        self.Nombouton.config(command=Commande)
        self.Nombouton.place(x=75, y=100)

    def run(self):
        self.Creer_bouton('Demarrer', 'Démarrer', self.Permutbouton('ControlStream', 'Stop', 'Gros.....STOOOOOOOOP!', 'destroy'))
        self.root.mainloop()

if __name__=='__main__':
    root = tkinter.Tk()
    app = Ui(root)
    app.run()
