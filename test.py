import unittest
from selenium import webdriver

from test_page import TestPage

def generate_wrong_format_email_list():
    """
    Generates wrong format emails list.

    Returns:
        result (list(str)): list of wrong emails
    """

    result = []

    name_list = ['', 'test']
    dog_list = ['', '@', '@@']
    box_list = ['', 'test']
    dot_list = ['', '.', '..']
    tld_list = ['', 'test']

    for name in name_list:
        for dog in dog_list:
            for box in box_list:
                for dot in dot_list:
                    for tld in tld_list:
                        result += [name + dog + box + dot + tld]

    result.remove('test@test.test')

    return result

class AuthForm(unittest.TestCase):
    """
    A class is for testing login form.
    """
    def setUp(self):
        self.valid_email = "test@protei.ru"
        self.valid_password = "test"

        self.driver = webdriver.Chrome()
        self.test_page = TestPage(self.driver)
        self.test_page.go_to_source_page()

    def test_login_click_valid_email_password(self):
        """
        Tests login with valid password and email by clicking on "Вход" button
        """
        test_page = self.test_page

        test_page.enter_login_email(self.valid_email)
        test_page.enter_password(self.valid_password)
        test_page.click_on_login_button()

        self.assertEqual(test_page.check_login_success(), True)

    def test_login_enter_valid_email_password(self):
        """
        Tests login with valid password and email by pressing "Enter" in password field
        """
        test_page = self.test_page

        test_page.enter_login_email(self.valid_email)
        test_page.enter_password(self.valid_password)
        test_page.press_enter_in_password_field()

        self.assertEqual(test_page.check_login_success(), True)

    def test_login_invalid_email_password(self):
        """
        Tests for message "Неверный E-Mail или пароль" appearance in case
        of invalid data in fields "Пароль" and "E-Mail" send in the login form.
        If the message "Неверный E-Mail или пароль" appears, then test passes.
        """
        test_page = self.test_page

        test_page.enter_login_email("test@test.ru")
        test_page.enter_password("test")
        test_page.click_on_login_button()

        self.assertEqual(test_page.check_login_success(), False)
        self.assertEqual(test_page.check_invalid_email_password_message(), True)

    def test_login_blank_password(self):
        """
        Tests for message "Неверный E-Mail или пароль" appearance in case
        of blank field "Пароль" send in the login form.
        If the message "Неверный E-Mail или пароль" appears when email is correct, 
        then test passes.
        """
        test_page = self.test_page

        test_page.enter_login_email("test@test.ru")
        test_page.enter_password("")
        test_page.click_on_login_button()

        self.assertEqual(test_page.check_login_success(), False)
        self.assertEqual(test_page.check_invalid_email_password_message(), True)

    def test_wrong_email_format_message(self):
        """
        Tests for message "Неверный формат E-Mail" appearance in case
        of wrong format email send in the login form.
        If the message "Неверный формат E-Mail" appears for all wrong format emails
        test passes.
        """
        test_page = self.test_page

        wrong_format_email_list = generate_wrong_format_email_list()
        expected_result = [True] * len(wrong_format_email_list)
        actual_result = []
        message = ''

        for email in wrong_format_email_list:
            test_page.enter_login_email(email)
            test_page.enter_password("")
            test_page.click_on_login_button()
            
            test_result = test_page.check_email_format_error_message() == True
            actual_result += [test_result]

            if test_result == False:
                message += "\nNo 'Неверный формат E-Mail' message for email '{}'".format(email)


        self.assertEqual(expected_result, actual_result, message)


    def tearDown(self):
        self.driver.close()

