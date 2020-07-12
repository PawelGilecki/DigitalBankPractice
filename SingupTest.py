import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
from selenium.webdriver.common.keys import Keys
import random
import datetime

sys.path.append(r"C:\Users\PawelGilecki\Desktop\DigitalBankPractice")
from pageObjects.SignupPage import SignupPage
from generators.generate_dob import generateDOB
from generators.SSN_generator import generateSSN
from generators.password_generator import generatePassword
from generators.postal_code_generator import generatePostalCode
from generators.phone_generator import generateMobile
from generators.phone_generator import generateHomePhone
from generators.phone_generator import generateWorkPhone

class SignupTest(unittest.TestCase):
    driver = webdriver.Firefox(executable_path=r"C:\Users\PawelGilecki\Desktop\DigitalBankPractice\driver\geckodriver.exe")
    wait = WebDriverWait(driver, 5)
    email_URL = "https://10minutemail.com/"
    signup_URL = "http://dbankdemo.com/signup"
    title = random.randint(1,3)
    firstName = "Marek"
    lastName = "Bliski"
    dob = generateDOB()
    SSN = generateSSN()
    password = generatePassword()
    address = "Bliska 111/11"
    locality = "Gdańsk"
    region = "Pomorskie"
    PostalCode = generatePostalCode()
    country = "Poland"
    HomePhone = generateHomePhone()
    MobilePhone = generateMobile()
    WorkPhone = generateWorkPhone()

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.email_URL)
        wait = WebDriverWait(cls.driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="qcCmpUi"]')))
        cls.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/button[2]").click()
        cls.driver.find_element_by_id("mail_address").send_keys(Keys.CONTROL + "c")
        cls.driver.get(cls.signup_URL)
        wait.until(EC.visibility_of_element_located((By.ID, "emailAddress")))
        cls.driver.maximize_window()
        cls.driver.find_element_by_id("emailAddress").send_keys(Keys.CONTROL + "v")

    def test_signup(self):
        wait = WebDriverWait(self.driver, 5)
        self.assertEqual("http://dbankdemo.com/signup", self.driver.current_url, "this is not signup page")
        signup_page = SignupPage(self.driver)
        wait.until(EC.element_to_be_clickable((By.XPATH, SignupPage.next_button_xpath)))
        signup_page.setTitle(self.title)
        signup_page.getTitle().text
        signup_page.setFirstName(self.firstName)
        signup_page.setLastName(self.lastName)
        signup_page.setGenderMale()
        signup_page.setDOB(self.dob)
        signup_page.setSSN(self.SSN)
        signup_page.setPassword(self.password)
        signup_page.confirmPassword(self.password)
        signup_page.clickNext()
        wait.until(EC.element_to_be_clickable((By.XPATH, SignupPage.register_button_xpath)))
        self.assertEqual("http://dbankdemo.com/signup", self.driver.current_url, "this is not signup page")
        signup_page.setAddress(self.address)
        signup_page.setLocality(self.locality)
        signup_page.setRegion(self.region)
        signup_page.setPostalCode(self.PostalCode)
        signup_page.setCountry(self.country)
        signup_page.setHomePhone(self.HomePhone)
        signup_page.setMobilePhone(self.MobilePhone)
        signup_page.setWorkPhone(self.WorkPhone)
        signup_page.checkAgreeTerms()
        signup_page.clickRegister()
        wait.until(EC.element_to_be_clickable((By.XPATH, SignupPage.sign_in_from_register)))
        self.assertEqual("http://dbankdemo.com/register", self.driver.current_url, "this is not finish sign up page")
        self.assertEqual("Registration Successful. Please Login.", self.driver.find_element_by_xpath(SignupPage.registration_successfull_msg_xpath).text, "this is not finish sign up page")
        signup_page.setPassword(self.password)
        signup_page.clickSignInFromRegister()
        self.assertEqual("http://dbankdemo.com/home", self.driver.current_url, "this is not homepage, not able to log in with new user")
        self.assertEqual("Welcome Marek", self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/ol/li").text, "this is not Marek")

    #@classmethod
    #def tearDownClass(cls):
        #cls.driver.close()

if __name__ == "__main__":
    unittest.main()