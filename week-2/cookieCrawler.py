import requests

url = 'https://www.amazon.co.uk/'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

c_headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
       'cookie': 'put your own cookie here' }


r_noheaders = requests.get(url)
print(r_noheaders.status_code)
with open('noheaders.html','bw') as f:
    f.write(r_noheaders.content)
    

r = requests.get(url,headers=headers)
print(r.status_code)
with open('nocookie.html','bw') as f:
    f.write(r.content)


r_cookies = requests.get(url,headers=c_headers)
print(r_cookies.status_code)
with open('cookie.html','bw') as f:
    f.write(r_cookies.content)
