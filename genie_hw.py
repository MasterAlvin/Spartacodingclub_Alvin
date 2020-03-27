import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
# 웹에서 copy = copy selector #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
rank = 1

for music in musics:
    # movie 안에 a 가 있으면,
    a_tag = music.select_one('td.info')
# #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
    if a_tag is not None:
        # a의 text를 찍어본다.
        title = a_tag.text
        singer = music.select_one("td.info > a.artist.ellipsis").text

        print (rank, title, singer)
        rank += 1