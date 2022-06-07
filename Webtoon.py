#네이버 웹툰 스크래핑
#https://comic.naver.com/index
#인기급상승 웹툰, li, class= rank01 02
#ol id = realTimeRankFavorite, class =asideBoxRank

import requests
from bs4 import BeautifulSoup
import lxml


agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
hdata = {'User-Agent':agent}
res = requests.get('https://comic.naver.com/index',headers=hdata)

bs = BeautifulSoup(res.text, 'lxml')
#웹툰 페이지의 html을 text 형태로 저장
#가장 빠른 lxml형태로 설정

result = bs.find('ol', id = 'realTimeRankFavorite')
result1 = result.find_all('a')

webtoonlist = []
for tmp in result1:
    print(tmp.text)
    webtoonlist.append(tmp.text)

print(webtoonlist)