from selenium.webdriver.common.by import By


def test_existence_add_to_basket_btn(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    btn_list = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert len(btn_list) >= 1, "Кнопка 'Добавить в корзину' не найдена на странице"
