from model.pages.mobile_pages.main_page import main_page
from model.pages.mobile_pages.profile_page import profile_page

def test_changing_language(android_management):
    main_page.open()

    # WHEN
    main_page.open_profile_page()
    profile_page.change_language_to_russian()

    # THEN
    profile_page.should_language_be_russian()
