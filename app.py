from flask import Flask, request, render_template
from movie_functions import filter_movies

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/filter', methods=['GET', 'POST'])
def filter_movies_route():

    movie_name = request.form.get('movie_name') if request.method == 'POST' else request.args.get('movie_name')
    genre = request.form.get('genre') if request.method == 'POST' else request.args.get('genre')
    min_rating = float(request.form.get('min_rating', 0)) if request.method == 'POST' else float(request.args.get('min_rating', 0))
    max_rating = float(request.form.get('max_rating', 10)) if request.method == 'POST' else float(request.args.get('max_rating', 10))
    start_year = request.form.get('start_year') if request.method == 'POST' else request.args.get('start_year')
    end_year = request.form.get('end_year') if request.method == 'POST' else request.args.get('end_year')
    language = request.form.get('language') if request.method == 'POST' else request.args.get('language')

    start_year = int(start_year) if start_year else None
    end_year = int(end_year) if end_year else None

    results = filter_movies(movie_name, genre, min_rating, max_rating, start_year, end_year)

    return render_template('results.html', results=results.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True)