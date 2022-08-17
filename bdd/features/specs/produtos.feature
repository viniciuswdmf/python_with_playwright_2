#language: pt

Funcionalidade: Administraçao de produtos
    Como um usuario da Loja
    Quero gerenciar os produtos
    Para poder atualizar e inserir suas informaçoes

Contexto: Estar logado
    Dado que esteja logado

# Cenário: Adicionar produto
#     Quando clicar no botao adicionar produto
#     E preencher as informaçoes do mesmo
#     Então o produto deve ser cadastrado

Cenário: Excluir produto
    Quando clicar no icone de exclusao
    Então o produto devera ser excluido