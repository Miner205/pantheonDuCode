# pantheonDuCode
https://poc.onepantheon.fr/html/rules.html

# Jeu du Plus ou Moins
- règles : le code choisit un nombre dans un certain intervalle, et ensuite l'utilisateur doit deviner ce nombre ;
chaque fois qu'il essaye mais ne trouve pas le nombre, le code lui dit si le nombre à deviner,
c'est plus ou c'est moins.


- fonctionnement du code :
  - display avec pygame
  - tout d'abord choisir les bornes min et max de l'intervalle du nombre à trouver
; pour confirmer les bornes rentré, appuyer sur enter/return (en ayant sélectionner la zone d'une des deux bornes = clicker dessus = cadre jaune)
; quand les bornes sont confirmer, le nombre mystère est changé et le compteur d'essais remis à 0.
    (Normalement j'ai réglé tous les bugs lié à ce changement de bornes "dynamique" mais prévenez moi si vous en trouvez un.)
  - pour entrer un nombre, clickez sur la zone correspondante, et pour envoyez le nombre sur la touche enter ;
les inputs claviers acceptés sont les chiffres, le -, enter/return et backspace (input sécuriser).
  - faire echap ou fermer la fenêtre à tout moment arrêtera le programme.


- instructions pour exécuter le projet :
  - pour apprécier ma douce voix, monter le son de votre ordinateur (vers 25%).
  - run main.py dans votre IDE python (pycharm, vscode, etc.) ; [comment créait-on un exécutable ?].
