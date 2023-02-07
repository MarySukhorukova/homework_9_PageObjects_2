from selene import have
from selene.support.shared import browser


class RadioButton:

    def __init__(self, element):
        self.element = element

    def select_gender(self, option):
        browser.all(self.element).element_by(have.value(option)).element('..').click()