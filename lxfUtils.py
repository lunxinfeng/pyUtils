

def write(content: str, path="lxf.txt"):
    """
    写入文件，并覆盖之前的内容，如果有的话
    :param path: 文件全称
    :param content: 写入的内容
    :return:
    """
    with open(path, "w") as file:
        file.write(content)



