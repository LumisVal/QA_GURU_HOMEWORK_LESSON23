import json

import allure
import requests
from allure_commons.types import AttachmentType

from config.settings import settings


def add_screenshot(driver, name="Screenshot"):
    allure.attach(
        driver.get_screenshot_as_png(),
        name=name,
        attachment_type=AttachmentType.PNG,
    )


def add_page_source(driver, name="Page source"):
    allure.attach(
        driver.page_source,
        name=name,
        attachment_type=AttachmentType.XML,
    )


def add_browserstack_session_link(session_id):
    session_url = (
        f"https://app-automate.browserstack.com/dashboard/v2/sessions/{session_id}"
    )

    allure.attach(
        session_url,
        name="BrowserStack session link",
        attachment_type=AttachmentType.TEXT,
    )


def add_browserstack_video(session_id):
    url = f"https://api.browserstack.com/app-automate/sessions/{session_id}.json"

    response = requests.get(
        url,
        auth=(settings.browserstack_user, settings.browserstack_key),
        timeout=10,
    )

    if response.status_code != 200:
        allure.attach(
            response.text,
            name="BrowserStack video error",
            attachment_type=AttachmentType.TEXT,
        )
        return

    video_url = response.json()["automation_session"]["video_url"]

    allure.attach(
        f"<html><body><video width='100%' controls><source src='{video_url}' type='video/mp4'></video></body></html>",
        name="BrowserStack video",
        attachment_type=AttachmentType.HTML,
    )