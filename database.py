from cassandra.cluster import Cluster

def get_db():
    # connecting to cassandra
    cluster = Cluster()
    session = cluster.connect("movie_prediction")
    return session


def insert_db(data):
    session = get_db()
    session.execute("INSERT INTO users (id,name,rating,revenue) VALUES (%s,%s,%s,%s)", (int(data[0]), str(data[1]), int(data[2]), int(data[3])))
    # cql = ("INSERT INTO users "
    # "(id,name,rating,revenue) "
    # "VALUES (%(id)s, %(name)s, %(rating)s, %(revenue)s)")
    #
    # d = {
    #     'id': int(data[0]),
    #     'name': str(data[1]),
    #     'rating': int(data[2]),
    #     'revenue': int(data[3]),
    #     }
    #
    # session.execute(cql, d)





