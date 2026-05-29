import allure
from selene import browser, have


class OnboardingPage:

    @allure.step("Проверить первый экран")
    def should_see_first_screen(self):
        browser.element(
            ("id", "org.wikipedia.alpha:id/primaryTextView")
        ).should(
            have.text("The Free Encyclopedia")
        )

    @allure.step("Проверить второй экран")
    def should_see_second_screen(self):
        browser.element(
            ("id", "org.wikipedia.alpha:id/primaryTextView")
        ).should(
            have.text("New ways to explore")
        )

    @allure.step("Проверить третий экран")
    def should_see_third_screen(self):
        browser.element(
            ("id", "org.wikipedia.alpha:id/primaryTextView")
        ).should(
            have.text("Reading lists")
        )

    @allure.step("Проверить четвертый экран")
    def should_see_fourth_screen(self):
        browser.element(
            ("id", "org.wikipedia.alpha:id/primaryTextView")
        ).should(
            have.text("Data & Privacy")
        )

    @allure.step("Нажать Continue")
    def continue_click(self):
        browser.element(
            ("id", "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
        ).click()

    @allure.step("Нажать Get Started")
    def get_started(self):
        browser.element(
            ("id", "org.wikipedia.alpha:id/fragment_onboarding_done_button")
        ).click()