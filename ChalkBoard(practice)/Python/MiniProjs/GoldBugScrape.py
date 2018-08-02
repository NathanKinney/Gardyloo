import bs4
import requests

res = requests.get('https://www.thegoldbugs.com/blog', 'lxml')
soup = bs4.BeautifulSoup(res.text, 'lxml')
blog = soup.select('pre')
text = blog[0]
blog_text = text.contents[0]
blog_lines = blog_text.split('-----')[1:]
result = ''

for sentence in blog_lines:
    result = result+sentence[0]

print(result)



