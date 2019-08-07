import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os

PATH = os.getcwd()
if PATH == '/home/rlawns324':
    PATH += '/projectDust_django'

# '&numOfRows= 를 24시간 * 7일 = 168 로 해야 지난 일주일 치 기록이 나옴. 0번 인덱스가 오늘 수치
def getpmGrade(stationName):
    url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'
    queryParams = '?' + 'ServiceKey=' + 'YMmMT2yHzdMM9M9nPSvQmLYIlLqIGRmwEa4cYOjF%2FgeLFqIsuwuhq2wZs%2BRKSKau3ZO2wTemglGfuGDR5b2JjQ%3D%3D'\
                    + '&numOfRows='+'168'\
                    +'&pageNo='+'1'\
                    +'&stationName='+stationName\
                    +'&dataTerm='+'MONTH'\
                    +'&ver='+'1.3'
    url1 = url + queryParams
    print(url1)
    r = requests.get(url1)
    print(r)
    # 정보를 수집해 올 페이지 로딩
    #chromedriver_loc = '/home/pirl/june/github/projectDust_django/projectDust/dust/chromedriver'
    chromedriver_loc = PATH + '/dust/chromedriver'
    driver = webdriver.Chrome(executable_path = chromedriver_loc)
    driver.get(url1)
    root = ET.fromstring(driver.page_source)
    pm10Grade = root.iter('pm10Grade')
    pm25Grade = root.iter('pm25Grade')
    pm10Grade_lastweek = []
    pm25Grade_lastweek = []
    for pm10_i in pm10Grade:
        temp = pm10_i.text
        pm10Grade_lastweek.append(temp)
    for pm25_i in pm25Grade:
        temp = pm25_i.text
        pm25Grade_lastweek.append(temp)
    return pm10Grade_lastweek, pm25Grade_lastweek


def getpmValue(stationName):
    url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'
    queryParams = '?' + 'ServiceKey=' + 'YMmMT2yHzdMM9M9nPSvQmLYIlLqIGRmwEa4cYOjF%2FgeLFqIsuwuhq2wZs%2BRKSKau3ZO2wTemglGfuGDR5b2JjQ%3D%3D'+'&numOfRows='+'168'+'&pageNo='+'1'+'&stationName='+stationName+'&dataTerm='+'MONTH'+'&ver='+'1.3'
    url1 = url + queryParams
    print(url1)
    r = requests.get(url1)
    print(r)
    # 정보를 수집해 올 페이지 로딩
    #chromedriver_loc = '/home/pirl/june/github//projectDust/dust/chromedriver'
    #Git에 올려놓고 거기서 가져와보기
    
    chromedriver_url = "https://raw.githubusercontent.com/rlawns324/projectDust_django/master/chromedriver"
    
    print(PATH + '/chromedriver')
    driver = webdriver.Chrome(executable_path = PATH + '/chromedriver')
    driver.get(url1)
    root = ET.fromstring(driver.page_source)
    pm10Value = root.iter('pm10Value')
    pm25Value = root.iter('pm25Value')
    pm10Value_lastweek = []
    pm25Value_lastweek = []
    for pm10_i in pm10Value:
        temp = pm10_i.text
        pm10Value_lastweek.append(temp)
    for pm25_i in pm25Value:
        temp = pm25_i.text
        pm25Value_lastweek.append(temp)
    return pm10Value_lastweek, pm25Value_lastweek
    print(pm10Value_lastweek)

getpmValue('중구')