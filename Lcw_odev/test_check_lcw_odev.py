import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec


class TestCheckLcwOdev(unittest.TestCase):

    CATEGORY_PAGE = (By.CSS_SELECTOR, ".menu-header-item  ")  # Erkek Kategorisini Seç [1]
    CATEGORY_PAGE_2 = (By.CLASS_NAME, "visible-md")  # Alt kategori [0]
    PRODUCT_PAGE = (By.CLASS_NAME, "product-card.product-card--one-of-4")  # Ürün Seç [0]
    CHOICE_SIZE = (By.XPATH, '//*[@id="option-size"]/a')  # Beden Seç [1]
    ADD_TO_CART = (By.ID, "pd_add_to_cart")
    CART_PAGE = (By.CLASS_NAME, "dropdown-label")  # Sepet'e git [2]
    MAIN_PAGE = (By.CLASS_NAME, "main-header-logo")


    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get('https://www.lcwaikiki.com/tr-TR/TR')
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)

    def test_check_lcw_odev(self):
        self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE))[1].click()
        self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE_2))[0].click()
        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_PAGE))[3].click()
        self.wait.until(ec.presence_of_all_elements_located(self.CHOICE_SIZE))[2].click()
        self.wait.until(ec.element_to_be_clickable(self.ADD_TO_CART)).click()
        self.wait.until(ec.presence_of_all_elements_located(self.CART_PAGE))[2].click()
        self.wait.until(ec.element_to_be_clickable(self.MAIN_PAGE)).click()

        self.driver.quit()
