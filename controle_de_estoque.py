MENU = """-=- Menu serviços -=-

1 - Adicionar Produto
2 - Atualizar Produto
3 - Excluir Produto
4 - Visualizar Estoque
5 - Registrar Venda
6 - Visualizar Vendas
0 - Sair do Sistema
"""

ERRO = """"
Desculpe, a operação selecionada não é válida.
Tente novamente!
"""

def operacao_selecionada(operacao):
    match operacao:
        case '1':
            print('Você clicou em Add Produto')
        case '2':
            print('Você clicou em Atualizar Produto')
        case '3':
            print('Você clicou em Excluir Produto')
        case '4':
            print('Você clicou em Visualizar Estoque')
        case '5':
            print('Você clicou em Registrar Vendas')
        case '6':
            print('Você clicou em Visualizar Vendas')
        case '0':
            print('Saindo do sistema...')
        case _:
            print(ERRO)

# Ponto de entrada no sistema
def main():
    print('Controle de Estoque')
    print('--'*20)
    print(MENU)
    operacao = input('Escolha um dos serviços acima: ')

    if operacao in ['1', '2', '3', '4','5', '6', '0']:
        operacao_selecionada(operacao)
    else:
        print(ERRO)

main()



