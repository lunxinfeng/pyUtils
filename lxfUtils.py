def write(content: str, path="lxf.txt", type="wb"):
    """
    写入文件，并覆盖之前的内容，如果有的话
    :param type: 写入模式
    :param path: 文件全称
    :param content: 写入的内容
    :return:
    """
    with open(path, type) as file:
        file.write(content)


def read(path: str, type="rb"):
    with open(path, type) as file:
        return file.read()
