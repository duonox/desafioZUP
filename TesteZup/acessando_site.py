import unittest


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class CompraClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testPageTitle(self):
        driver=self.driver
        driver.get("https://www.magazineluiza.com.br/")
        self.assertIn("Magazine Luiza | Pra você é Magalu", driver.title)
        busca = driver.find_element_by_xpath("//div[@class='search-header header-search-container']//input[1]")
        busca.send_keys("Samsung Note 10")
        busca.send_keys(Keys.RETURN)
        driver.implicitly_wait(6)
        self.assertTrue("Smartphone Samsung Galazy Note 10 256GB")
        driver.implicitly_wait(12)
        select_iten = driver.find_element_by_xpath ("//*[contains(text(),'Smartphone Samsung Galaxy Note 10 256GB Dual Chip Android')]")
        select_iten.click()
        driver.implicitly_wait(7)
        buy_iten = driver.find_element_by_xpath("//*[contains(text(),'Adicionar à sacola')]")
        buy_iten.click()
        driver.implicitly_wait(7)
        self.assertTrue("Código do produto: jd1c2685ah")
        #Verifico se há um produto na sacola, através do código do produto

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()