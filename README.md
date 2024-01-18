Voir le microgiciel ici :
- [github.com/cegep-electronique-programmable/gamepadArduino](https://github.com/cegep-electronique-programmable/gamepadArduino)

Procédure d’installation Python :

- Visiter https://www.python.org/downloads/
- Télécharger Python 3.12.1
- Installer avec l’installateur
  - Activer l’option Use admin privileges when installing py.exe
  - Activer l’option Add python.exe to PATH
  - A la fin de l’installation, cliquer sur Disable path length limit
- Ovrir une invite de commande Windows
- Taper :
  - py -m pip install pyautogui
  - py -m pip install pyserial
- Cliquer sur le fichier driver.py avec le bouton droit
- Choisir Edit with IDLE > Edit with IDLE 3.12 (64-bit)
- Connecter la manette
- Modifier le numéro de port COM
- Appuyer sur F5 pour rouler le programme.


Attention, s’assurer que le logiciel Arduino est fermé quand vous utilisez le driver pour ne pas avoir de conflits de connexion avec la manette

Attention, ne pas installer le package serial à la place de pyserial
