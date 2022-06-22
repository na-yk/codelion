import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

# file = open("cau.html","w") # 쓰기모드로 cau.html 파일 생성
# file.write(response.text) # file변수에 response.text 쓰기
# file.close() # 파일 닫기

# print(soup.title)   # title 태그
# print(soup.title.string)  # title 태그의 내용 - "중앙대학교"
# print(soup.span)    # 가장 상단에 있는 span 태그
# print(soup.findAll('span')) # 모든 span 태그

results = soup.findAll("a",{"class":"ellipsis mlog"})
print(results)
# for result in results:
#     print(result,"\n")