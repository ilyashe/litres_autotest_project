import allure
from allure_commons.types import Severity

from data.users import User
from model.pages.main_page import main_page
from model.pages.profile_page import profile_page
import os


@allure.epic('Логаут')
@allure.label('owner', 'Ilya Shebanov')
@allure.feature('Проверка логаута юзера')
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
def test_logout():
    user = User(
        first_name='Andrey',
        last_name='Sokolov',
        email=os.getenv('EMAIL'),
        password=os.getenv('PASSWORD')
    )
    main_page.open()

    #WHEN
    main_page.fill_email(user)
    main_page.fill_password(user)
    main_page.open_profile()
    main_page.close_modal()
    profile_page.logout()

    #THEN
    main_page.user_should_be_unauthorized()