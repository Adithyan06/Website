from flask import Flask, jsonify, render_template

import sqlite3

app = Flask(__name__, template_folder='/storage/emulated/0/templates/index.html')

@app.route('/')

def index():

    return render_template('/storage/emulated/0/templates/index.html')

@app.route('/movies')

def get_movies():

    conn = sqlite3.connect('movies.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM movies')

    movies = cursor.fetchall()

    conn.close()

    return jsonify(movies)

if __name__ == '__main__':

    app.run()
