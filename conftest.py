import os

import pytest

from appium.options.android import UiAutomator2Options
from selene import browser
from selenium import webdriver

from config.settings import settings


@pytest.fixture(scope="function", autouse=True)
def mobile_management():

    if os.getenv("CONTEXT") == "bstack":

        options = UiAutomator2Options()

        options.set_capability(
            "bstack:options",
            {
                "userName": settings.browserstack_user,
                "accessKey": settings.browserstack_key,
                "deviceName": settings.android_device,
                "osVersion": settings.android_os_version,
                "projectName": settings.project_name,
                "buildName": settings.build_name,
                "sessionName": settings.session_name,
            }
        )

        options.set_capability("app", settings.android_app)

        driver = webdriver.Remote(
            command_executor="https://hub.browserstack.com/wd/hub",
            options=options,
        )

    else:

        options = UiAutomator2Options()

        options.set_capability("platformName", "Android")
        options.set_capability("deviceName", settings.device_name)
        options.set_capability("platformVersion", settings.platform_version)
        options.set_capability("app", os.path.abspath(settings.app))

        driver = webdriver.Remote(
            "http://127.0.0.1:4723",
            options=options
        )

    browser.config.driver = driver

    yield

    driver.quit()