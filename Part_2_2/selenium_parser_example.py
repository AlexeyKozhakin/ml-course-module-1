from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

def save_page_html_selenium(id_game, forms = False):
    if not forms:
        link = f'https://soccer365.ru/games/{id_game}/'
        file_name = f'{id_game}.html'
    else:
        link = f'https://soccer365.ru/games/{id_game}/&tab=form_teams'
        file_name = f'form_teams{id_game}.html'

    # Установите параметры для Firefox
    options = Options()
    options.headless = True  # Запуск в фоновом режиме

    # Укажите путь к исполняемому файлу Firefox
    options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'  # Замените на ваш путь


    # Путь к geckodriver
    geckodriver_path = r'C:\Users\alexe\Downloads\ML-модуль-1\geckodriver.exe'

    # Запуск браузера
    service = Service(geckodriver_path)
    driver = webdriver.Firefox(service=service, options=options)

    # Переход на страницу
    driver.get(link)

    # Ждем полной загрузки страницы (необязательно, зависит от страницы)
    time.sleep(5)

    # Получаем полный HTML страницы
    page_html = driver.page_source

    # Сохраняем HTML в файл
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(page_html)

    # Закрываем браузер
    driver.quit()



if __name__ == '__main__':
    save_page_html_selenium(2084729, forms=False)
