
from features.page_objects.Loja.pages.home import *
from features.page_objects.Loja.pages.login import *
from features.page_objects.Loja.pages.produtos import *
class LojaIndex():

    def __init__(self, context):
        self.home = LojaHome(context)
        self.login = LojaLogin(context)
        self.produtos = LojaProduto(context)
