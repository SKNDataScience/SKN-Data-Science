import pandas as pd
import numpy as np
import math


class Dane:

    def __init__(self):
        self.Dane=pd.read_csv(input("podaj nazwe danych"))



    def clean(self):


        # zamiana plci na liczby
        Dane.Sex.replace(to_replace=dict(male=0, female=1), inplace=True)


        # zapelnienie pustych miejsc
        median_train_age = math.floor(Dane.Age.median())
        Dane.Age = Dane.Age.fillna(median_train_age)

        median_test_age = math.floor(Dane.Age.median())
        Dane.Age = Dane.Age.fillna(median_test_age)

        average_class = math.floor(np.mean(Dane.Pclass))
        Dane.Pclass = Dane.Pclass.fillna(average_class)

        median_parch = math.floor(Dane.Parch.median())
        Dane.Parch = Dane.Parch.fillna(median_parch)

        median_fare = math.floor(Dane.Fare.median())
        Dane.Fare = Dane.Fare.fillna(median_fare)


    def print(self):
        print(Dane)

dane=Dane()
dane.print()