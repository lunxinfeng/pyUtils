import requests
import bs4
import re
import lxfUtils

r = requests.get("https://www.101weiqi.com/chessbook/chess/568482/")
soup = bs4.BeautifulSoup(r.text, "html.parser")
# lxfUtils.write(soup.prettify(), "zhubo1.html")
pattern = re.compile(r"var chessobj = {.*};")
result = soup.find_all("script", text=pattern)
# lxfUtils.write(str(result), "lxf.html")
for item in result:
    print(item)

print(pattern.search(result[0].text).group())
