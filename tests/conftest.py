import pytest
from appium import webdriver


@pytest.fixture
def driver(request):
    capabilities = {
        'platformName': 'Android',
        'appium:platformVersion': '11.0',
        'appium:automationName': 'uiautomator2',
        'appium:appiumVersion': '1.22.0',
        'appium:deviceName': 'emulator5554',
        'appium:deviceOrientation': 'portrait',
        'appium:appPackage': 'br.com.petz',
        'appium:appActivity': 'br.com.hanzo.petz.view.MainActivity'
    }

    _url = 'http://localhost:4723/wd/hub'
    driver_ = webdriver.Remote(_url, capabilities)

    def sair():
        driver_.quit()

    request.addfinalizer(sair)
    return driver_
