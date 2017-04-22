from flask import Flask, render_template, request
from database import insert_db, read_data_from_database, delete_db
from ML_prediction import predict
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/insert")
def insert():
    return render_template("insert.html")

@app.route("/insertmovie", methods=['POST'])
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
    result = list()
    i = 0
    color_class = ["info", "danger", "warning", "active", "success"]
    for each_movie in data:
        res = predict([each_movie.rating, each_movie.revenue])
        result.append([each_movie.id, each_movie.name, each_movie.rating, each_movie.revenue, res, color_class[i % 5]])
        i = i + 1
    return render_template("prediction.html", data=result)


@app.route("/report")
def report():
    return render_template("report.html")

@app.route("/delete", methods=['POST'])
def delete():
    movie_id = request.form['mid']
    print type(movie_id)
    delete_db(int(movie_id))
    return prediction()

if __name__ == "__main__":
    app.run(debug=True)

