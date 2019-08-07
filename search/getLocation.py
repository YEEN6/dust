import os
import sys
import urllib.request
import json
import ast
import pprint

from urllib.parse import urlencode



def call_location_api(location):
    document_path = os.getcwd() + '/search/secret_key.json'

    with open(document_path) as json_file:
        data = json.load(json_file)
        key = data["key"]

    # please put your naver api clinet_is and client_secret
    client_id = "lQzBPQ7eLjRbVKhMDTqI"
    client_secret = key

    encText = urllib.parse.quote(location)
    url = "https://openapi.naver.com/v1/search/local.json?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/local.xml?query=" + encText # xml 결과
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
    else:
        print("Error Code: ", end='')
        print(rescode)

    return response_body.decode('utf-8')


def get_location(location):
    response_data = call_location_api(location)

    data = json.loads(response_data)
    contents = data['items']

    # data = ast.literal_eval(response_data)
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(data)

    result_data = []

    for content in contents:
        temp = {}
        content['title'] = content['title'].replace("<b>", "").replace("</b>", "")
        print(content['title'])
        temp['title'] = content['title']
        temp['address'] = content['address']
        result_data.append(temp)

    return result_data
