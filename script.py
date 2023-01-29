#!/bin/bash


# importer les bibliothèques qu'on a besoin
import os
import sys
import ast
import subprocess

#La fonction pull

# définir la variable de dossier github
url = "https://github.com/MouAyo/TP-Scripting.git"

# définir la fonction pull pour télécharger un dossier du github 
def pull(url, path):
    # vérifier si le dossier est deja telecharger
    if os.path.exists(path):
        # si le dossier existe déjà, il faut le supprimer
        subprocess.call(["rm", "-rf", path])
    # si le dossier n'existe pas, on le telecharge du git
    subprocess.call(["git", "clone", url, path])


if __name__ == "__main__":
    # obtenir l'URL et le chemin du dossier à télécharger
    url = sys.argv[1]
    path = sys.argv[2]
    # appeler la fonction pour télécharger le dossier
    pull(url, path)

# La fonction build 

# définirla racine du dossier github
racine = os.path.join(url, "root")

# chercher le fichier python dans le dossier github
for dossier, sous_dossiers, fichiers in os.walk(racine):
  for fichier in fichiers:
    # si le fichier est un fichier python, exécutez la fonction build
    if fichier.endswith(".py"):
      os.system("python " + os.path.join(dossier, fichier) + " build")


#La fonction test 


# Définir la fonction pour tester le fichier
def test_file(fichier):
    # Vérifier si le fichier existe
    if not os.path.exists(fichier):
        print('Le fichier n\'existe pas.')
        return

    # Essayer de lire le fichier
    try:

        with open(fichier, 'r') as f:
            contenu = f.read()
    except:
        print('Impossible de lire le fichier.')
        return

    # Essayer de le parser
    try:
        tree = ast.parse(contenu)
    except SyntaxError as err:
        print('Le fichier est incorrect : {}'.format(err))
        return

    # Si aucune exception n'est trouver, le fichier est correct
    print('Le fichier est correct.')

# il faut executer la fonction test pour ajouter le nouveau fichier sur successful ou failed

# la commande run
cmd1 = "bash testFailed.sh"
cmd2 = "bash testSuccessful.sh"

# si le test est validé
result = subprocess.run(cmd2, shell=True, capture_output=True)

# si le test n'est pas validé
result = subprocess.run(cmd1, shell=True, capture_output=True)

# ecrire le output

print(result.stdout.decode())