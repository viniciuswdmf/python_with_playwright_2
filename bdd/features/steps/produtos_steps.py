from behave import given, when, then
import time

@when(u'clicar no botao adicionar produto')
def clicar_adicionar_produto(context):
    context.Loja.home.acessar_cadastro_produto(context)


@when(u'preencher as informaçoes do mesmo')
def adicionar_produto(context):
    context.Loja.produtos.cadastrar_produto(context, 'TV LCD TESTE QA', '200,00', 'Preta')

@then(u'o produto deve ser cadastrado')
def validar_cadastro(context):
    context.Loja.produtos.validar_produto_ok(context)

################exclusao steps

@when(u'clicar no icone de exclusao')
def excluir_item(context):
    context.Loja.home.excluir_primeiro_item(context)


@then(u'o produto devera ser excluido')
def validar_item_excluido(context):
    context.Loja.home.validar_exclusao_primeiro_item(context)