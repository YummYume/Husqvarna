# Lire le fichier Tondeuses.txt
def readFile():
    # Ouvrir le fichier et le séparer ligne par ligne
    file = open("Tondeuses.txt", "r")
    file = file.read().splitlines()

    # Retirer les espaces blancs
    for f in range(len(file)):
        file[f] = file[f].strip()

    return file

# Main
if __name__ == "__main__":
    # Liste des lignes
    lines = readFile()
    # Première ligne = Coin supérieur droit
    topRightCorner = lines[0]
    # On retire la première ligne pour n'avoir que le format suivant : position | instruction
    del lines[0]
    # Liste des positions initiales
    initialPositions = []
    # Liste des instructions
    instructions = []

    # Construction des listes initialPositions et instructions
    i = 0
    for line in range(len(lines)):
        i += 1
        if (i == 1):
            initialPositions.append(lines[line])
        else:
            instructions.append(lines[line])
            i = 0

    print("Coin supérieur droit : ", topRightCorner)
    print("Positions initiales : ", initialPositions)
    print("Instructions : ", instructions)