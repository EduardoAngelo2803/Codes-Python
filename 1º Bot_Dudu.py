#Importar a biblioteca Selenium, e dentro dela, o "livro" webdriver, ou seja, uma parte da Biblioteca
from selenium import webdriver
import time

#Comando para abrir o navegador
navegador = webdriver.Chrome()

#Comando para abrir um determinado site
navegador.get('https://afazenda.r7.com/a-fazenda-13')
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="box_614151a043527f00bc0004ec"]/div/div/div/div/section/div[2]/figure[2]/button').click()
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="checkbox"]').click()
time.sleep(3)
navegador.find_element_by_xpath('/html/body/div[7]/div[1]/div/div/div/div[1]/div[2]/button').click()

