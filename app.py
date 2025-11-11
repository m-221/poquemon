from flask import Flask,render_template,request,redirect,url_for,flash,requests,jsonify
API = "https://pokeapi.co/api/v2/pokemon/"
app = Flask(__name__)
app.secret_key ='claVe_SeCReTa_My_ClAvE'


@app.route('/')
def index():
    return render_template('inicio.html')


@app.route('/search', methods=['POST'])
def search_pokemon():
    pkemonn = request.form.get('pkemonn','').strip().lower()
    
    if not pkemonn:
        flash('por favor,ingresa tu informacion','error')
        return redirect(url_for('inicio.html'))
    
    repuesta= requests.get(f"{API}{pkemonn}")
    
    if respuesta.status_code == 200:
        pkemonn_data =respuesta_json()
        return render_template('inicio.html')
    




if __name__ == '__main__':
    app.run(debug=True)