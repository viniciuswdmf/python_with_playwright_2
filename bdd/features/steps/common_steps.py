from behave import given, when, then
import time

@given(u'que esteja logado')
def estar_logado(context):
    context.Loja.login.acessar_site_login(context)
    context.Loja.login.fazer_login_com_parametros(context, "admin", "admin")