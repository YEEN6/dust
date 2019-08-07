import pandas as pd
import joblib
import os
PATH = os.getcwd()


class ML_Model():
    def __init__(self):
        self.x_test = pd.DataFrame()

    def infer(self):
        self.model = joblib.load(PATH + '/data/finalized_model.sav')
        #일단 원래 있던 testset에서 7개만 배서 돌리고, 시간 여유 있으면 실시간 데이터 크롤링 해서 새로운 test set 만들기
        self.x_test = pd.read_pickle(PATH + '/data/temp_testset_week.pkl')
        self.y_pred = self.model.predict(self.x_test)