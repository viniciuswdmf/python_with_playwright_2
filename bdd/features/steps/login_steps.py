from behave import given, when , then
import time


@when(u'realizar login com user e senha válidos')
def realizar_login_teste(context):
    context.Loja.login.acessar_site_login(context)
    context.Loja.login.fazer_login_com_parametros(context, "admin", "admin")

@then(u'deve validar que o login foi realizado com sucesso')
def validar_login(context):
    context.Loja.home.validar_usuario_logado(context)

@when(u'realizar login com "{login}" invalido')
def fazer_login_invalido(context, login):
    context.Loja.login.acessar_site_login(context)
    context.Loja.login.fazer_login_sem_sucesso(context, login)


@then(u'deve ser retornada a "{mensagem}" de erro')
def validar_login_invalido(context, mensagem):
    context.Loja.login.validar_login_sem_sucesso(context, mensagem)