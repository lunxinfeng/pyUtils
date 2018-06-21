import urllib.request
import urllib.error
import os
import socket

address = "https://www2.youku00.com/20180318/py4jw0QK/1000kb/hls/RG3jwOA8406000.ts"
down_path = r"E:\workspace\download\\"
num = 108
name = "015"


def get_html(url: str):
    page = urllib.request.urlopen(url)
    result = page.read()
    return result


def download_ts(url: str):
    print(url)
    file_name = "E:\\workspace\\download\\" + url[-6:]
    try:
        urllib.request.urlretrieve(url, file_name)
    except urllib.error.ContentTooShortError:
        print("reloading..." + url)
        download_ts(url)


def covert(s: int):
    if s >= 100:
        return str(s)
    elif s >= 10:
        return "0" + str(s)
    else:
        return "00" + str(s)


def del_file(path: str):
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
    url = address[0:-6] + covert(a) + ".ts"
    download_ts(url)

os.system("copy /b E:\workspace\download\*.ts E:\workspace\\" + name + ".ts")
