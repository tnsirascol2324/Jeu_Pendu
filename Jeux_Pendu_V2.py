import random

"""
    Classe représentant le jeu du pendu

    Attribut :
        mot (str) : Le mot à deviner par le joueur
    
    Methodes :
        nouveau_mot(self) -> str :
            Sélectionne un mot aléatoire parmi une liste prédéfinie
            Return :
                str : Le mot sélectionné

"""

class Pendu :
    
    def __init__(self) :
        self.mot = self.nouveau_mot()

    
    def nouveau_mot(self) :
        liste_mots = ['jeux', 'ordinateur', 'voiture','magnifique','tenture']
        return random.choice(liste_mots)

    
    def pendu_logique(self) :
        vie = 9
        vides = "_ " * len(self.mot)
        lettres = set()
        win = False
        while vie > 0 :
            print(str(vie) + "\n")
            lettre = input("Votre lettre ? (en munuscule) : " + vides + "\n")
            if not lettre.isalpha() or not lettre.islower() :
                print("Veuillez entrer une lettre en minuscules valide")
                continue

            if lettre in lettres:
                print("Vous avez déjà essayé cette lettre.")
                continue

            lettres.add(lettre)

            if lettre not in self.mot:
                vie -= 1

            vides = ""
            for char in self.mot:
                if char in lettres:
                    vides += char + " "
                else:
                    vides += "_ "

            print(vides + "\n")

            if vides.replace(" ", "") == self.mot:
                win = True
                break

        if win:
            print("Gagné !\n" + self.mot)
        else:
            print("Perdu ! Le mot était : " + self.mot)

    def jouer(self):
        print("Le jeu du pendu commence !")
        self.pendu_logique()
        msg = input("J pour jouer à nouveau ou Q pour quitter : ").lower()
        if msg == "j":
            self.mot = self.nouveau_mot()
            self.jouer()
        else:
            print("Merci d'avoir joué !")


jeu_pendu = Pendu()
jeu_pendu.jouer()
