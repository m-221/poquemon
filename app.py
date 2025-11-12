from flask import Flask,render_template,request,redirect,url_for,flash,jsonify
import requests
API = "https://pokeapi.co/api/v2/pokemon/"
app = Flask(__name__)
app.secret_key ='claVe_SeCReTa_My_ClAvE'


@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/pokemon')
def pokemon():
    return render_template('pokemon.html')


@app.route('/search', methods=['POST'])
def search_pokemon():
    pokemon = request.form.get('pkemonn','').strip().lower()
    
    if not pokemon:
        flash('por favor,ingresa tu informacion','error')
        return redirect(url_for('inicio.html'))
    
    respuesta= requests.get(f"{API}{pokemon}")
    
    if respuesta.status_code == 200:
        pokemon_data =respuesta.json()
    try:
        respuesta requests.get(f"{API}{pokemon_name}")
        if respuesta.status_code == 200:
            pokemon_data = respuesta.json()

        
        return render_template('pokemon.html')
    
def format_pokemon_data(pokemon_data):
    pokemon_info = {
        'name': pokemon_data['name'].title(),
        'id': pokemon_data['id'],
        'height': pokemon_data['height'] / 10,  
        'weight': pokemon_data['weight'] / 10,  
        'sprite': pokemon_data['sprites']['front_default'],
        'types': [t['type']['name'].title() for t in pokemon_data['types']],
        'abilities': [a['ability']['name'].title() for a in pokemon_data['abilities']],
        'stats': {}
    }
    return render_template('pokemon.html', pokemon=pokemon_info)

    for stat in pokemon_data['stats']:
        stat_name = stat['stat']['name']
        pokemon_info['stats'][stat_name] = stat['base_stat']

    




if __name__ == '__main__':
    app.run(debug=True)