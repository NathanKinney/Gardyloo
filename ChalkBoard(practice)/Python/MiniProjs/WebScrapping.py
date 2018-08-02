import requests
import bs4
# res = requests.get('http://example.edu/')
# print(type(res))

# print(res.text)

# soup = bs4.BeautifulSoup(res.text, 'lxml')
# title_tag_list = soup.select('title')
# print(title_tag_list[0].getText())

# res = requests.get('https://en.wikipedia.org/wiki/Room_641A')
# soup = bs4.BeautifulSoup(res.text, 'lxml')
#
# headline_list = soup.select('.mw-headline')
# for item in headline_list:
#     print(item.getText())
# print(headline_list)

res = requests.get('https://en.wikipedia.org/wiki/Cicada_3301')
soup = bs4.BeautifulSoup(res.text, 'lxml')
image_info = soup.select('.thumbimage')
# print(type(image_info))
# print(len(image_info))
cicada = image_info[0]
# print(cicada['src'])
image_link = 'http:'+cicada['src']
# print(image_link)
cicada_image = requests.get(image_link, 'lxml')
# print(cicada_image.content)

f = open('cicada_image_new.jpg', 'wb')
print(f.write(cicada_image.content))
f.close()
