from flask import Flask , render_template ,request
from database import insert_db
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/insert")
def insert():
    return render_template("insert.html")

@app.route("/insertmovie",methods=['POST'])
def insertmovie():
    # inserting the movies details in the cassandra database
    movie_id = request.form['mid']
    movie_name = request.form['mname'];
    movie_ratings = request.form['mratings']
    movie_revenue = request.form['mrevenue']
    data = [movie_id, movie_name, movie_ratings, movie_revenue]
    insert_db(data)
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)




