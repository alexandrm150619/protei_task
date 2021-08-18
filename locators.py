from selenium.webdriver.common.by import By

class TestPageLocators:
    """
    A class for locators
    """
    AUTH_EMAIL_FIELD = (By.ID, "loginEmail")
    AUTH_PASSWORD_FIELD = (By.ID, "loginPassword")
    AUTH_LOGIN_BUTTON = (By.ID, "authButton")

    INPUT_EMAIL_FIELD = (By.ID, "dataEmail")
    INPUT_NAME_FIELD = (By.ID, "dataName")
    INPUT_GENDER_SELECTOR = (By.ID, "dataGender")
    INPUT_CHECK_1 = (By.ID, "dataCheck11")
    INPUT_CHECK_2 = (By.ID, "dataCheck12")
    INPUT_RADIO_1 = (By.ID, "dataSelect21")
    INPUT_RADIO_2 = (By.ID, "dataSelect22")
    INPUT_RADIO_3 = (By.ID, "dataSelect23")
    INPUT_SEND_BUTTON = (By.ID, "dataSend")
    INPUT_DATA_TABLE = (By.ID, "dataTable")
    INPUT_DIALOG_BUTTON = (By.XPATH, "/html/body/div[3]/div/div/div[2]/button")