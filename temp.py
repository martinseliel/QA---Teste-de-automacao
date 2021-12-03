# -*- coding: utf-8 -*-

"""
Funcionalidade: Busca no Banco de Questões
Cenário: Busca por questão inexistente
Dado que navego para a página de busca do banco de questões
E digito 'Science: Computers' no campo de busca
Quando clico no botão de buscar
Então visualizo uma mensagem de erro com o texto 'No questions found.'
"""

from selenium.webdriver import Firefox
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver
from time import sleep

class Escuta(AbstractEventListener):

    def before_close(self, webdriver):

        mensagem = envolocro_browser.find_elements_by_css_selector('.alert')[0].text
        print(mensagem)
        assert mensagem == 'No questions found.', 'Mensagem não confere!'


url = 'https://opentdb.com/'

browser = Firefox()
envolocro_browser = EventFiringWebDriver(browser, Escuta())
browser.get(url)
sleep(2)

a_lista = envolocro_browser.find_elements_by_tag_name('a')
botao = a_lista[1]
botao.click()

lista_btn = envolocro_browser.find_elements_by_tag_name('button')
botao_search = lista_btn[1]

campo = envolocro_browser.find_element_by_tag_name('input')
campo.send_keys('Science: Computers')
botao_search.click()
envolocro_browser.close() 

print()

