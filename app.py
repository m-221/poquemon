from flask import Flask, render_template, request, redirect, url_for, flash
import requests

API = "https://pokeapi.co/api/v2/pokemon/"
app = Flask(__name__)
app.secret_key = 'claVe_SeCReTa_My_ClAvE'


@app.route('/')
def index():
    return render_template('inicio.html')


@app.route('/pokemon')
def pokemon():
    return render_template('pokemon.html')


@app.route('/search', methods=['POST'])
def search_pokemon():
    pokemon = request.form.get('pokemon', '').strip().lower()  

    if not pokemon:
        flash('Por favor, ingresa tu información', 'error')
        return redirect(url_for('index'))

    try:
        respuesta = requests.get(f"{API}{pokemon}")
        if respuesta.status_code == 200:
            pokemon_data = respuesta.json()
            formatted_data = format_pokemon_data(pokemon_data)
            return render_template('pokemon.html', pokemon=formatted_data)
        else:
            flash('Pokémon no encontrado. Por favor, intenta de nuevo.', 'error')
            return redirect(url_for('pokemon'))

    except requests.exceptions.RequestException:
        flash('Error al conectar con la API. Por favor, intenta de nuevo más tarde.', 'error')
        return redirect(url_for('index'))


def format_pokemon_data(pokemon_data):
    return {
        'name': pokemon_data['name'].title(),
        'id': pokemon_data['id'],
        'height': pokemon_data['height'] / 10,  
        'weight': pokemon_data['weight'] / 10,  
        'sprite': pokemon_data['sprites']['front_default'],
        'types': [t['type']['name'].title() for t in pokemon_data['types']],
        'abilities': [a['ability']['name'].title() for a in pokemon_data['abilities']],
        'stats': {s['stat']['name']: s['base_stat'] for s in pokemon_data['stats']}
    }

if __name__ == '__main__':
    app.run(debug=True)