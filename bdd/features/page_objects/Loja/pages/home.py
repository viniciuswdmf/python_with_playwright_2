from features.helper.page_helper import *
from features.page_objects.Loja.pages.components.el_home import *
from features.page_objects.Loja.pages.components.el_login import *
from playwright.sync_api import expect
import time

class LojaHome():
    
    def __init__(self, context):
        pass

    def validar_usuario_logado(self, context):
        locator = context.page.locator(home_elements['NAV_USUARIO_LOGADO'])
        expect(locator).to_have_text('Boas vindas, admin!')

    def acessar_cadastro_produto(self, context):
        context.page.click(home_elements['BTN_ADICIONAR_PRODUTO']) 

    def excluir_primeiro_item(self, context):
        context.page.click(home_elements['BTN_EXCLUIR_PRIMEIRO_ITEM'])
    
    def validar_exclusao_primeiro_item(self, context):
        locator = context.page.locator(home_elements['TOAST_EXCLUSAO'])
        expect(locator).to_be_visible()

    def selecionar_primeiro_item(self, context):
        context.page.click(home_elements['LINK_PRIMEIRO_PRODUTO'])
    
#     def acessar_extrato(self, context):
#         context.page.click(home_elements['MENU_EXTRATO'])
#         time.sleep(5)

#     def acessar_conta(self, context):
#         context.page.click(home_elements['DROPDOWN_MENU'])
#         time.sleep(3)
#         context.page.click(home_elements['MENU_CONTA'])
#         time.sleep(5)

#     def acessar_registro(self, context):
#         context.page.click(home_elements['MENU_REGISTRO'])

#     def resetar_infos(self, context):
#         context.page.click(home_elements['DROPDOWN_MENU'])
#         time.sleep(3)
#         context.page.click(home_elements['MENU_RESET'])