class InputPage(unittest.TestCase):
    """
    A class is for testing input form.
    """
    def setUp(self):
        self.valid_email = "test@protei.ru"
        self.valid_password = "test"

        self.email = "test@test.ru"
        self.name = "test"

        self.driver = webdriver.Chrome()
        self.test_page = TestPage(self.driver)
        self.test_page.go_to_source_page()

        self.test_page.enter_login_email(self.valid_email)
        self.test_page.enter_password(self.valid_password)
        self.test_page.click_on_login_button()
    
    def tearDown(self):
        self.driver.close()

    def test_success_add_window_close(self):
        """
        Tests closing window "Данные добавлены" which appears 
        after successful sending of data
        """
        test_page = self.test_page

        test_page.enter_input_email(self.email)
        test_page.enter_name(self.name)
        test_page.select_radio_1()

        test_page.click_on_send_button()
        test_page.click_on_ok_button()

        self.assertEqual(test_page.check_send_message_opened(), False)

    
    def test_email_display_right(self):
        """
        Tests sending and displaying value of field "E-Mail"
        """
        test_page = self.test_page

        test_page.enter_input_email(self.email)
        test_page.enter_name(self.name)
        test_page.select_radio_1()
        test_page.click_on_send_button()

        row = test_page.take_row_from_table(1)

        self.assertEqual(row['email'], self.email)

    def test_name_display_right(self):
        """
        Tests sending and displaying value of field "Имя"
        """
        test_page = self.test_page

        test_page.enter_input_email(self.email)
        test_page.enter_name(self.name)
        test_page.select_radio_1()
        test_page.click_on_send_button()

        row = test_page.take_row_from_table(1)

        self.assertEqual(row['name'], self.name)

    def test_gender_display_right(self):
        """
        Tests sending and displaying selected option of drop-down list  "Пол"
        """
        test_page = self.test_page

        test_page.enter_input_email(self.email)
        test_page.enter_name(self.name)
        test_page.select_radio_1()

        test_page.select_gender_male()
        test_page.click_on_send_button()
        test_page.click_on_ok_button()

        test_page.select_gender_female()
        test_page.click_on_send_button()
        test_page.click_on_ok_button()

        row_male  = test_page.take_row_from_table(1)
        row_female = test_page.take_row_from_table(2)

        self.assertEqual(row_male['gender'], "Мужской",
                         "\nGender 'Мужской' is not displayed correctly")
        self.assertEqual(row_female['gender'], "Женский",
                         "\nGender 'Женский' is not displayed correctly")

    def test_checkbox_display_correctly(self):
        """
        Tests sending and displaying selected checkboxes "Вариант 1"
        """

        test_page = self.test_page

        test_page.enter_input_email(self.email)
        test_page.enter_name(self.name)
        test_page.select_radio_1()
        test_page.click_on_send_button()
        test_page.click_on_ok_button()

        test_page.click_check_1()
        test_page.click_on_send_button()
        test_page.click_on_ok_button()
        test_page.click_check_1()


        test_page.click_check_2()
        test_page.click_on_send_button()
        test_page.click_on_ok_button()
        test_page.click_check_2()


        test_page.click_check_1()
        test_page.click_check_2()
        test_page.click_on_send_button()
        test_page.click_on_ok_button()

        row_check_0 = test_page.take_row_from_table(1)
        row_check_1 = test_page.take_row_from_table(2)
        row_check_2 = test_page.take_row_from_table(3)
        row_check_12 = test_page.take_row_from_table(4)

        self.assertEqual(row_check_0['check'], "Нет")
        self.assertEqual(row_check_1['check'], "1.1")
        self.assertEqual(row_check_2['check'], "1.2")
        self.assertEqual(row_check_12['check'], "1.1, 1.2")
        
    def test_radiobutton_display_correctly(self):
        """
        Tests sending and displaying selected radio buttons "Вариант 2"
        """
        test_page = self.test_page

        test_page.enter_input_email(self.email)
        test_page.enter_name(self.name)

        test_page.select_radio_1()
        test_page.click_on_send_button()
        test_page.click_on_ok_button()

        test_page.select_radio_2()
        test_page.click_on_send_button()
        test_page.click_on_ok_button()

        test_page.select_radio_3()
        test_page.click_on_send_button()
        test_page.click_on_ok_button()

        row_radio_1 = test_page.take_row_from_table(1)
        row_radio_2 = test_page.take_row_from_table(2)
        row_radio_3 = test_page.take_row_from_table(3)


        self.assertEqual(row_radio_1['radio'], '2.1')
        self.assertEqual(row_radio_2['radio'], '2.2')
        self.assertEqual(row_radio_3['radio'], '2.3')

    def test_send_some_row_display_correctly(self):
        """
        Tests sending and displaying several different valid data.
        """
        test_page = self.test_page

        expected = [    {'email': 'test1@test.ru',
                          'name': 'test1',
                          'gender': 'Мужской',
                          'check': '1.1',
                          'radio': '2.1'},
                        {'email': 'test2@test.ru',
                          'name': 'test2',
                          'gender': 'Женский',
                          'check': '1.2',
                          'radio': '2.2'},
                        {'email': 'test3@test.ru',
                          'name': 'test3',
                          'gender': 'Мужской',
                          'check': '1.1, 1.2',
                          'radio': '2.3'} 
                    ]

        test_page.enter_input_email("test1@test.ru")
        test_page.enter_name("test1")
        test_page.select_gender_male()
        test_page.click_check_1()
        test_page.select_radio_1()
        test_page.click_on_send_button()
        test_page.click_on_ok_button()
        test_page.click_check_1()

        test_page.enter_input_email("test2@test.ru")
        test_page.enter_name("test2")
        test_page.select_gender_female()
        test_page.click_check_2()
        test_page.select_radio_2()
        test_page.click_on_send_button()
        test_page.click_on_ok_button()
        test_page.click_check_2()

        test_page.enter_input_email("test3@test.ru")
        test_page.enter_name("test3")
        test_page.select_gender_male()
        test_page.click_check_1()
        test_page.click_check_2()
        test_page.select_radio_3()
        test_page.click_on_send_button()

        result  = [ test_page.take_row_from_table(1),
                    test_page.take_row_from_table(2),
                    test_page.take_row_from_table(3)]


        self.assertEqual(result, expected)

    def test_blank_name_field(self):
        """
        Tests for message "Поле имя не может быть пустым" appearance in case
        of blank field "Имя" send in the input form.
        If the message "Поле имя не может быть пустым" appears when all 
        other data is correct, test passes.
        """
        test_page = self.test_page
    
        expected = {'email': '',
                    'name': '',
                    'gender': '',
                    'check': '',
                    'radio': ''}
    
        test_page.enter_input_email(self.email)
        test_page.enter_name('')
        test_page.select_radio_1()
        test_page.click_on_send_button()

        empty_row = test_page.take_row_from_table(1)

        self.assertEqual(test_page.check_blank_name_error_message(), True,
                         "\nError message 'Поле имя не может быть пустым' did not appear")

        self.assertEqual(empty_row, expected,
                         "\nData with blank field 'Имя' was added to the table")
    
    def test_radiobutton_by_default(self):
        """
        Tests radiobuttons are checked by default.
        If none of the radiobuttons was pressed and other data is valid
        then added line to the field "Вариант 2" should contain "2.1" or "2.2" or "2.3".
        Else test fails.
        """
        test_page = self.test_page

        test_page.enter_input_email(self.email)
        test_page.enter_name(self.name)
        test_page.click_on_send_button()

        row = test_page.take_row_from_table(1)

        self.assertIn(row['radio'], ['2.1', '2.2', '2.3'],
                      "\nNone of radiobuttons are checked by default")

    def test_wrong_email_format(self):
        """
        Tests for message "Неверный формат E-Mail" appearance in case
        of wrong format email send in the input form.
        If the message "Неверный формат E-Mail" appears for all wrong format emails
        test passes.
        """

        test_page = self.test_page

        wrong_format_email_list = generate_wrong_format_email_list()
        expected_result = [True] * len(wrong_format_email_list)
        actual_result = []
        message = ''

        for email in wrong_format_email_list:
            test_page.enter_input_email(email)
            test_page.click_on_send_button()
            
            test_result = test_page.check_email_format_error_message() == True
            actual_result += [test_result]

            if test_result == False:
                message += "\nNo 'Неверный формат E-Mail' message for email '{}'".format(email)


        self.assertEqual(expected_result, actual_result, message)

if __name__ == "__main__":
    unittest.main(warnings='ignore')
