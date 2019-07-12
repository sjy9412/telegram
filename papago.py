import requests
import pprint
from decouple import config
# 1. 네이버 API
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')
# 2. URL 설정
naver_url = 'https://openapi.naver.com/v1/papago/n2mt'
# 3. 요청보내기 - POST
headers = {
    'X-Naver-Client-Id':naver_client_id,
    'X-Naver-Client-Secret':naver_client_secret
    }
data = {
    'source' : 'ko',
    'target' : 'en',
    'text' : '띵작'
    }
response = requests.post(naver_url, headers=headers, data=data).json()
pprint.pprint(response)
text = response.get('message').get('result').get('translatedText')
print(text)