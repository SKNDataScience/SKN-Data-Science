import pandas as pd
from sklearn import linear_model
from sklearn.metrics import r2_score
import numpy as np
import math
from sklearn.model_selection import train_test_split


from scipy.stats.stats import pearsonr

#wczytanie danych
df_train=pd.read_csv("train.csv")
df_test=pd.read_csv("test.csv")
df_ver=pd.read_csv("gender_submission.csv")
# zamiana plci na liczby
df_train["Sex"].replace(to_replace=dict(male=0,female=1), inplace=True)
df_test["Sex"].replace(to_replace=dict(male=0,female=1), inplace=True)

#zapelnienie pustych miejsc
median_train_age=math.floor(df_train["Age"].median())
df_train["Age"]=df_train["Age"].fillna(median_train_age)

median_test_age=math.floor(df_test["Age"].median())
df_test["Age"]=df_test["Age"].fillna(median_test_age)

average_class=math.floor(np.mean(df_test["Pclass"]))
df_test["Pclass"]=df_test["Pclass"].fillna(average_class)

median_parch=math.floor(df_test["Parch"].median())
df_test["Parch"]=df_test["Parch"].fillna(median_parch)

median_fare=math.floor(df_test["Fare"].median())
df_test["Fare"]=df_test["Fare"].fillna(median_fare)

#deklaracja modelu regresji liniowej

reg=linear_model.LinearRegression()


#trenowanie modelu

X = df_train[['Pclass','Fare','Sex']]
y = df_train['Survived']

X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.2)


reg.fit(X_train,y_train)
#testowanie wspolczynnika determinacji

accuracy=reg.score(X_test,y_test)
print(accuracy)

reg.fit(X,y)
accuracy=reg.score(X,y)
print(accuracy)



# przewidywanie
predictions=reg.predict(df_test[['Pclass','Fare','Sex']])


for i in range(len(predictions)):
    if predictions[i]>0.5:
        predictions[i]=1

    else:
        predictions[i]=0


df_test['Survived']=predictions

print(df_test)

x=np.array(df_ver['Survived'])

index=0
for i in range(len(x)):
    if predictions[i]==x[i]:
        index+=1
    else:
        continue

print(index)
print(len(predictions))
#tabelka korelacji

pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', -1)
corr=df_train.corr()

print(corr)
