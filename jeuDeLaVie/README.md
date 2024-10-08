# pantheonDuCode
https://poc.onepantheon.fr/html/defi.html

# Jeu de la vie
- règles/wikis : 
  - https://fr.wikipedia.org/wiki/Jeu_de_la_vie
  - https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
  - https://conwaylife.com/wiki
  - https://conwaylife.com/wiki/Spaceship
- vidéos :
  - https://www.youtube.com/watch?v=S-W0NX97DB0 ((fractal à 16m15s))
  - https://www.youtube.com/watch?v=eMn43As24Bo


- fonctionnement du code :
  - display avec pygame
  - functionalities :
    - ajouter ou retirer une cell sur la map avec click gauche
    - click droit pour ouvrir le menu "d'outils" ; il contient :
      - Tout les pré-concus (changement de taille de map automatique pour éviter les erreurs / convenir au pré-concu)
      - save & load vos créations (selon la taille de la map, le programme rajoute automatiquement une 'extension' à la fin du nom de votre création save ; comme _100x100, qui signifie que cette création ne marche/peut être chargé que sur une map de 100x100)
        (entrer le nom du txt à charger ou sauvegarder dans 'txt name :' ; /!\ nommé un txt de la même mannière qu'un ancien txt et le save écrasera l'ancien (je n'ai pas voulu ajouté de sécuriter pour cela))
      - le on/off du mode 'detailed cell color' (cf https://fr.wikipedia.org/wiki/Jeu_de_la_vie pour le détails des couleurs) [affecte les performances sur les maps 500x500]
      - les switch manuels entre map de taille 100x100, 200x200 et 500x500 (pour donc vos créations, pouvoir les créer et les charger)
        (les changements de tailles de map réinitialise la map ; + passer sur une map 200x200 ou 500x500 enlèvera automatiquement la grille et les nombres des cases)
    - en haut à gauche il y a 3 infos : temps en secondes depuis le lancement du programme, la génération/itération actuelle, et la population total (nombre de cell vivantes) de la map.
    - les 4 boutons en haut à gauche, de gauche à droite, quand clicker servent à :
      - réinitialiser la map (supprimer toutes les cells + remise à 0 de génération + 'mise en pause')
      - revenir à la map initial, donc seulement si au moins 1 génération est passé (supprimer toutes les cells + remise à 0 de génération + 'mise en pause' + remet la map 'initial'/génération 0)
      - bouton run/pause (quand clické, fait alternativement : passe à l'itération suivante (xinf) jusqu'à 'mise en pause', et 'mise en pause')
        (il est aussi possible de mettre en pause en ajoutant une cellule sur la map pendant que ça run)
      - button next iteration (passe à l'itération suivante (x1))
    - les boutons en haut à droite servent à :
      - zoom et dezoom ; pour slider(/bouger de gauche à droite et de haute en bas), utilisez les flèches directionnelles du clavier
      - mode_grille ; pour changer entre les différentes types de grilles possibles [affecte beaucoup les performances]
      - mode_numbers ; pour activer ou désactiver les nombres des cases [n'affecte quasiment pas les performances]
      - go to center button, pour retourner au centre de la map
    - appuyer sur la touche échap à tout moment pour arrêter le programme
    + peut-être d'autres trucs que j'ai oublié de noté au dessus ; d'ailleurs n'hésitez à me dire les trucs à améliorer/que vous aimeriez
    

- instructions pour exécuter le projet :
  - run main.py dans votre IDE python (pycharm, vscode, etc.) ; 
[comment créait-on un exécutable ?] : https://www.youtube.com/watch?v=ufp4LJwJQUE
