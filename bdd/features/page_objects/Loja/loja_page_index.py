from features.page_objects.Loja.pages.login import *
from features.page_objects.Loja.pages.commons import *
from features.page_objects.Loja.pages.home import *
from features.page_objects.Loja.pages.movimentacao import *
from features.page_objects.Loja.pages.extrato import *
from features.page_objects.Loja.pages.conta import *
from features.page_objects.Loja.pages.registro import *

class LojaIndex():

    def __init__(self, context):
        self.commons = LojaCommons(context)
        self.home = LojaHome(context)
        self.login = LojaLogin(context)
        self.movimentacao = LojaMovimentacao(context)
        self.extrato = LojaExtrato(context)
        self.conta = LojaConta(context)
        self.registro = LojaRegistro(context)
