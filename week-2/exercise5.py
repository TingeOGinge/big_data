import requests
from bs4 import BeautifulSoup as bs

# url = 'https://www.volleyball.world/en/vnl/2018/women/results-and-ranking/round1'
#
# cookie = 'vnl2018#lang=en; Language=en; SC_ANALYTICS_GLOBAL_COOKIE=a8bb0e0745414ca5971fb626b204d621|False; ASP.NET_SessionId=tc5qcdmolcug3lcs0ocv3sc5'

# req = requests.get(url, headers={'user-agent': userAgent, 'cookie': cookie})
# pattern = re.compile('href="/en/vnl/2018/women/teams/.*?">(.*?)</a></figcaption>\s+</figure>\s+</td>\s+<td>(.*?)</td>\s+<td class="table-td-bold">(.*?)</td>\s+<td class="table-td-rightborder">(.*?)</td>')

# try:
#   with open('volleyballOutput.csv', 'w') as output:
#     output.write('acronym,played,won,lost\n')
#     for team in re.findall(pattern, req.text):
#       output.write(f"{team[0]},{team[1]},{team[2]},{team[3]}\n")
#     output.close()
#     print("Success")
# except Exception as err:
#   print(err)



def calculateTotalCookTime(array):
  return int(array[0]) if array[1] == 'minutes' else int(array[0]) * 60 + int(array[2])

def extractJamieRecipe(url):
  userAgent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'
  cookie = 'euconsent=BOvHJckOvHJckEDABBENC-AAAAAuiAAA; CookieControl={"necessaryCookies":["CookieControl","JSESSIONID","PHPSESSID","blaize_session","blaize_tracking_id","jo_user_login3","forgotten-password-redirect"],"optionalCookies":{},"initialState":{"type":"closed"},"statement":{"shown":true,"updated":"04/09/2018"},"consentDate":1565015422168,"consentExpiry":365,"interactedWith":true,"user":"E666985F-3A6A-47B2-BAB8-295E3B315D55"}'
  req = requests.get(url, headers={'user-agent': userAgent, 'cookie': cookie})
  
  recipe = {}
  
  soup = bs(req.text, features="html.parser")
  recipe['name'] = soup.title.text.split(' | ')[0].title()
  recipe['serves'] = int(soup("div", {"class": "recipe-detail serves"})[0].contents[2].strip())
  timeString = soup("div", {"class": "recipe-detail time"})[0].contents[2].strip()
  recipe['time'] = calculateTotalCookTime(timeString.split())
  recipe['calories'] = soup.select('li[title="Calories"] > div > span[class="top"]')[0].contents[0].strip()
  recipe['method'] = [steps.contents[0].strip() for steps in soup.select('ol[class="recipeSteps"] > li')]
  recipe['ingredients'] = [" ".join(ingredient.text.split()) for ingredient in soup.select('ul[class="ingred-list"] > li')]
  
  print(recipe)


extractJamieRecipe("https://www.jamieoliver.com/recipes/chicken-recipes/roast-tikka-chicken/")


# try:
#   with open('recipe-scraper-test.csv', 'w') as output:
#     output.write('dietary restrictions\n')
#     for restrictions
# except Exception as err:
#   print(err)