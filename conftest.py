import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.main_page import MainPage
from page_objects.login_page import LoginPage
from urls import Endpoints
import requests
import helpers
from helpers import RegisterNewUser

faker = Faker()


@pytest.fixture(params=['firefox', 'chrome'], scope="function")
def driver(request):

    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        service = ChromeService(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service)

    browser.maximize_window()
    browser.implicitly_wait(10)

    browser.get(Endpoints.BASE_URL)

    yield browser

    browser.quit()


@pytest.fixture
def registration_new_user_and_delete(driver):

    user_registration = RegisterNewUser()
    payload = user_registration.generate_new_user_data()

    response = requests.post(Endpoints.CREATE_USER, json=payload)
    response_body = response.json()

    access_token = response_body.get('accessToken')
    if access_token:
        payload['accessToken'] = access_token
    else:
        raise ValueError("AccessToken отсутствует в ответе")

    main_page = MainPage(driver)
    main_page.click_on_auth_button_main_page()
    login_page = LoginPage(driver)
    login_page.wait_visibility_of_enter_title()
    login_page.send_email(payload['email'])
    login_page.send_password(payload['password'])
    login_page.click_on_enter_button()

    yield {'driver': driver, 'payload': payload, 'accessToken': response_body['accessToken']}

    access_token = response_body['accessToken']
    requests.delete(Endpoints.DELETE_USER, headers={'Authorization': access_token})


@pytest.fixture(scope='function')
def create_order(registration_new_user_and_delete):

    payload = {'ingredients': helpers.get_order_data()}
    access_token = registration_new_user_and_delete['accessToken']
    response = requests.post(Endpoints.CREATE_ORDER, json=payload,
                             headers={'Authorization': access_token})
    order_number = response.json()['order']['number']
    order = {'order_number': order_number,
             'user_email': registration_new_user_and_delete['payload']['email'],
             'user_password': registration_new_user_and_delete['payload']['password']}

    return order

