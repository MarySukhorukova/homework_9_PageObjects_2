from selene import have
from selene.support.shared import browser
import os
from selene import command
import tests
from model.controls.checkboxes import Checkbox
from model.controls.datepicker import DatePicker
from model.controls.dropdown import DropDown
from model.controls.radiobutton import RadioButton
from model.data.user import User


class FillingForm:

    def input_data(self, user: User):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        radiobutton = RadioButton('[name=gender]')
        radiobutton.select_gender(user.gender)
        browser.element('#userNumber').type(user.phone)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        month = DatePicker('.react-datepicker__month-select')
        month.select_date(user.birthday_month)
        browser.element('.react-datepicker__year-select').click()
        year = DatePicker('.react-datepicker__year-select')
        year.select_date(user.birthday_year)
        browser.element(f'.react-datepicker__day--0{user.birthday_day}').click()
        browser.element('#subjectsInput').type(user.subject).press_enter()
        checkbox = Checkbox('[for^=hobbies-checkbox]')
        checkbox.check_hobby(user.hobby)
        browser.element('#uploadPicture').set_value(
            os.path.abspath(os.path.join(os.path.dirname(tests.__file__), 'files/Pytest_logo.svg.png')))
        browser.element('#currentAddress').type(user.address).perform(command.js.scroll_into_view)
        state = DropDown('#state')
        state.select(by_text=user.state)
        city = DropDown('#city')
        city.select(by_text=user.city)

    def open_practice_form(self):
        browser.open('/automation-practice-form')
        return self

    def submit_form(self):
        browser.element('#submit').press_enter()
        return self

    def should_be_data_in_form(self, user: User):
        browser.element('.table').all('td').even.should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone,
            f'{user.birthday_day} {user.birthday_month},{user.birthday_year}',
            user.subject,
            user.hobby,
            user.image,
            user.address,
            f'{user.state} {user.city}'
        ))