import os.path

from selene import browser, be, command, have


def test_demoqa():
    browser.open('/')
    browser.element('#firstName').type('Petr')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('petr15@mail.ru')
    browser.element('[class="custom-control-label"][for="gender-radio-1"]').click()
    browser.element('#userNumber').type('7000000000')
    browser.element('#dateOfBirthInput').clear()
    browser.element('.react-datepicker__month-select').click().element('[value="0"]').click()
    browser.element('.react-datepicker__year-select').click().type('1990').press_enter()
    browser.element('[class="react-datepicker__day react-datepicker__day--015"]').click()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('[class="custom-control-label"][for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('image/picture.jpg'))
    browser.element('#currentAddress').type('Moscow, Arbat street, 15')
    browser.element('#react-select-3-input').should(be.visible).type('NCR').press_enter()
    browser.element('#react-select-4-input').should(be.visible).type('Delhi').press_enter()
    browser.element('#submit').perform(command.js.scroll_into_view)
    browser.element('#submit').execute_script('element.click()')
    browser.element('.modal-content').element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td:nth-of-type(2)').should(have.texts(
        'Petr Ivanov',
        'petr15@mail.ru',
        'Male',
        '7000000000',
        '15 January,1990',
        'Maths',
        'Reading',
        'picture.jpg',
        'Moscow, Arbat street, 15',
        'NCR Delhi'))

















