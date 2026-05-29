from selene.support.shared import browser
import allure
from allure_commons.types import AttachmentType


def add_screenshot(name="Screenshot"):
    allure.attach(
        browser.config.driver.get_screenshot_as_png(),
        name=name,
        attachment_type=AttachmentType.PNG,
    )