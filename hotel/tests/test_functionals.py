import time

import pytest
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope='class', params=['chrome', 'edge'])
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome("hotel/tests/chromedriver.exe")
    if request.param == "edge":
        web_driver = webdriver.Edge("hotel/tests/msedgedriver.exe")
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("driver_init")
class TestDriver:
    def test_open_url(self, live_server):
        self.driver.get(live_server.url)
        assert "Hotel-ST88" in self.driver.title

    def test_choose_room_category(self, live_server, new_room):
        self.driver.get(live_server.url)
        select_room_cats = self.driver.find_elements(by=By.TAG_NAME, value='h2')
        for room_cat in select_room_cats:
            if room_cat.text == new_room.cat.name:
                room_cat.click()
        assert self.driver.find_element(by=By.CLASS_NAME, value='room-info').find_element(by=By.TAG_NAME,
                                                                                          value='h1').text == new_room.cat.name

    def test_authenticate_user(self, db, live_server, new_user):
        self.driver.get(f'{live_server.url}/accounts/login/')

        login = self.driver.find_element(by=By.NAME, value='login')
        password = self.driver.find_element(by=By.NAME, value='password')
        submit = self.driver.find_element(by=By.TAG_NAME, value='button')

        login.send_keys(new_user.username)
        password.send_keys(new_user.password)
        submit.send_keys(Keys.RETURN)

        menu = self.driver.find_elements(by=By.CLASS_NAME, value='brand')
        flag = False
        for item in menu:
            if item.text == 'Booked rooms':
                flag = True
        assert flag

    def test_create_new_user(self, live_server):
        self.driver.get(f'{live_server.url}/accounts/signup/')

        username = self.driver.find_element(by=By.NAME, value='username')
        email = self.driver.find_element(by=By.NAME, value='email')
        password1 = self.driver.find_element(by=By.NAME, value='password1')
        password2 = self.driver.find_element(by=By.NAME, value='password2')
        submit = self.driver.find_element(by=By.TAG_NAME, value='button')

        username.send_keys('new_user')
        email.send_keys('new_user@gmail.com')
        password1.send_keys('fylhtq03')
        password2.send_keys('fylhtq03')
        submit.send_keys(Keys.RETURN)

        menu = self.driver.find_elements(by=By.CLASS_NAME, value='brand')
        flag = False
        for item in menu:
            if item.text == 'Booked rooms':
                flag = True
        assert flag
