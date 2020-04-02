import re
import requests

def crawler(url):
    try:
        rer = requests.get(url)
    except requests.exceptions.RequestException as err:
        return err
    rer.encoding = rer.apparent_encoding
    pattern = re.compile('href="/en/vnl/2018/women/teams/.*?">(.*?)</a></figcaption>\s+</figure>\s+</td>\s+<td>(.*?)</td>\s+<td class="table-td-bold">(.*?)</td>\s+<td class="table-td-rightborder">(.*?)</td>')
    p = re.findall(pattern, rer.text)
    return p
    
if __name__ == "__main__":
    #the following lines will not be executed if the volleyballCrawlerParser is imported instead of executed
    #Please think of how this command can be utilised 
    #useful if you are building a lot of modules and have test codes- Dalin
    url = 'http://www.volleyball.world/en/vnl/2018/women/results-and-ranking/round1'
    result = crawler(url)
    print(result)