#language: pt

Funcionalidade: Login no site da Loja
    Como um usuario da Loja
    Quero efetuar Login
    Para poder utilizar as funcionalidades da mesma

Cenário: Realizar login com sucesso
    Quando realizar login com user e senha válidos
    Então deve validar que o login foi realizado com sucesso

Esquema do Cenário: Realizar login com erro
    Quando realizar login com "<login>" invalido
    Então deve ser retornada a "<mensagem>" de erro
    Exemplos:
        | login           | mensagem                |
        | 78578           | Falha ao fazer o login  |