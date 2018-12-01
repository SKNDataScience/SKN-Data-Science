
import pandas as pd
from sklearn import linear_model
import numpy as np
import math
from scipy.stats.stats import pearsonr

#Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare

df_train=pd.read_csv("train.csv")
# median_sibsp=math.floor(df_train.SibSp.median())
# df_train.Age=df_train.Age.fillna(median_age)
df_train.Sex.replace(to_replace=dict(male=1,female=2), inplace=True)

pclass=df_train['Pclass']
sex=df_train['Sex']
age=df_train['Age']
sibsp=df_train['SibSp']
parch=df_train['Parch']
fare=df_train['Fare']
survived=df_train['Survived']
#
# pclass.append(df_train.Pclass)
# survived.append(df_train.Survived)
# sex.append(df_train.Sex)
# age.append(df_train.Age)
# sibsp.append(df_train.SibSp)
# parch.append(df_train.Parch)
# fare.append(df_train.Fare)
#
# print(np.multiarray.correlate(sex,survived))

print(pearsonr(pclass,survived))
print(pearsonr(sex,survived))
print(pearsonr(age,survived))
print(pearsonr(sibsp,survived))
print(pearsonr(parch,survived))
print(pearsonr(fare,survived))