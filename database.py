from cassandra.cluster import Cluster

def get_db():
    # connecting to cassandra
    cluster = Cluster()
    try:
        session = cluster.connect("movie_prediction")
        return session
    except:
        print "exception raised"


def insert_db(data):
    session = get_db()
    d = (int(data[0]), str(data[1]), int(data[2]), int(data[3]))
    session.execute("INSERT INTO users (id,name,rating,revenue) VALUES (%s,%s,%s,%s)", d)


def read_data_from_database():
    session = get_db()
    data = session.execute("SELECT * FROM USERS")
    return data

def delete_db(movie_id):
    session = get_db()
    session.execute("DELETE FROM USERS WHERE id= %s ", [movie_id])










