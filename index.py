from flask import Flask , render_template ,request
from database import insert_db , read_data_from_database
from ML_prediction import predict
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

@app.route("/prediction")
def prediction():
    data = read_data_from_database()
    print type(data[0].id)
    print type(data[0].name)
    print type(data[0].rating)
    print type(data[0].revenue)
    result = list()
    for each_movie in data:
        res = predict([each_movie.rating, each_movie.revenue])
        result.append([each_movie.id, each_movie.name, each_movie.rating, each_movie.revenue, res])
    return render_template("prediction.html", data=result)


if __name__ == "__main__":
    app.run(debug=True)




