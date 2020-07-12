from selenium.webdriver.support.ui import Select
import random

class SignupPage():
    title_id = "title"
    first_name_id = "firstName"
    last_name_id = "lastName"
    man = "label.form-check-label:nth-child(1) > input:nth-child(1)"
    woman = "label.form-check-label:nth-child(2) > input:nth-child(1)"
    dob_id = "dob"
    social_security_no_id = "ssn"
    email_id = "emailAddress"
    password_id = "password"
    confirm_password_id = "confirmPassword"
    next_button_xpath = "/html/body/div[1]/div/div/div[2]/form/button"
    address_id = "address"
    locality_id = "locality"
    region_id = "region"
    postal_code_id = "postalCode"
    country_id = "country"
    home_phone_id = "homePhone"
    mobile_phone_id = "mobilePhone"
    work_phone_id = "workPhone"
    agree_terms_id = "agree-terms"
    register_button_xpath = "/html/body/div[1]/div/div/div[2]/form/button"
    sign_in_from_register = '//*[@id="submit"]'
    registration_successfull_msg_xpath = "/html/body/div[1]/div/div/div[2]/div/span[2]"

    def __init__(self, driver):
        self.driver = driver

    def setTitle(self, title):
        Select(self.driver.find_element_by_id(self.title_id)).select_by_index(title)

    def getTitle(self):
        self.driver.find_element_by_id(self.title_id).text

    def setFirstName(self, firstName):
        self.driver.find_element_by_id(self.first_name_id).send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element_by_id(self.last_name_id).send_keys(lastName)

    def setGenderMale(self):
        self.driver.find_element_by_css_selector(self.man).click()

    def setGenderFemale(self):
        self.driver.find_element_by_css_selector(self.woman).click()

    def setDOB(self, dob):
        self.driver.find_element_by_id(self.dob_id).send_keys(dob)

    def setSSN(self, SSN):
        self.driver.find_element_by_id(self.social_security_no_id).send_keys(SSN)

    def setEmail(self, email):
        self.driver.find_element_by_id(self.email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def confirmPassword(self, password):
        self.driver.find_element_by_id(self.confirm_password_id).send_keys(password)

    def clickNext(self):
        self.driver.find_element_by_xpath(self.next_button_xpath).click()

    def setAddress(self, address):
        self.driver.find_element_by_id(self.address_id).send_keys(address)

    def setLocality(self, locality):
        self.driver.find_element_by_id(self.locality_id).send_keys(locality)

    def setRegion(self, region):
        self.driver.find_element_by_id(self.region_id).send_keys(region)

    def setPostalCode(self, PostalCode):
        self.driver.find_element_by_id(self.postal_code_id).send_keys(PostalCode)

    def setCountry(self, country):
        self.driver.find_element_by_id(self.country_id).send_keys(country)

    def setHomePhone(self, HomePhone):
        self.driver.find_element_by_id(self.home_phone_id).send_keys(HomePhone)

    def setMobilePhone(self, MobilePhone):
        self.driver.find_element_by_id(self.mobile_phone_id).send_keys(MobilePhone)

    def setWorkPhone(self, WorkPhone):
        self.driver.find_element_by_id(self.work_phone_id).send_keys(WorkPhone)

    def checkAgreeTerms(self):
        self.driver.find_element_by_id(self.agree_terms_id).click()

    def clickRegister(self):
        self.driver.find_element_by_xpath(self.register_button_xpath).click()

    def clickSignInFromRegister(self):
        self.driver.find_element_by_xpath(self.sign_in_from_register).click()