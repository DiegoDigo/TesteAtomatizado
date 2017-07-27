from __future__ import unicode_literals
from selenium import webdriver
import unittest


class TesteLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.base_url = "http://linkedby-ecommerce.com.br:9004/"

    def testeAcesso(self):
            driver = self.driver
            driver.get(self.base_url + "#/home")
            driver.find_element_by_xpath("//input[@ng-model='account.usuario']").clear()
            driver.find_element_by_xpath("//input[@ng-model='account.usuario']").send_keys("13143408000008")
            driver.find_element_by_xpath("//input[@ng-model='account.password']").clear()
            driver.find_element_by_xpath("//input[@ng-model='account.password']").send_keys("13143408000008")
            driver.find_element_by_class_name("bt_logar").submit()
            self.assertEqual(driver.find_element_by_css_selector("span.ng-binding").text, "CRISTIANO")
            driver.close()

    # def testeEsqueceuSenha(self):
    #     driver = self.driver
    #     driver.get(self.base_url + "#/home")
    #     driver.find_element_by_xpath("//a[@ng-click='abreEsqueceuSenha()']").click()
    #     # self.assertEqual(driver.find_element_by_tag_name('h2').text, 'RECUPERAÇÃO DE SENHA')
    #     driver.find_element_by_xpath("//input[@ng-model='account.email']").clear()
    #     driver.find_element_by_xpath("//input[@ng-model='account.email']").send_keys("teste@gmail.com")
    #     driver.find_element_by_xpath("//input[@ng-click='lembrarSenha(account.email)']").submit()

    # def testeEsqueceuSenha(self):
    #     driver = self.driver
    #     driver.get(self.base_url + "#/home")
    #     driver.find_element_by_xpath("//a[@ng-click='abreEsqueceuSenha()']").click()
    #     self.assertEqual(driver.find_element_by_tag_name('h2').text, 'RECUPERAÇÃO DE SENHA')

if __name__ == '__main__':
    TesteLogin()