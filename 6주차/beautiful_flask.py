# 모듈 읽기
from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

# 웹 서버 생성 & route 설정
app = Flask(__name__)
@app.route("/")

def hello():
    # urlopen() 함수로 기상청의 전국 날씨 읽기
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

    # BeautifulSoup을 사용해 웹 페이지 분석하기
    soup = BeautifulSoup(target, "html.parser")

    # location 태그 찾기
    # output 변수 선언
    output = ""
    for location in soup.select("location"):
        # 내부의 province, city, wf, tmn, tmx 태그를 찾아 출력
        # 지역 구분을 h3로, 각 도시들은 h4로 나타냄
        # 날씨, 최저, 최고기온을 표시해주고 hr(줄)을 이용하여 다음 출력 내용과 구분
        output += "<div style='width: 30%;background: #eee;padding-left: 30px;'>"
        output += "<h3>{}</h3>".format(location.select_one("province").string)
        output += "<h4>{}</h4>".format(location.select_one("city").string)
        output += "날씨: {}<br/>".format(location.select_one("wf").string)
        output += "최저/최고 기온: {}/ {}"\
            .format(\
                location.select_one("tmn").string,\
                location.select_one("tmx").string\
            )
        output += "</div>"
        output += "<hr/>"
    return output
app.run()