class QSSHelper:
    def __init__(self):
        pass

    @staticmethod
    def readQSS(qss_path):
        with open(qss_path, "r") as f:
            return f.read()
