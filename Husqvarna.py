# Lire le fichier Tondeuses.txt
def readFile():
    # Ouvrir le fichier et le séparer ligne par ligne
    file = open("Tondeuses.txt", "r")
    file = file.read().splitlines()

    # Retirer les espaces blancs
    for f in range(len(file)):
        file[f] = file[f].strip()

    return file

# Classe Tondeuse
class Tondeuse():
    # Position x qui correspond au premier charactère de la ligne
    x = 0
    # Position y qui correspond au second charactère de la ligne
    y = 0
    # Orientation qui correspond au quatrième charactère de la ligne
    orientation = "N"

    # Constructeur de la tondeuse
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    # Afficher la position actuelle de la tondeuse (format : xy o)
    def currentPosition(self):
        print(self.x, self.y, " ", self.orientation, sep = "")

    # Changer l'orientation de la tondeuse
    def changeOrientation(self, orientationOrder):
        # Liste des orientations
        orientations = ["N", "E", "S", "W"]

        # Si l'ordre est d'aller à droite
        if orientationOrder == "D":
            # Si on est au bout du tableau des orientations, on repasse au début (pour éviter une exception out of range)
            if self.orientation == orientations[len(orientations) - 1]:
                self.orientation = orientations[0]
            # Sinon on cherche dans le tableau l'orientation actuelle et on l'incrémente de 1
            else:
                i = 0
                changed = False
                while changed == False and orientations[i] != orientations[len(orientations) - 1]:
                    if self.orientation == orientations[i]:
                        self.orientation = orientations[i + 1]
                        changed = True
                    i += 1

        # Sinon à gauche
        elif orientationOrder == "G":
            # Si on est au début du tableau des orientations, on repasse à la fin (pour éviter une mauvaise orientation)
            if self.orientation == orientations[0]:
                self.orientation = orientations[len(orientations) - 1]
            else:
                # On cherche comme pour la droite, mais dans le sens inverse (en partant de -1, donc la dernière valeure de la liste)
                i = -1
                changed = False
                while changed == False and orientations[i] != orientations[0]:
                    if self.orientation == orientations[i]:
                        self.orientation = orientations[i - 1]
                        changed = True
                    i -= 1

    # Bouger la tondeuse
    def move(self, order, xMax, yMax):
        # Si l'ordre est de changer d'orientation (droite ou gauche)
        if order == "D" or order == "G":
            self.changeOrientation(orientationOrder = order)
        # Sinon si l'ordre est d'avancer, on avance en fonction de l'orientation actuelle uniquement si on ne dépasse pas la valeure maximale pour l'axe des x et y
        elif order == "A":
            if self.orientation == "N" and self.y != yMax:
                self.y += 1
            elif self.orientation == "E" and self.x != xMax:
                self.x += 1
            elif self.orientation == "S" and self.y != yMax * -1:
                self.y -= 1
            elif self.orientation == "W" and self.x != xMax * -1:
                self.x -= 1

# Main
if __name__ == "__main__":
    # Liste des lignes
    lines = readFile()
    # On récupère la valeure max pour l'axe des x et y (en int, pour pouvoir bien faire les comparaisons)
    xMax = int(lines[0][0])
    yMax = int(lines[0][1])
    # On retire la première ligne pour n'avoir que le format suivant : position | instruction
    del lines[0]
    # Liste des tondeuses
    tondeuses = []
    # Liste des instructions
    instructions = []

    # Construction des objets tondeuses et de la liste des instructions
    i = 0
    for line in range(len(lines)):
        i += 1
        # Si on est sur une ligne paire
        if (i == 1):
            # Création d'un objet tondeuse avec les données x, y et son orientation
            tondeuse = Tondeuse(x = int(lines[line][0]), y = int(lines[line][1]), orientation = lines[line][3])
            # On ajoute la tondeuse à la liste tondeuses
            tondeuses.append(tondeuse)
        else:
            # On ajoute les instructions dans la liste instructions
            instructions.append(lines[line])
            i = 0

    # Pour chaque ligne d'instruction dans notre liste instructions, on bouge notre tondeuse correspondante dans la liste tondeuses (qui a le même index)
    for i in range (len(instructions)):
        for c in instructions[i]:
            # On bouge la tondeuse pour chaque caractère sur la ligne, on donne également la valeure maximale de l'axe des x et y à ne pas dépasser
            tondeuses[i].move(order = c, xMax = xMax, yMax = yMax)
        
        # Quand une tondeuse a terminée ses instructions, elle affiche sa position et son orientation
        tondeuses[i].currentPosition()