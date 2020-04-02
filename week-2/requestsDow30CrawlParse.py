import requests
import re
#requests for crwaler and re for parser 
def retrieve_dji_list():
    rer = requests.get('http://money.cnn.com/data/dow30/')
    #You need to look at the html first to determine the pattern
    search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span><\/td>\s+.*?class="wsod_stream">(.*?)<\/span>')
    dji_list_in_text = re.findall(search_pattern, rer.text)
    return dji_list_in_text

dji_list = retrieve_dji_list()
print(dji_list)