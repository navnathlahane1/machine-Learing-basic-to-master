import pickle
import os 
class NN_model(object):
    def ___init__(self):
        path = os.getcwd() + "/model_exercise.pkl"
        file = open(path,"rb")
        self.model = pickle.load(file)

def predict(self,season,age,childish,trauma,surgical,fevers,alcohol,smoking,sitting):
    x =[[season,age, childish,trauma,surgical,fevers,alcohol,smoking,sitting]]
    return self.model.predict()