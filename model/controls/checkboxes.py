from selene import have
from selene.support.shared import browser


class Checkbox:

    def __init__(self, element):
        self.element = element

    def check_hobby(self, option):
        browser.all(self.element).element_by(have.text(option)).click()

