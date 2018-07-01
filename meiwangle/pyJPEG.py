import urllib.request
import urllib.error
import os
import socket
import time

address = "https://www2.youku00.com/20180318/FHUvAKei/1000kb/hls/wOH6s1229000.jpeg"
file_type = ".jpeg"
num = 258
start = 0
name = "031"


def get_html(url: str):
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    page = urllib.request.urlopen(url, headers=headers)
    result = page.read()
    page.close()
    return result


def download_ts(url: str, index: int):
    print(url)
    if num >= 1000:
        if index < 1000:
            file_name = "0" + url[-(file_type.__len__() + 3):]
        else:
            file_name = url[-(file_type.__len__() + 4):]
    else:
        file_name = url[-(file_type.__len__() + 3):]
    file_path = "E:\\workspace\\download\\" + file_name
    try:
        urllib.request.urlretrieve(url, file_path)
    except urllib.error.ContentTooShortError:
        print("reloading..." + url)
        download_ts(url)


def covert(a):
    if a >= 100:
        return str(a)
    elif a >= 10:
        return "0" + str(a)
    else:
        return "00" + str(a)


# def getNum(n: int):
#     if n < 1000:
#         return 3
#     else:
#         return 4


def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)


def rename():
    """
    修改1000以内的文件名： 000.ts --> 0000.ts 三位转4位
    """
    ls = os.listdir("E:\\workspace\\download\\")
    print(ls)
    for i in ls:
        c_path = os.path.join("E:\\workspace\\download\\", i)
        if i.__len__() == 6:
            os.renames(c_path, c_path[:-6] + "0" + c_path[-6:])


socket.setdefaulttimeout(120)
del_file('E:\\workspace\\download\\')
for a in range(start, num + 1):
    url = address[0:-(file_type.__len__() + 3)] + covert(a) + file_type
    download_ts(url, a)
    time.sleep(1)

os.system("copy /b E:\workspace\download\*" + file_type + " E:\workspace\\" + name + file_type)
