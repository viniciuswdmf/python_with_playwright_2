from features.helper.page_helper import *
from features.page_objects.Loja.pages.components.el_home import *
from features.page_objects.Loja.pages.components.el_login import *
from features.page_objects.Loja.pages.components.el_produtos import *
from playwright.sync_api import expect
import time

class LojaProduto():
    
    def __init__(self, context):
        pass

    def cadastrar_produto(self, context, nome, valor, cor):
        context.page.fill(produto_elements['INP_PRODUTO_NOME'], nome)
        context.page.fill(produto_elements['INP_PRODUTO_VALOR'], valor)
        context.page.fill(produto_elements['INP_PRODUTO_COR'], cor)
        context.page.click(produto_elements['BTN_SALVAR']) 
    
    def validar_produto_ok(self, context):
        locator = context.page.locator(produto_elements['TOAST_SUCCESS'])
        expect(locator).to_be_visible()

    def alterar_produto(self, context, nome, valor, cor):
        context.page.fill(produto_elements['INP_PRODUTO_NOME'], nome)
        context.page.fill(produto_elements['INP_PRODUTO_VALOR'], valor)
        context.page.fill(produto_elements['INP_PRODUTO_COR'], cor)
        context.page.click(produto_elements['BTN_SALVAR']) 

    

    
