import requests
import re as regex

userAgent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'
cookie = 'FastAB=0=9080,1=0600,2=4988,3=1540,4=3343,5=0603,6=6072,7=0892,8=3168,9=8062; tryThing01=3956; OptanonConsent=landingPath=https%3A%2F%2Fmoney.cnn.com%2Fdata%2Fdow30%2F&datestamp=Wed+Jan+29+2020+11%3A36%3A22+GMT%2B0000+(Greenwich+Mean+Time)&version=5.11.0&groups=0_73737%3A1%2C0_73761%3A1%2C0_73764%3A1%2C0_37173%3A1%2C107%3A1%2C116%3A1%2C124%3A1%2C133%3A1%2Creq%3A1%2Csm%3A0%2Csmv%3A0%2CBG139%3A0%2Cad%3A0%2Cadv%3A0%2CBG137%3A0%2Cpf%3A0%2Cpfv%3A0%2CBG138%3A0%2Cpzv%3A0%2Cpz%3A0%2CBG140%3A0%2Cbb%3A0%2Cbbv%3A0%2CBG141%3A0%2Csa%3A0%2Csav%3A0%2CBG136%3A0&consentId=57190593-64e6-4cc9-aae5-60725aafbf22&AwaitingReconsent=true&EU=true&geolocation=&isIABGlobal=true; OptanonAlertBoxClosed=2019-10-21T11:18:43.913Z; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%22f0cf76fa-c768-42aa-83ca-41597dcf7248%22; s_fid=259C99E5BF5D3CDC-298035D76E77ADA3; SelectedEdition=edition; countryCode=GB; geoData=southampton|STH|so16 7qf|GB|EU|0|broadband; OptanonControl=ccc=GB&otvers=5.11.0&reg=gdpr&pctm=Mon Oct 21 2019 12:18:43 GMT+0100 (British Summer Time)&vers=1.4.3; cnprevpage_pn=mny%3Ao%3Amoney%3A%2Fdata%2Fdow30%2F; s_ppv=44'

req = requests.get('https://money.cnn.com/data/dow30/', headers={'User-Agent': userAgent, 'Cookie': cookie})
searchPattern = regex.compile('class="wsod_symbol">(.*?)</a>.*?<span.*?">(.*?)</span></td>\s+.*?class="wsod_stream">(.*?)</span>')

data = {}
for line in regex.findall(searchPattern, req.text):
  data[line[0]] = {'Full Name': line[1], 'Dow Score': line[2]}

print(data)

def writeDowToCsv(dowScores):
  with open('dow30-stats.csv', 'w') as output:
    output.write('acronym,name,score\n')
    for company in dowScores:
      output.write("{0},{1},{2}\n".format(company[0], company[1], company[2]))