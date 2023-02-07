from selene import have
from selene.support.shared import browser


class DropDown:

    def __init__(self, element):
        self.element = element

    def select(self, by_text):
        browser.element(self.element).click()
        browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text(by_text)
      ).click()