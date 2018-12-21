from selenium import webdriver


class Item(object):
    book_name = None  # 书名


class Spider:

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.url = "https://www.101weiqi.com/book/level/1/"

    def get_books(self):
        self.browser.get(self.url)
        self.browser.implicitly_wait(3)

        list = self.browser.find_elements_by_css_selector("a[ng-href*='book']")
        for item in list:
            print(item.text + "\t" + item.get_attribute("href"))

    def exit(self):
        self.browser.quit()


if __name__ =='__main__':
    spider = Spider()
    spider.get_books()
    spider.exit()
