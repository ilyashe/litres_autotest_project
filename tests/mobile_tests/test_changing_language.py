import allure
from allure_commons.types import Severity
from model.pages.mobile_pages.main_page import main_page
from model.pages.mobile_pages.profile_page import profile_page


pytestmark = [
    allure.label("layer", 'mobile')
]

@allure.epic('Изменение языка интерфейса')
@allure.label('owner', 'Ilya Shebanov')
@allure.feature('Проверка изменения языка интерфейса')
@allure.tag('mobile')
@allure.severity(Severity.NORMAL)
def test_changing_language(android_management):
    main_page.open()

    # WHEN
    main_page.open_profile_page()
    profile_page.change_language_to_russian()

    # THEN
    profile_page.should_language_be_russian()
