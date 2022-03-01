# 모듈을 읽어들입니다.
from urllib import request
from bs4 import BeautifulSoup

# urlopen() 함수로 기상청의 전국 날씨 읽어보기
target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

# BeautifulSoup을 사용해 웹 페이지 분석하기
soup = BeautifulSoup(target, "html.parser")

# location 태그 찾기
for location in soup.select("location"):
    # 내부의 city, wf, tmn, tmx 태그를 찾아 출력
    print("구분: ", location.select_one("province").string)
    print("도시: ", location.select_one("city").string)
    print("날씨: ", location.select_one("wf").string)
    print("최저 기온: ", location.select_one("tmn").string)
    print("최고 기온: ", location.select_one("tmx").string)
    print("일자: ", location.select_one("tmEf").string)
    print()