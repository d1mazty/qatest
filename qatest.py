from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep


def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized') # Параметр FullScreen для запуска браузера
    browser = webdriver.Chrome(chrome_options=options) 
    wait = WebDriverWait(browser, 20)
    browser.get('https://netpeak.ua/')
    browser.find_element_by_xpath('//*[@id="main-menu"]/ul/li[5]/a').click() # Клик "Карьера"
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'green-btn'))).click() # Клик "Я хочу работать в Нетпик"
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'has-success')))  # Ожидание прогрузки div с нужным элементом
    # wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'blue-btn'))) # Логичнее так, но не всегда срабатывает
    
    browser.find_element_by_xpath('/html/body/input').send_keys('E:\\GitLocal\\netpeak_test\\logo.png') # Загрузка файла с недопустимым форматом
    browser.find_element_by_xpath('//*[@id="inputName"]').send_keys('Ivan') # Ввод имени
    browser.find_element_by_xpath('//*[@id="inputLastname"]').send_keys('Ivanov') # Ввод фамилии
    browser.find_element_by_xpath('//*[@id="inputEmail"]').send_keys('i.ivanov@gmail.com') # Ввод почты
    Select(browser.find_element_by_xpath('//*[@id="user-main-info"]/div[11]/div[2]/select')).select_by_value('2001') # Выбор года ДР
    Select(browser.find_element_by_xpath('//*[@id="user-main-info"]/div[11]/div[3]/select')).select_by_value('01') # Выбор месяца ДР
    Select(browser.find_element_by_xpath('//*[@id="user-main-info"]/div[11]/div[4]/select')).select_by_value('20') # Выбор даты ДР
    browser.find_element_by_xpath('//*[@id="inputPhone"]').send_keys('+380672001212') # Ввод телефона
    browser.find_element_by_xpath('//*[@id="submit"]').click() # Клик "Отправить резюме"
    sleep(3)
    browser.execute_script('window.scrollTo(0, 0)') # Переход на начало страницы, исполняя JS
    sleep(2) 
    browser.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/div[1]/div[1]').click() # Клик по логотипу
    sleep(2)   
    browser.quit()


if __name__ == "__main__":
    main()