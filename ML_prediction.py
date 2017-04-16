import pickle

with open('static/Movie_Prediction_decisionTree.pkl', 'rb') as f:
    decision_Tree = pickle.load(f)

def predict(data):
    result = decision_Tree.predict([data[0], data[1]])
    return result



