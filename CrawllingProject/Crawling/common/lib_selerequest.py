
import time
import platform
from selenium import webdriver
from selenium.common.exceptions import TimeoutException


class SeleDriver:

    def __init__(self):
        pass

    def getDriverPath(self):
        plat = platform.system()
        if plat == 'Windows':
            driverPath = 'd:\\solution\\chromedriver_win32\\chromedriver.exe'
        else:
            driverPath = '/usr/local/bin/chromedriver'
            # driverPath = '/Users/SON/data/chromedriver'

        return driverPath

    def setDriver(self):
        driverPath = self.getDriverPath()

        options = webdriver.ChromeOptions()
        # 창이 뜨지 않게 설정
        options.add_argument('headless')

        driver = webdriver.Chrome(executable_path=driverPath, options=options)
        return driver

    # 구글 보안 기능 샌드박스를 비활성화 하는 것
    # 악성코드 침입이 쉬워진다.
    def setDriverNoSandbox(self, head=None):
        options = None
        driverPath = self.getDriverPath()

        if head == 'nohead':
            options.add_argument('headless')
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')

        driver = webdriver.Chrome(driverPath, options=options)
        return driver

    def setDriverNoOption(self, head=None):
        # options = None
        driverPath = self.getDriverPath()

        options = webdriver.ChromeOptions()

        if head == 'headless':
            options.add_argument('headless')
        # size
        options.add_argument("--start-maximized")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("Accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" )
        options.add_argument("Accept-Encoding=gzip, deflate, br")
        options.add_argument("Accept-Language=en-US,en;q=0.9,ko;q=0.8")
        options.add_argument("Connection=keep-alive")
        options.add_argument("Cookie=CookieNo=1042680256; smenu=menu%5Fortgi=20200919/141801; JKStarter=; PCID=16004926822230588237080; StarterRecentMenu=Recent0=1; __gads=ID=a902b2c24740bbcc:T=1600492682:S=ALNI_MZfPnSOZVBd3QoGKr3b_NQs6HyWEA; _ga=GA1.3.61676160.1600492682; _gac_UA-34423025-1=1.1600492684.Cj0KCQjwtZH7BRDzARIsAGjbK2azKqS57QQhfn9aDQfhvFBLjfLQpF3rys6HH5njftGn0IZhQ3cBX3oaAtmOEALw_wcB; _gac_UA-75522609-1=1.1600492684.Cj0KCQjwtZH7BRDzARIsAGjbK2azKqS57QQhfn9aDQfhvFBLjfLQpF3rys6HH5njftGn0IZhQ3cBX3oaAtmOEALw_wcB; TR10148105490_t_pa1=11.0.0.362715.null.null.null.0; _fbp=fb.2.1600492683828.1741098634; _wp_uid=2-7cbb77af82db090e273a3ef373614064-s1580222772.7158|mac_osx|chrome-1n8pgbv; mainContents=0; DirectStat=ON; Secure_IPonOFF=Y; saveKeyword=on; ASP.NET_SessionId=v0mgc0os5azzbh4w301ph4uz; ECHO_SESSION=1981600504573941; TR10148105490_t_uid=14145113018233099.1600504576556; ASPSESSIONIDQCQACDRC=JDEINLKCCBOANCBDFPDNFBPK; session=; KPIs=param=&keyword=; sm=keyword=; jkHost=www%2E; GnbMeActvtNewAlert=N; GnbMeOpenNewAlert=Y; User=UID=&Type=; Search%5FE%5FDate=1900%2D01%2D01; SMS%5FNum=0; JK%5FTemp=Mem%5FType%5FCode=&Mem%5FId=; TM%5FCnt=0; TO%5FCnt=0; jkmember%5FcLv=3; jkmember%5Fcreg=1; GuinC%5FName=%B4%A9%B8%AE%BE%EE%BD%C3%BD%BA%C5%DB; C%5FUSER=AAA=&UID=&DB%5FNAME=GI; Search%5FStat=0; WMONID=MF4sP5NCbNE; ASPSESSIONIDSCRBACQC=FECOILHDECPEJNFDHKFOLONJ; ASPSESSIONIDQCQADCRC=ICMLMHHDCONHHJNHHDNMBKOB; PstnInfoLayer=oneYear; ASPSESSIONIDSSDCCBSC=IPIFDKHDPFNBLINLJFPEBNPA; MainRcntlyData=%3c%6c%69%3e%3c%61%20%68%72%65%66%3d%22%2f%72%65%63%72%75%69%74%2f%6a%6f%62%6c%69%73%74%3f%6d%65%6e%75%63%6f%64%65%3d%6c%6f%63%61%6c%26%6c%6f%63%61%6c%6f%72%64%65%72%3d%31%22%3e%c1%f6%bf%aa%ba%b0%3c%2f%61%3e%20%26%67%74%3b%20%3c%61%20%68%72%65%66%3d%22%2f%72%65%63%72%75%69%74%2f%6a%6f%62%6c%69%73%74%3f%6d%65%6e%75%63%6f%64%65%3d%6c%6f%63%61%6c%26%6c%6f%63%61%6c%3d%48%30%30%30%22%20%63%6c%61%73%73%3d%22%63%61%74%65%22%3e%ba%ce%bb%ea%3c%2f%61%3e%3c%2f%6c%69%3e%7c%24%24%7c%3c%6c%69%3e%3c%61%20%68%72%65%66%3d%22%2f%72%65%63%72%75%69%74%2f%68%6f%6d%65%22%3e%c3%a4%bf%eb%c1%a4%ba%b8%c8%a8%3c%2f%61%3e%3c%2f%6c%69%3e%7c%24%24%7c; ASPSESSIONIDSQQBABTD=FIHCIIMDCMAEDIAFEBAHGAGK; ASPSESSIONIDSARDBDQC=MDPLIHEADPKIMPAPJJDAIMDA; ASPSESSIONIDQSCDCASD=MDPFKKNACAHGFFOJDOGFCENI; ASPSESSIONIDAAQCCBQA=BAAHONNBIOEHCGLAMMPHDKHO; ASPSESSIONIDQSTBDDRC=CMPHOPIAPIIDJFDHGDFHJLKN; PersonSrchngText=keyword=java; ASPSESSIONIDACTABBQB=BEICLBEAPAFKKCFJBAJKHEKM; BLogo%5FName=; Mem%5FStat=GI; M%5FPhoto%5FName=; ASPSESSIONIDQAQBDDSC=NOIFOKNBIPENGGNNHDCLEBKM; ResumeRead=7866518%7C10172097%7C18393209%7C6717432%7C18613481%7C17220462%7C17660766%7C; ASPSESSIONIDSSTBDARD=ANOKLHCCPCADJKMBEJADDDEA; jobkorea=Site_Oem_Code=C1; _gid=GA1.3.1194075987.1601887971; PassN%5FCnt=21; ASPSESSIONIDQATADATD=FGILJKABKBEBHOLJHCFGKBBH; Main_Top_Banner_Seq=1; TR10148105490_t_if=4.277.471.0.4ce6ff00d4bcf2676e55aa2835f61e48.null.null.14145511650449700; JK%5FUser=DI%5FCODE%5FEXIST=Y&S%5FName=&H%5FID=&C%5FID=636e10d1cc445194e46d3723b24f3433d8712fcbb96b4e8961b9d50d8d72d6ec65a9373768960518e67e525e77922783&LoginTime=2020%2D10%2D06+16%3A33%3A00&S%5FID=&E%5FID=&DS%5FID=f4e7362ad00202b3e7350137bb800f6c&LoginStat=8e9af2777eeb928bc49d75872aee93a530b7540469d7e16760ae422ae709d777&M%5FID=; PassALL%5FCnt=62; GuinN%5FCnt=7; Search%5FNum=95; ASPSESSIONIDSADSCDQD=NIIKCFNBPAFGPIDLPCCICMMB; last_search_saveno=120743358; _gat_trackerOne2=1; TR10148105490_t_sst=14145887986493700.1601969756021")
        options.add_argument("Host=www.jobkorea.co.kr")
        options.add_argument("Referer=https://www.jobkorea.co.kr/Login/Login.asp")
        options.add_argument("Sec-Fetch-Dest=iframe")
        options.add_argument("Sec-Fetch-Mode=navigate")
        options.add_argument("Sec-Fetch-Site=same-origin")
        options.add_argument("Upgrade-Insecure-Requests=1")
        options.add_argument("User-Agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36")

        driver = webdriver.Chrome(driverPath, options=options)
        return driver


    def reqSeleniumGet(self, driver, url):
        print('reqSeleniumGet S')
        print('url : ', url)
        try:
            driver.get(url)
            print('driver.get')
        except TimeoutException:
            print('SeleLogin - reqSeleniumGet - sleep')
            time.sleep(5)
            driver.get(url)
        except Exception as ex:
            print('SeleLogin - reqSeleniumGet')
            print(ex.__cause__)
            print(ex.__class__)
            print(ex.__context__)
        return driver


    def getPageSource(self, driver, plog):
        try:
            soup = None
        except Exception as ex:
            print('reqJabCount getPageSource:', ex)
            print(ex.__class__)
        finally:
            return soup

    '''
    # Selenium -> requests
    '''
    # def getRequestSession(self):
    #     from onch.utils.util_request import RequestHit
    #     req = RequestHit()
    #     return req.getSession()

    def getDriverCookieInfo(self, fromDriver, toSession):
        for cookie in fromDriver.get_cookies():
            c = {cookie['name']: cookie['value']}
            toSession.cookies.update(c)
        return toSession

    # request --> selenium
    def selLogin(self, driver, sess, url):
        # 1-2. request selenium
        driver = self.reqSeleniumGet(driver, url)

        # session value
        for c in sess.cookies:
            driver.add_cookie({'name': c.name, 'value': c.value})

        # refresh selenium
        driver.refresh()
        return driver


if __name__ == '__main__':
    sell = SeleDriver()

