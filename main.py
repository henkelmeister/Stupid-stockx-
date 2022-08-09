# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium_stealth import stealth

def runProg(PROXYAddress):
    #   pyautogui.confirm('no bitches', buttons=['it be like that'])
    DRIVER_PATH = 'chromedriver.exe'
    PROXY = PROXYAddress
    options = webdriver.ChromeOptions()
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY,
        "proxyType": "MANUAL",

    }

    webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True
    options.add_argument("user-agent="+user_agent)
    options.add_argument("start-maximized")

    options.headless = True
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    action = ActionChains(driver)

    driver.get('https://stockx.com/adidas-yeezy-slide-black-onyx')
    #driver.get('https://bot.sannysoft.com/')

    user_agent_check = driver.execute_script("return navigator.userAgent;")
    print("User agent check\n\n")
    print(user_agent_check)
    print("\n\n end user agent check")

    time.sleep(2)

    print(driver.title)

    time.sleep(2)
    if driver.title == 'Access to this page has been denied':
        #You now have to try a different proxy address because the one you previously used did not work
        driver.close()
        print("calling new instace of program")
        runProg("167.172.173.210:38491") # Given that access to the page was denied this is where the new proxy address is passed in
        # Try this website using selenium to get all the proxy addresses https://geonode.com/free-proxy-list/


        ''' Ignore this block, was trying to make a script to bypass bot detection but realized it was futile
        runProg()
        bamboozle = driver.find_element(By.XPATH, "/html/body/div/div/div[2]")
        print(bamboozle)
        print(bamboozle.location)
        print(bamboozle.size)

        
        
        x, y = bamboozle.location
        size = bamboozle.size
        newX = (size['width']/2)
        newY = (size['height']/4)
        action.click_and_hold(bamboozle).move_by_offset(newX, newY)
        action.perform()
        time.sleep(10)
        action.release()
        print(driver.title)
        '''


        #stupid = driver.find_elements(By.XPATH, "//div[@id='px-captcha]")
        #print(stupid)
        #location = stupid.location
        #size = stupid.size
        #print(location)
        return
    else:
        #element = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/section[1]/div[2]/div/div[3]/div[2]/div[3]/div/div[1]/p[2]")
        #print(element.text)
        print('else statement executed')
        print(driver.title)
    return




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    runProg('95.217.62.36:3128') #First address (write a program that scrapes a proxy website and loads them into a list of proxyies to use)


#click and hold
#/html/body/div/div/div[2]/div[2]/p
#/html/body/div/div/div[2]/div[2]