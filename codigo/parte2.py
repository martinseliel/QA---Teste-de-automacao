# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 13:44:08 2021

@author: vitok
"""

"""
Funcionalidade: Busca no banco de questões
Cenário: Busca por quantidade específica de questões (25)..
Dado que navego para a página de busca do banco de questões
E marco a opção de busca 'categoria'
E busco pelo termo 'Science: Computers'
Quando clico no botão de buscar
Então verifico se há 25 questões listadas na página e se está presente a barra de paginação

"""
from selenium.webdriver import Firefox
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver
from time import sleep

class Escuta(AbstractEventListener):

    def before_click(self, elemento, webdriver):
        if elemento.tag_name == 'button':
            lista_ul = envolocro_browser.find_elements_by_tag_name('ul')
            assert len(lista_ul) > 1, 'Paginação não existe!'


url = 'https://opentdb.com/'

browser = Firefox()
envolocro_browser = EventFiringWebDriver(browser, Escuta())
envolocro_browser.get(url)
sleep(2)

a_lista = envolocro_browser.find_elements_by_tag_name('a')
botao = a_lista[1]
botao.click()

campo = envolocro_browser.find_element_by_tag_name('input')

seletor = envolocro_browser.find_elements_by_tag_name('option')
categoria = seletor[2]
categoria.click()

lista_btn = envolocro_browser.find_elements_by_tag_name('button')
botao_search = lista_btn[1]

campo.send_keys('Science: Computers')
botao_search.click()

tabela = envolocro_browser.find_element_by_tag_name('table')
linhas_tabela = tabela.find_elements_by_tag_name('tr')
del linhas_tabela[0]


assert len(linhas_tabela) == 25
