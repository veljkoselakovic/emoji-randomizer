import pickle


class Cookies(object):
    def __init__(self, driver):
        self.driver = driver

    def log_cookies(self):
        pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))

    def get_cookies(self):
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
