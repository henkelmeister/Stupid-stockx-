# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains

def runProg():
    #   pyautogui.confirm('no bitches', buttons=['it be like that'])
    DRIVER_PATH = 'chromedriver.exe'
    options = Options()
    options.headless = False
    options.add_argument("--window-size=1920,1200")


    #/html/body/div/div/div[2]/div[2]/p
    #/html/body/div/div/div[2]/div[2]/p

    #/html/body/div/div/div[2]/div[2]/p

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    action = ActionChains(driver)

    driver.get('https://stockx.com/adidas-yeezy-slide-black-onyx')

    print(driver.title)

    time.sleep(100)
    #/html/body/div/div/div[2]/div[2]/p
    if driver.title == 'Access to this page has been denied':
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


        time.sleep(100)
        #stupid = driver.find_elements(By.XPATH, "//div[@id='px-captcha]")
        #print(stupid)
        #location = stupid.location
        #size = stupid.size
        #print(location)
        return
    else:
        element = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/section[1]/div[2]/div/div[3]/div[2]/div[3]/div/div[1]/p[2]")
        print(element.text)
    return







    print("test print:")
    print(element.text)
    #print(location)
    #print(size)
    #/html/body/div[1]/div/main/div/section[1]/div[2]/div/div[3]/div[2]/div[3]/div/div[1]/p[2]
    #//*[@id="main-content"]/div/section[1]/div[2]/div/div[3]/div[2]/div[3]/div/div[1]/p[2]
    #/html/body/div[1]/div/main/div/section[1]/div[1]/div/div[5]/div/div[1]/p[2]
    #time.sleep(100)
    #element = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/section[1]/div[1]/div/div[5]/div/div[1]")
    #print(element.text)
    #print(driver.find_element(By.XPATH, "//div[@data-component='LastSale']"))
    #driver.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    runProg()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


#click and hold
#/html/body/div/div/div[2]/div[2]/p
#/html/body/div/div/div[2]/div[2]