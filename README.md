# Movie-Prediction-Using-Decision-Tree


This project uses machine learning to predict if the movie is Excellent, Great, Good, Average and Worst using decision tr
ee.

Tech Stack:
1. Flask - pyhton web development framework
2. Python for machine learning
3. Cassandra - NoSql database for backend


Steps To Run Project :-
1. type 
	pip install -r requirements.txt
   this will install all the python packages required for the project.

2. open your cassandra treminal interface
	for linux :
		>sudo serivce cassandra start
		>cqlsh
	for windows :
		search cql in windows start button and open it.

3. create keyspace in cassandra and table
	> CREATE KEYSPACE movie_prediction
	  WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 3};

 	> create table users (
				id int,
				name text,
				rating int,	
				revenue int,
				primary key (id)
			     )
4. finally run the server by going to the project directory and type 
	python index.py

Now you are good to go ...
