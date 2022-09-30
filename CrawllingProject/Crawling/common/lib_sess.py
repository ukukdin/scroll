
from lib_selerequest import SeleDriver

class LibSession:

    def __init__(self):
        self.req = None
        self.sess = None

        self.sell = None
        self.driver = None

    ################
    # Selenium
    ################
    # INIT SELENIUM GET Session
    # GET Selenium Driver
    def getSeleDriver(self):
        self.sell = SeleDriver()
        self.driver = self.sell.setDriverNoOption()
        return self.driver

    def closeDriver(self):
        self.driver.close()