import urllib.request
import urllib.error
import os
import socket

address = "https://www2.youku00.com/20180318/py4jw0QK/1000kb/hls/RG3jwOA8406108.jpeg"
num = 108
name = "015"


def getHtml(url):
    page = urllib.request.urlopen(url)
    result = page.read()
    return result


def downloadTS(url):
    print(url)
    file_name = "E:\\workspace\\download\\" + url[-8:]
    try:
        urllib.request.urlretrieve(url, file_name)
    except urllib.error.ContentTooShortError:
        print("reloading..." + url)
        downloadTS(url)


def covert(a):
    if a >= 100:
        return str(a)
    elif a >= 10:
        return "0" + str(a)
    else:
        return "00" + str(a)


def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)


socket.setdefaulttimeout(120)
del_file('E:\\workspace\\download\\')
for a in range(0, num + 1):
    url = address[0:-8] + covert(a) + ".jpeg"
    downloadTS(url)

# os.system("copy /b E:\workspace\download\*.ts E:\workspace\\" + name + ".ts")
