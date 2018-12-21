# import requests
# import bs4
# import re
# import lxfUtils

# r = requests.get("https://www.101weiqi.com/chessbook/chess/568482/")
# soup = bs4.BeautifulSoup(r.text, "html.parser")
# # lxfUtils.write(soup.prettify(), "zhubo1.html")
# pattern = re.compile(r"var chessobj = {.*};")
# result = soup.find_all("script", text=pattern)
# # lxfUtils.write(str(result), "lxf.html")
# for item in result:
#     print(item)
#
# print(pattern.search(result[0].text).group())


def Temperature(prob, T):
    result = [0] * len(prob)
    print([0])
    print(result)
    sum_prob = 0
    for i in range(len(prob)):
        t = p[i] ** (1 / T)
        result[i] = t
        sum_prob += t

    for i in range(len(result)):
        result[i] /= sum_prob

    return result


if __name__ == '__main__':
    p = [0.5, 0.3, 0.2]
    print(Temperature(p, 1))
    print(Temperature(p, 0.01))
    print(Temperature(p, 0.5))
    print(Temperature(p, 0.5))
