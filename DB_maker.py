import requests
from bs4 import BeautifulSoup as bs
import datetime

'''
# 웹사이트에서 이름, URL 가져오기
url = 'https://famouspeople.astro-seek.com/filter_death/?umrti_den=nezalezi&umrti_mesic=nezalezi&umrti_rok=&pricina_umrti=&pohlavi=&razeni='
page = requests.get(url)
html = page.text
soup = bs(html, 'lxml')

name_full_list = []
url_full_list = []

name_list = soup.select('td.w300_p5 > a > span > strong')
url_list = soup.select('td.w300_p5 > a')

for name in name_list:
    name_full_list.append(name.text)

for url in url_list:
    url_full_list.append(url.get('href'))


#for url in url_full_list:
'''
# 세부 사이트로 들어가서 행성 정보 받아오기
url2 = 'https://birthcharts.astro-seek.com/birth-chart/christopher-reeve-horoscope'
horoscope = requests.get(url2)
html = horoscope.text
soup = bs(html, 'lxml')

data = [] #name, birthdate, death, cause, occupation, sun, moon, mercury, venus, mars, jupiter, saturn
name = soup.select('body > div.main-nad-envelope > div.main-envelope > div.main-web > div.stredni-menu > div.obsah > div.obsah-uvod > div.obsah-vnitrek > div.detail-info > h2')[0].text.replace('\n', '')
birthdate = soup.select('body > div.main-nad-envelope > div.main-envelope > div.main-web > div.stredni-menu > div.obsah > div.obsah-uvod > div.obsah-vnitrek > div.detail-info > div:nth-of-type(2) > div:nth-of-type(5)')[0].text.strip().replace("\n", '')
birth_convert = datetime.datetime.strptime(birthdate.replace('h',''), "%d %B %Y - %H:%M")
death = soup.select('body > div.main-nad-envelope > div.main-envelope > div.main-web > div.stredni-menu > div.obsah > div.obsah-uvod > div.obsah-vnitrek > div.detail-info > div:nth-of-type(7) > div:nth-of-type(2) > a')[0].text
death_convert = datetime.datetime.strptime(death, '%d %B %Y')
cause = soup.select('body > div.main-nad-envelope > div.main-envelope > div.main-web > div.stredni-menu > div.obsah > div.obsah-uvod > div.obsah-vnitrek > div.detail-info > div:nth-of-type(7) > div:nth-of-type(2) > span > a')[0].text
occupation = soup.select('body > div.main-nad-envelope > div.main-envelope > div.main-web > div.stredni-menu > div.obsah > div.obsah-uvod > div.obsah-vnitrek > div.detail-info > div:nth-of-type(11) > div:nth-of-type(2)')[0].text.strip()


#행성별 숫자 가져오기 : 행성에 따라 확인할 필요 있음

sign = {'aries' : 0.00, 'taurus' : 30.00, 'gemini' : 60.00, 'cancer' : 90.00, 'leo' : 120.00, 'virgo' : 150.00, 'libra' : 180.00, 'scorpio' : 210.00, 'sagittarius' : 240.00, 'capricorn' : 270.00, 'aquarius' : 300.00, 'pisces' : 330.00}

def get_degree(symbol):
    for name in sign:
        if name in symbol[0].get('src'):
            degree = sign[name]
        else:
            pass
    return degree


sun_symbol = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(4) > img')
sun_degree0 = get_degree(sun_symbol)
sun_degree1 = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(5) > span')[2].text
sun_degree2 = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(5) > span')[3].text

moon_symbol = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(10) > img')
moon_degree0 = get_degree(moon_symbol)
moon_degree1 = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(11) > span:nth-of-type(1)')[0].text
moon_degree2 = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(11) > span:nth-of-type(2)')[0].text

merc_symbol = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(16) > img')
merc_degree0 = get_degree(merc_symbol)
merc_degree1 = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(17) > span')[2].text
merc_degree2 = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(17) > span')[3].text

ven_symbol = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(22) > img')
ven_degree0 = get_degree(ven_symbol)
ven_degree1 = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(23) > span')[0].text
ven_degree2 = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(23) > span')[1].text

mars_symbol = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(28) > img')
mars_degree0 = get_degree(mars_symbol)
mars_degree1 = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(29) > span')[0].text
mars_degree2 = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(29) > span')[1].text

jup_symbol = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(34) > img')
jup_degree0 = get_degree(jup_symbol)
jup_degree1 = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(35) > span')[0].text
jup_degree2 = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(35) > span')[1].text

sat_symbol = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(40) > img')
sat_degree0 = get_degree(sat_symbol)
sat_degree1 = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(41) > span')[0].text
sat_degree2 = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(41) > span')[1].text

#문자열 수정 및 숫자로 변환
sun = float((sun_degree1 + '.' + sun_degree2).replace("’","")) + sun_degree0
moon = float((moon_degree1 + '.' + moon_degree2).replace("’","")) + moon_degree0
merc = float((merc_degree1 + '.' + merc_degree2).replace("’","")) + merc_degree0
ven = float((ven_degree1 + '.' + ven_degree2).replace("’","")) + ven_degree0
mars = float((mars_degree1 + '.' + mars_degree2).replace("’","")) + mars_degree0
jup = float((jup_degree1 + '.' + jup_degree2).replace("’","")) + jup_degree0
sat = float((sat_degree1 + '.' + sat_degree2).replace("’","")) + sat_degree0


#data 리스트에 정보 입력하기
input_lists = (name, birth_convert, death_convert, cause, occupation, sun, moon, merc, ven, mars, jup, sat)
for input in input_lists:
    data.append(input)



