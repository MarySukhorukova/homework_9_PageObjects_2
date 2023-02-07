from model.data.user import User
from model.pages import practice_form
from model.pages.practice_form import FillingForm


def test_filling_and_submitting_form():
    user = User(first_name='Harry',
                last_name='Potter',
                email='hp@test.com',
                gender='Male',
                phone='0123456789',
                birthday_day=31,
                birthday_month='July',
                birthday_year='1980',
                subject='Arts',
                hobby='Sports',
                image='Pytest_logo.svg.png',
                address='Hogwarts',
                state='Haryana',
                city='Karnal')

    practice_form.open_practice_form()
    practice_form.input_data(user)
    practice_form.submit_form()

    practice_form.should_be_data_in_form(user)


practice_form = FillingForm()
