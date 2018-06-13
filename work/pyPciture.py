import urllib.request
from bs4 import BeautifulSoup

addressHome = 'https://www.ebay.com.au/itm/HPI-RACING-BAJA-5T-86610-HEAVY-DUTY-DRIVE-SHAFT-15X120MM-BAJA-5B-SILVER-2PCS/382370246684?hash=item59070af01c:g:~PsAAOSwXkNaaa5R'

page = urllib.request.urlopen(addressHome)
result = page.read()
soup = BeautifulSoup(result, 'html.parser')
img = soup.find("img", id="icImg")
imgUrl = img["src"]
print(imgUrl)
urllib.request.urlretrieve(imgUrl, "xyf.jpg")

# import urllib
# import re
#
#
# def getHtml(url):
#     page = urllib.urlopen(url)
#     html = page.read()
#     return html
#
#
# def getImg(html):
#     reg = r'src="(.+?\.jpg)" pic_ext'
#     imgre = re.compile(reg)
#     imglist = re.findall(imgre, html)
#     x = 0
#     for imgurl in imglist:
#         urllib.urlretrieve(imgurl, '%s.jpg' % x)
#         x += 1
#
#
# html = getHtml("https://tieba.baidu.com/p/5582243679")
# print(getImg(html))
