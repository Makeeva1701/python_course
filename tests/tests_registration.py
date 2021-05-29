from page_objects.elements.RegistrationForm import RegistrationForm


def test_new_user_registration(browser, url):
    RegistrationForm(browser).open_registration_form(url)
    RegistrationForm(browser).registration_user()
