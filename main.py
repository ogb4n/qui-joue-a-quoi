from flask import Flask, render_template
import requests
import matplotlib.pyplot as plt
app = Flask(__name__)

COLORS = {
    0: [255, 255, 255],
    1: [228, 228, 228],
    2: [136, 136, 136],
    3: [34, 34, 34],
    4: [255, 167, 209],
    5: [229, 0, 0],
    6: [229, 149, 0],
    7: [160, 106, 66],
    8: [229, 217, 0],
    9: [148, 224, 68],
    10: [2, 190, 1],
    11: [0, 229, 240],
    12: [0, 131, 199],
    13: [0, 0, 234],
    14: [224, 74, 255],
    15: [130, 0, 128]
}


@app.route('/')
def index():
    response = requests.get('https://api.steambase.io/games?sortBy=players&sortDirection=1&skip=0&take=10')
    if response.status_code == 200:
        data = response.json()
        current_players_list = []
        playercount = 0
        game_name_list = []
                                # on récupère les données de chaque jeu
        for game in data:
            game_name_list.append(game['name'])
            current_players_list.append(game['current_players'])
            game_id = game['steam_app_id']
            playercount += game['current_players']


                                # on crée un graphique en barres
        plt.figure(figsize=(8, 6), facecolor='white', edgecolor='white')
        plt.bar(game_name_list, current_players_list, color=[(v[0]/255, v[1]/255, v[2]/255) for v in COLORS.values()])
        plt.ylabel('Nombre de joueurs (Millions)', color='white')
        plt.xticks(rotation=45, ha='right', color='white')
        plt.yticks(color='white')
        plt.tight_layout()

        plt.savefig('./static/bar_chart.png', transparent=True, edgecolor='white') 
            
                                    # on récupère le nombre total de joueurs connectés
        res = requests.get('https://store.steampowered.com/stats/userdata.json?days_back=3')
        data2 = res.json()
        online_players = data2[0]['data'][-1][1]

                                    # on crée un graphique en camembert
        plt.figure(figsize=(6, 4), facecolor='white', edgecolor='white')
        plt.pie([playercount, online_players - playercount], labels=['Joue à un jeu du top 10', 'Nombre total de connectés'], autopct='%1.1f%%', startangle=140, colors=['#4fb0ff', '#94e044'], labeldistance=0.8, textprops={'color': 'white'} )
        plt.axis('equal') 
        plt.tight_layout()

        plt.savefig('./static/pie_chart.png', transparent=True) 

        return render_template('index.html', games=data, online_players=online_players, playercount=playercount)
    else:
        return "Erreur lors de la récupération des données de l'API"
  
if __name__ == '__main__':
    app.run(debug=True, threaded=True) 