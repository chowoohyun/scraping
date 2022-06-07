import requests # request 모듈 import


# res = requests.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101')
# #naver에 접속하는 코드
#
# print(res.text)
#모든 웹 페이지에 접근이 가능한게아니다
#안되는경우, requests.exceptions.ConnectionError
#크롤링은 봇이 정보를 가져 오는것이기 때문에
#못들어 오게 막는 기능이 작동중
#웹 브라우져에서 접근 하느것 처럼 만들어주는것= 유저에이전트

#user-agent//http://www.useragentstring.com/
#naver에 접속하는 코드
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
hdata = {'User-Agent':agent}
res = requests.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101',headers=hdata)
#헤더를 지정해주면 내가 접속하는것 처럼 속일 수 있다.// 다른방법으론 클릭 값을 받아서 넣어주면 된다.
print(res.text)
#네이버 뉴스 경제 부분에서 에이전트를 바꿔서 접속 가능하게 한다.

