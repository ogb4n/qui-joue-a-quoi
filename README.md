<div align="center">

  <h3 align="center">Qui joue à quoi ?</h3>

_projet réalisé dans le cadre d'un cours sur la manipulation de données_ <br>
_language: python techstack: flask, tailwind_

  <p align="center">
    Site qui affiche les 10 jeux les plus joués sur steam et compare leur population à la population totale de steam
    <br />
  </p>
</div>

### Built With

- Python
- Flask
- TailwindCSS
- Matplotlib

<!-- GETTING STARTED -->

## Getting Started

Cloner le repo sur votre machine

Soyez sûr d'avoir python installé sur votre machine

### Installation

1. Cloner le repo

   ```sh
   git clone https://github.com/ogb4n/alpha_monit-app.git
   ```

2. Installer les packages python nécessaires

   ```sh
   pip install -r requirements.txt
   ```

   vous pouvez aussi créer un environnement virtuel et installer les packages dedans pour garder votre machine propre

3. Run the main.py file and go to http://localhost:5000/ to see the web interface

   ```sh
   python main.py
   ```

## A propos

Le site récupère les 10 jeux les plus joués actuellement sur steam et compare leur population à la population totale de joueurs dans un jeu steam. Les données sont récupérées via des requêtes et sont ensuite affichées sur le site. Le site est réalisé avec Flask et TailwindCSS pour le front-end. Les graphiques sont générés avec Matplotlib.
