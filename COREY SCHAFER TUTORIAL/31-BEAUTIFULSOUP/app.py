'''
pip install beautifulsoup4
pip install lxml
pip install html5lib
pip install requests
'''
import csv

from bs4 import BeautifulSoup
import requests
# with open('sample.html') as html_file:
#      soup=BeautifulSoup(html_file,'lxml')
# print(soup)
# print(soup.prettify())
# match=soup.title
# match=soup.title.text
# match=soup.div
'''class is a special keyword thats y we use class_'''
# match=soup.find('div',class_="footer")
# print(match)
# article=soup.find('div',class_="article")
# print(article)
'''find all returns a list'''
# for article in soup.find_all('div',class_="article"):
#     headline=article.h2.a
#     print(headline)
#     summary=article.p.text
#     print(summary)

source=requests.get('http://coreyms.com').text
soup=BeautifulSoup(source,'lxml')
# print(soup.prettify())
# article=soup.find('article')
# # print(article.text)
# # print(article.prettify())
# headline=article.h2.a.text
# # print(headline)
# summary=article.find('div',class_='entry-content').p.text
# # print(summary)
# vid_src=article.find('iframe',class_='youtube-player')['src']
# # print(vid_src)
# vid_id=vid_src.split('/')[4]
# vid_id=vid_id.split('?')[0]
# # print(vid_id)
# vid_lnk=f"http://youtube.com/watch?v={vid_id}"
# print(vid_lnk)
csv_file=open('details.csv','w')
csvwriter=csv.writer(csv_file)
csvwriter.writerow(['head','summar','link'])
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)
    summary = article.find('div', class_='entry-content').p.text
    print(summary)
    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        vid_lnk = f"http://youtube.com/watch?v={vid_id}"
    except Exception as e:
        vid_lnk=None
    print(vid_lnk)
    csvwriter.writerow([headline,summary,vid_lnk])
    print()
csv_file.close()
