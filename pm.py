import requests
from bs4 import BeautifulSoup
import re

def convertGrade(status):
    status = re.findall(r'\d+|-',status)[1]
    if status == '1':
        status = '좋음'
    elif status == '2':
        status = '보통'
    elif status == '3':
        status = '나쁨'
    elif status == '4':
        status = '매우나쁨'
    else:
        status = '-'
    return status

def convertPmValue(value):
    value = re.findall(r'\d+|-',value)[1]
    value = 0 if value == '-' else int(value)
    return value

# '&numOfRows= 를 24시간 * 7일 = 168 로 해야 지난 일주일 치 기록이 나옴. 0번 인덱스가 오늘 수치
def getpm_Grade_Value(stationName):
    url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'
    queryParams = '?' + 'ServiceKey=' + 'YMmMT2yHzdMM9M9nPSvQmLYIlLqIGRmwEa4cYOjF%2FgeLFqIsuwuhq2wZs%2BRKSKau3ZO2wTemglGfuGDR5b2JjQ%3D%3D'\
                    +'&numOfRows='+'168'\
                    +'&pageNo='+'1'\
                    +'&stationName='+stationName\
                    +'&dataTerm='+'MONTH'\
                    +'&ver='+'1.3'
    url1 = url + queryParams
    r = requests.get(url1)
    soup = BeautifulSoup(r.text,'lxml')

    pm10Value_lastweek = [convertPmValue(i) for i in str(soup.findAll('pm10value')).split(',')]
    pm25Value_lastweek = [convertPmValue(i) for i in str(soup.findAll('pm25value')).split(',')]
    pm10Grade_lastweek = [convertGrade(i) for i in str(soup.findAll('pm10grade')).split(',')]
    pm25Grade_lastweek = [convertGrade(i) for i in str(soup.findAll('pm25grade')).split(',')]

    return pm10Grade_lastweek, pm25Grade_lastweek, pm10Value_lastweek, pm25Value_lastweek
#Test code
#getpmValue('중구')