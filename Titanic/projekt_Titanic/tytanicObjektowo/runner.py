import pandas as pd

from tytanicObjektowo.Dane import Loader

sciezka = "tytanicObjektowo/train.csv"

loader = Loader(sciezka=sciezka)
loader.preprocess()


train_data, = loader.returnData()

