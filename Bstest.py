#뷰티풀 숩4
#HTML XML JSON 등의 구문을 분석하는데 사용되는 모듈
#다양한 paser 다양한 특징들이 있다.

from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html>
<head>
 <title>BeautifulSoup</title>
</head>
<body>
 <div>
   <p>사과1</p>
   <p>사과2</p>
 </div>
 <div class="ex_class">
   <p>딸기1</p>
   <p>딸기2</p>
 </div>
 <div id="ex_id">
   <p>포도1</p>
 </div>
 <a href='http://www.naver.com' class='ex_link'>네이버 바로가기</a>
</body>
</html>
"""

bs = BeautifulSoup(html,'html.parser')
# print(bs)

#사과1 이라는 것을 찾고 싶으면 태크를 먼저 확인

# result = bs.find('p')
# #첫번째 p가 result 값으로 저장
# result2 = bs.find('div')
# #첫번째 div가 저장
# print(result)
# print(result2)

#모든 tag를 검색
# result = bs.find_all('p')
# # print(result)
#
# for tmp in result:
#     print(tmp.text)
    #.text = 문자만

#딸기만 가져 오고 싶다.
#div로 시작하지만 클래스 네임이 다르다
result = bs.find('div',class_='ex_class')
result1 = result.find_all('p')
# print(result1)

result = bs.find('div',id='ex_id')


result = bs.find('a',class_='ex_link')
result1 = result.get('href')
print(result1)

