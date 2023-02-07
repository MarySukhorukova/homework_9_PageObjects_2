from selene import have
from selene.support.shared import browser


class DatePicker:

    def __init__(self, element):
        self.element = element

    def select_date(self, option):
        browser.element(self.element).all('option').element_by(have.exact_text(option)).click()