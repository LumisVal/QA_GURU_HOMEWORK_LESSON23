from selene import browser, have


# noinspection PyMethodMayBeStatic
class OnboardingPage:

    def should_see_first_screen(self):
        browser.element(
            ("id", "org.wikipedia.alpha:id/primaryTextView")
        ).should(have.text("The Free Encyclopedia"))

    def should_see_second_screen(self):
        browser.element(
            ("id", "org.wikipedia.alpha:id/primaryTextView")
        ).should(have.text("New ways to explore"))

    def should_see_third_screen(self):
        browser.element(
            ("id", "org.wikipedia.alpha:id/primaryTextView")
        ).should(have.text("Reading lists"))

    def should_see_fourth_screen(self):
        browser.element(
            ("id", "org.wikipedia.alpha:id/primaryTextView")
        ).should(
            have.text("Data & Privacy")
        )

    def continue_click(self):
        browser.element(
            ("id", "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
        ).click()

    def get_started(self):
        browser.element(
            ("id", "org.wikipedia.alpha:id/fragment_onboarding_done_button")
        ).click()