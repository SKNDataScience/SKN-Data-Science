import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder

#TODO pomoc https://gist.github.com/ralphbean/4c2d4105ea2c7e407fb5
# https://machinelearningmastery.com/prepare-text-data-machine-learning-scikit-learn/
# https://www.analyticsvidhya.com/blog/2018/02/the-different-methods-deal-text-data-predictive-python/
# http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html

#TODO Rozwiązanie
#Rozwiązanie https://www.kaggle.com/mjidiba/a-beginner-s-guide-to-his-first-kaggle-project?scriptVersionId=6202347

x_test = pd.read_csv("data/test.csv")
x_train = pd.read_csv("data/train.csv")
x_test.pop("Id")
x_train.pop("Id")
y_train = x_train.pop("SalePrice")

# print(x_train.shape , x_test.shape, y_train.shape)


# Kodowanie klas z podziałem na liczby i treści
dict_numb = {"MSSubClass": -1000, "LotFrontage": -1000 , "LotArea": -1000, "OverallQual": -1000, "OverallCond": -1000, "YearBuilt": -1000, "YearRemodAdd": -1000, "MasVnrArea": -1000, "BsmtFinSF1": -1000, "BsmtFinSF2": -1000, "BsmtUnfSF": -1000, "TotalBsmtSF":-1000, "1stFlrSF": -1000, "2ndFlrSF": -1000, "LowQualFinSF": -1000, "GrLivArea": -1000, "BsmtFullBath": -1000, "BsmtHalfBath": -1000, "FullBath": -1000, "HalfBath": -1000, "BedroomAbvGr": -1000, "KitchenAbvGr": -1000, "TotRmsAbvGrd": -1000, "Fireplaces": -1000,  "Fireplaces": -1000, "GarageCars": -1000, "GarageArea": -1000, "WoodDeckSF": -1000, "OpenPorchSF": -1000, "EnclosedPorch": -1000, "3SsnPorch": -1000, "ScreenPorch": -1000, "PoolArea": -1000, "MiscVal": -1000, "MoSold": -1000, "YrSold": -1000,}
# Treściowe - stringami
# dict_text = {"Alley": "nwdm", "MSZoning": "nwdm", ""}

# x_train = x_train.fillna(value=dict_numb)
# x_train = x_train.fillna("niewiadomo")


#ENCODING DATA
# ordinal_encoder = OrdinalEncoder()
# ordinal_encoder.fit(x_train)
# print(ordinal_encoder.fit(x_train))

#LABEL ENCODER
# label_encoder = LabelEncoder()
# label_encoder.fit(x_train["Alley"])
# a= label_encoder.transform(x_train["Alley"])

# X_train, X_test, y_train, y_test = \
#         train_test_split(x_train, y_train, test_size=0.25, random_state=0)



