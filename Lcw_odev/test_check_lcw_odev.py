import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class TestCheckLcwOdev(unittest.TestCase):
    CATEGORY_PAGE = (By.CSS_SELECTOR, ".menu-header-item  ")
    CATEGORY_PAGE_2 = (By.CLASS_NAME, 'visual-item__anchor__text')
    PRODUCT_PAGE = (By.CLASS_NAME, "product-card--one-of-4")
    CHOICE_SIZE = (By.CSS_SELECTOR, "#option-size a:not([data-stock*='0']")
    ADD_TO_CART = (By.ID, "pd_add_to_cart")
    CART_PAGE = (By.CLASS_NAME, "dropdown-label")
    MAIN_PAGE = (By.CLASS_NAME, "main-header-logo")
    PAYMENT_STEP = (By.CLASS_NAME, 'keep-shopping-label')


    base_url = 'https://www.lcwaikiki.com/tr-TR/TR'
    wait_time = 10

    def setUp(self):
        option = Options()
        option.add_argument('--disable-extensions')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(self.wait_time)
        self.wait = WebDriverWait(self.driver, self.wait_time)

    def test_check_lcw_odev(self):
        self.driver.get(self.base_url)
        self.assertIn('LC Waikiki', self.driver.title)

        element = self.driver.find_element(*self.CATEGORY_PAGE)
        ActionChains(self.driver).move_to_element(element).perform()

        self.driver.find_element(*self.CATEGORY_PAGE_2).click()
        self.assertIn('Kadın', self.driver.title)

        self.driver.find_elements(*self.PRODUCT_PAGE)[4].click()
        self.assertTrue(self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART)).text)

        self.driver.find_element(*self.CHOICE_SIZE).click()
        self.driver.find_element(*self.ADD_TO_CART).click()

        self.driver.find_elements(*self.CART_PAGE)[2].click()
        self.assertEqual('Alışverişe Devam Et', self.wait.until(
            EC.element_to_be_clickable(self.PAYMENT_STEP)).text)

        self.driver.find_element(*self.MAIN_PAGE).click()
        self.assertIn('LC Waikiki', self.driver.title)

    def tearDown(self):
        self.driver.close()
