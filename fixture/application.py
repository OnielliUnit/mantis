from selenium import webdriver
from fixture.session import sessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import mailHelper
from fixture.soap import SoapHelper

class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox(executable_path=r'../geckodriver.exe')
        elif browser == "chrome":
            self.wd = webdriver.Chrome(executable_path=r'../chromedriver.exe')
        elif browser == "ie":
            self.wd = webdriver.Ie(executable_path=r'../IEDriverServer.exe')
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(3)
        self.session = sessionHelper(self)
        self.project = ProjectHelper(self)
        self.james = JamesHelper(self)
        self.signup = SignupHelper(self)
        self.mail = mailHelper(self)
        self.soap = SoapHelper(self)
        self.config = config
        self.baseUrl = config['web']['baseUrl']

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.baseUrl)

    def destroy(self):
        self.wd.quit()
