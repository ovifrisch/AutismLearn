#https://stackoverflow.com/questions/9193603/applying-a-coloured-overlay-to-an-image-in-either-pil-or-imagemagik

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time

class Scraper:
    def __init__(self, home_url, chrome_path):
        self.home_url = home_url
        self.driver = webdriver.Chrome(chrome_path)

    def start(self):
        self.driver.get(self.home_url)
        problinks = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "skill-tree-skill-link")))
        for idx, plink in enumerate(problinks):
            plinks = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "skill-tree-skill-link")))
            plink = plinks[idx]
            plink.click()
            WebDriverWait(self.driver, 10)
            self.driver.save_screenshot("problem" + str(idx) + ".png")
            self.driver.get(self.home_url)



if __name__ == "__main__":
    s = Scraper("https://www.ixl.com/math/grade-1", "../chromedriver")
    s.start()


#
# f = open("index.html", 'w')
#
# chrome_path = "../chromedriver"
#
# url = "https://www.ixl.com/math/pre-k/learn-to-count-up-to-3"
# driver = webdriver.Chrome(chrome_path)
# driver.get(url)
# exitbtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "modal-close")))
# exitbtn.click()
# driver.save_screenshot("screen.png")
#
#
# els = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "secContentPiece")))
# print(len(els))
#
# for el in els:
#     f.write(el.get_attribute("innerHTML"))
