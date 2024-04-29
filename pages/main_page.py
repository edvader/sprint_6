
from locators.main_page_locators import MainPageLocator
from pages.base_page import BasePage
import allure

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик на "Самокат" в хеддере')
    def click_on_scooter_logo(self):
        self.click_on_element(MainPageLocator.SCOOTER_ICON)

    @allure.step('Клик на "Принять куки"')
    def click_on_cookie_button(self):
        self.click_on_element(MainPageLocator.COOKIE_BUTTON)

    @allure.step('Клик на кнопку "Принять куки"')
    def click_on_question(self, locator):
        self.click_on_element(locator)

    @allure.step('Клик на кнопку "Заказать" в хедере')
    def click_on_top_order_button(self):
        self.click_on_element(MainPageLocator.MAKE_ORDER_TOP_BUTTON)

    @allure.step('Клик на кнопку "Заказать" внизу главной страницы')
    def click_on_bottom_order_button(self):
        self.scroll_to_element(MainPageLocator.MAKE_ORDER_BOTTOM_BUTTON)
        self.click_on_element(MainPageLocator.MAKE_ORDER_BOTTOM_BUTTON)

    @allure.step('Получаем аттрибут елемента')
    def get_attribute(self, locator, attribute):
        return self.find_current_element(locator).get_attribute(attribute)

    @allure.step('Получаем атрибут картинки')
    def get_img_attribute(self):
        return self.get_attribute(MainPageLocator.IMG_MAIN_PAGE, "alt")

    @allure.step('Клик на "Яндекс" в хеддере')
    def click_on_yandex_logo(self):
        self.find_element_with_wait(MainPageLocator.YANDEX_ICON)
        self.click_on_element(MainPageLocator.YANDEX_ICON)

    @allure.step('Скроллим до вопросов')
    def scrolling_to_questions(self):
        self.scroll_to_element(MainPageLocator.QUESTION_8)

    @allure.step('Кликаем на вопрос')
    def click_important_question(self, number):
        method, locator = MainPageLocator.QUESTION_LOCATOR
        locator = locator.format(number)
        element = [method, locator]
        self.click_on_element(element)

    @allure.step('получаем ответ')
    def get_important_reply(self, number):
        method, locator = MainPageLocator.ANSWER_LOCATOR
        locator = locator.format(number)
        return self.driver.find_element(method, locator).text