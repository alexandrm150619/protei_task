from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from locators import TestPageLocators as TPL
from base_page import BasePage

class TestPage(BasePage):
    """
    A TestPage class ables to interact with the tested page
    """
    def enter_login_email(self, email):
        """
        Enters a email in the login form field "E-Mail"

        Arguments:
            email (str): email for input
        """
        elem_login_email = self.find_element(TPL.AUTH_EMAIL_FIELD)
        elem_login_email.clear()
        elem_login_email.send_keys(email)

    def enter_password(self, password):
        """
        Enters a password in the login form field "Пароль"

        Arguments:
            password (str): password for input
        """
        elem_login_password = self.find_element(TPL.AUTH_PASSWORD_FIELD)
        elem_login_password.clear()
        elem_login_password.send_keys(password)

    def press_enter_in_password_field(self):
        """
        Presses "Enter" in the login form field "Пароль"
        """
        self.find_element(TPL.AUTH_PASSWORD_FIELD).send_keys(Keys.RETURN)

    def click_on_login_button(self):
        """
        Clicks on a button "Вход"
        """
        self.find_element(TPL.AUTH_LOGIN_BUTTON).click()

    def enter_input_email(self, email):
        """
        Enters a email in the input form field "E-Mail"

        Arguments:
            email (str): email for input
        """
        elem_input_email = self.find_element(TPL.INPUT_EMAIL_FIELD)
        elem_input_email.clear()
        elem_input_email.send_keys(email)

    def enter_name(self, name):
        """
        Enters a name in the input form field "Имя"

        Arguments:
            name (str): name for input
        """
        elem_input_name = self.find_element(TPL.INPUT_NAME_FIELD)
        elem_input_name.clear()
        elem_input_name.send_keys(name)

    def select_gender_male(self):
        """
        Selects "Мужской" in drop-down list "Пол"
        """
        elem_gender = Select(self.find_element(TPL.INPUT_GENDER_SELECTOR))
        elem_gender.select_by_index(0)

    def select_gender_female(self):
        """
        Selects "Женский" in drop-down list "Пол"
        """
        elem_gender = Select(self.find_element(TPL.INPUT_GENDER_SELECTOR))
        elem_gender.select_by_index(1)

    def click_check_1(self):
        """
        Click on a check box "Вариант 1.1"
        """
        self.find_element(TPL.INPUT_CHECK_1).click()

    def click_check_2(self):
        """
        Clicks on a check box "Вариант 1.2"
        """
        self.find_element(TPL.INPUT_CHECK_2).click()

    def select_radio_1(self):
        """
        Selects a radio button "Вариант 2.1"
        """
        self.find_element(TPL.INPUT_RADIO_1).click()

    def select_radio_2(self):
        """
        Selects a radio button "Вариант 2.2"
        """
        self.find_element(TPL.INPUT_RADIO_2).click()

    def select_radio_3(self):
        """
        Selects a radio button "Вариант 2.3"
        """
        self.find_element(TPL.INPUT_RADIO_3).click()

    def click_on_send_button(self):
        """
        Clicks on a button "Добавить"
        """
        self.find_element(TPL.INPUT_SEND_BUTTON).click()

    def click_on_ok_button(self):
        """
        Clicks on a button "Ok"
        """
        self.find_element(TPL.INPUT_DIALOG_BUTTON).click()

    def take_row_from_table(self, row_num):
        """
        Returns a row from a data table
        
        Arguments:
            row_num (int): number of the line from which the data is taken.
                           If pass 0, row with the headers will be extracted.
                           If pass row_num > number of rows in table, row 
                                with blank columns will be extracted.

        Returns:
            result (dict): dictionary representing columns of a table row with 
                           specified number in the form:
                           {
                               email (str): "E-Mail" column,
                               name (str): "Имя" column,
                               gender (str): "Пол" column,
                               check (str): "Выбор 1" column,
                               radio (str): "ВЫбор 2" column
                           }

        """
        elem_table = self.find_element(TPL.INPUT_DATA_TABLE)
        rows = elem_table.find_elements(By.TAG_NAME, "tr")

        result = {'email': '', 
                  'name': '',
                  'gender': '',
                  'check': '', 
                  'radio': ''}

        if row_num < len(rows):
            row = rows[row_num]
            result['email'] = row.find_elements(By.TAG_NAME, "td")[0].text
            result['name'] = row.find_elements(By.TAG_NAME, "td")[1].text
            result['gender'] = row.find_elements(By.TAG_NAME, "td")[2].text
            result['check'] = row.find_elements(By.TAG_NAME, "td")[3].text
            result['radio'] = row.find_elements(By.TAG_NAME, "td")[4].text

        return result

    def check_invalid_email_password_message(self):
        """
        Checks if message "Неверный E-Mail или пароль" appeared
        """
        try:
            self.driver.find_element_by_id("invalidEmailPassword")
            result = True
        except:
            result = False

        return result

    def check_email_format_error_message(self):
        """
        Checks if message "Неверный формат E-Mail" appeared
        """
        try:
            self.driver.find_element_by_id("emailFormatError")
            result = True
        except:
            result = False

        return result

    def check_blank_name_error_message(self):
        """
        Checks if message "Поле имя не может быть пустым" appeared
        """
        try:
            self.driver.find_element_by_id("blankNameError")
            result = True
        except:
            result = False

        return result

    def check_login_success(self):
        """
        Checks login success by determining the visibility of the input form
        Returns:
            True: if login was successful
            False: if login was failed
        """
        elem_inputsPage = self.driver.find_element_by_id('inputsPage')
        display = elem_inputsPage.value_of_css_property('display')
        
        return  display != 'none'

    def check_send_message_opened(self):
        """
        Checks if the message window "Данные добавлены" is opened
        Returns:
            True: if message window is opened
            False: if message window was is opened
        """
        try:
            self.driver.find_element_by_xpath("/html/body/div[3]")
            result = True
        except:
            result = False

        return result
