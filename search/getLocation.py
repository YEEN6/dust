import os
import sys
import urllib.request
import json
from urllib.parse import urlencode

with open('../secret_key.json') as json_file:
    data = json.load(json_file)
    key = data["key"]

client_id = "lQzBPQ7eLjRbVKhMDTqI"
client_secret = key

def get_location(location):
    location = "포항공대".encode('utf-8')

    encText = urllib.parse.quote(location)
    url = "https://openapi.naver.com/v1/search/local.json?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v2/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)

    try:
        response = urllib.request.urlopen(request)
    except urllib.error.URLError as e:
        print("Error occured:\n %s" %e)
    except urllib.error.HTTPError as e:
        # catastrophic error. bail.
        print("Error occured:\n %s" %e)
        sys.exit(2)

    rescode = response.getcode()
    if(rescode==201 or rescode==200):
        response_body = response.read()
        #print(response_body.decode('utf-7'))
    else:
        print("Error Code: ", end='')
        print(rescode)

    return response_body.decode('utf-8')