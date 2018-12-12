from datetime import datetime

import pandas as pd
import numpy as np
import math

class Data(pd.DataFrame):


    @property
    def _constructor(self):
        return Data



    def clean(self):
        self.Sex.replace(to_replace=dict(male=0, female=1), inplace=True)

        # zapelnienie pustych miejsc
        median_train_age = math.floor(self.Age.median())
        self.Age = self.Age.fillna(median_train_age)

        median_test_age = math.floor(self.Age.median())
        self.Age = self.Age.fillna(median_test_age)

        average_class = math.floor(np.mean(self.Pclass))
        self.Pclass = self.Pclass.fillna(average_class)

        median_parch = math.floor(self.Parch.median())
        self.Parch = self.Parch.fillna(median_parch)

        median_fare = math.floor(self.Fare.median())
        self.Fare = self.Fare.fillna(median_fare)

df=pd.read_csv("train.csv")
data=Data(df)
data.clean()


print(data)


