import pandas as pd
import numpy as np
import math


class Loader:

    def __init__(self, sciezka):
        self.dane = pd.read_csv(sciezka)



    def preprocess(self):

        # zamiana plci na liczby
        self.dane["Sex"].replace(to_replace=dict(male=0, female=1), inplace=True)

        # zapelnienie pustych miejsc
        median_train_age = math.floor(self.dane["Age"].median())
        self.dane["Age"] = self.dane["Age"].fillna(median_train_age)

        median_test_age = math.floor(self.dane["Age"].median())
        self.dane["Age"] = self.dane["Age"].fillna(median_test_age)

        average_class = math.floor(np.mean(self.dane["Pclass"]))
        self.dane["Pclass"] = self.dane["Pclass"].fillna(average_class)

        median_parch = math.floor(self.dane["Parch"].median())
        self.dane["Parch"] = self.dane["Parch"].fillna(median_parch)

        median_fare = math.floor(self.dane["Fare"].median())
        self.dane["Fare"] = self.dane["Fare"].fillna(median_fare)


    def printData(self):
        print(dane)

loader =  Loader()
Loader.printData()