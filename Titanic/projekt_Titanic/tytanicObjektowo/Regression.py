import numpy as np
import pandas as pd


class Regression:

    def __init__(self,fit_intercept=True):
        self.coef=None
        self.intercept=None
        self._fit_intercept=fit_intercept

    # def fit(self):
