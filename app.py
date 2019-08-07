from flask import Flask, render_template, request, url_for, jsonify

from search.getLocation import get_location
from datetime import date, timedelta
import ml, pm

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def getLocationList():
    result = request.form['searchInput']
    print(result)
    response_data = get_location(result)

    return render_template('search-result.html', contents=response_data)


@app.route('/passParameter', methods=['POST'])
def passParameter():

    return render_template()

@app.route('/info')
def info():
    # 그래프 x축 날짜
    x_week = []
    varDate = date.today()
    for i in range(7):
        dmy = varDate.strftime("%Y.%m.%d")
        x_week.append(dmy)
        varDate += timedelta(days=1)

    # 이미 있던 데이터셋으로 모델 돌리기, 7개짜리 y 리스트(결과값) 생성
    model = ml.ML_Model()
    model.infer()
    y_pred = [int(i) for i in list(model.y_pred)]
    y_sum = sum(y_pred)

    # 오늘자 대기 정보
    today = date.today().strftime("%Y년 %m월 %d일")
    stationLoc = '대도동'
    g_pm10_list, g_pm25_list, v_pm10_list, v_pm25_list = pm.getpm_Grade_Value(stationLoc)
    v_pm10_today, v_pm25_today, g_pm10_today, g_pm25_today = v_pm10_list[0], v_pm25_list[0], g_pm10_list[0], \
                                                             g_pm25_list[0]

    return render_template('info.html', x_week = x_week, y_pred = y_pred, y_sum = y_sum, \
                           v_pm10_today=v_pm10_today, v_pm25_today=v_pm25_today,\
                           g_pm10_today=g_pm10_today, g_pm25_today=g_pm25_today,\
                           stationLoc=stationLoc, today=today
                           )


with app.test_request_context():
    print(url_for('index'))
    print(url_for('getLocationList'))
    print(url_for('passParameter'))
    print(url_for('info'))
