from selene.support.shared import browser
from selene import have, be

from helpers.files_funcs import generate_absolute_path


def given_opend_registration_form():
    browser.open("/automation-practice-form")
    browser.execute_script('[...document.body.getElementsByTagName("*")].filter(x => getComputedStyle(x, null).getPropertyValue("position") === "fixed").forEach(element => element.remove())')


def test_success_submit():
    given_opend_registration_form()

    """Fill the fields"""

    browser.element("#firstName").type("Nichole")
    browser.element("#lastName").type("Harvey")
    browser.element("#userEmail").type("rejet@mailinator.com")
    browser.element("#gender-radio-2 + .custom-control-label").click()
    browser.element("#userNumber").type("9991223421")
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__year-select option[value='1990']").click()
    browser.element(".react-datepicker__month-select option[value='5']").click()
    browser.element(".react-datepicker__month .react-datepicker__day--013").click()
    browser.element("#subjectsContainer input").click().type("c")
    browser.element(".subjects-auto-complete__option, .css-yt9ioa-option").click()
    subject = browser.element("#subjectsContainer .subjects-auto-complete__multi-value__label").text
    browser.element("#hobbies-checkbox-1 + .custom-control-label").click()
    browser.element("#uploadPicture").send_keys(generate_absolute_path("resources/student-photo.jpeg"))
    browser.element("#currentAddress").type("Saint-Petersburg, ul. Lenina, 45")
    browser.element("#state").click()
    browser.element("#state .css-yt9ioa-option").click()
    state = browser.element("#state .css-1uccc91-singleValue").text
    browser.element("#city").click()
    browser.element("#city .css-1n7v3ny-option").click()
    city = browser.element("#city .css-1uccc91-singleValue").text

    """Send and verify result"""

    browser.element("#submit").click()
    browser.element(".modal-header #example-modal-sizes-title-lg").should(be.present)
    browser.element(".modal-body").all("td:nth-child(even)").should(have.texts(
        'Nichole Harvey',
        'rejet@mailinator.com',
        'Female',
        '9991223421',
        '13 June,1990',
        subject,
        'Sports',
        'student-photo.jpeg',
        'Saint-Petersburg, ul. Lenina, 45',
        f'{state} {city}'
    ))

