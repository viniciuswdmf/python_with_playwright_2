from features.helper.page_helper import *
from features.page_objects.Loja.pages.components.el_home import *
from features.page_objects.Loja.pages.components.el_login import *
from playwright.sync_api import expect
import time

class LojaLogin():
    
    def __init__(self, context):
        pass

    def acessar_site_login(self, context):
        context.page_helper.acessar(context, "")
        

    def fazer_login_com_parametros(self, context, user, senha):
        context.page.fill(login_elements['INP_LOGIN'], user)
        context.page.fill(login_elements['INP_SENHA'], senha)
        context.page.click(login_elements['INP_BTN_LOGIN']) 
        time.sleep(8)
    
    def fazer_login_sem_sucesso(self, context, login):
        context.page.fill(login_elements['INP_LOGIN'], login)  
        context.page.click(login_elements['INP_BTN_LOGIN']) 

    def validar_login_sem_sucesso(self, context, mensagem):
        locator = context.page.locator(login_elements['TOAST_ERRO'])
        expect(locator).to_have_text(mensagem)
    # def validar_login_correto(self, context):
    #     locator = context.page.locator(home_elements['TOAST_SUCESS'])
    #     expect(locator).to_be_visible()

