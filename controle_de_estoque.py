MENU = """-=- Menu serviços -=-

1 - Adicionar Produto
2 - Atualizar Produto
3 - Excluir Produto
4 - Visualizar Estoque
5 - Registrar Venda
6 - Visualizar Vendas
0 - Sair do Sistema
"""

ERRO = """
Desculpe, a operação selecionada não é válida.
Tente novamente!
"""
# Base de dados
estoque = []

# Ponto de entrada no sistema
def main():
    while True:
        print('Controle de Estoque')
        print('--'*20)
        print(MENU)
        operacao = input('Escolha um dos serviços disponíveis: ')

        if operacao in ['1', '2', '3', '4','5', '6', '0']:
            if operacao == '0':
                print('Saindo do sistema...')
                break
            else:
                operacao_selecionada(operacao)
        else:
            print(ERRO)

def operacao_selecionada(operacao):
        if operacao == '1':
            adicionar_produto()
        elif operacao == '2':
            atualizar_produto()
        elif operacao == '3':
            excluir_produto()
        elif operacao == '4':
            visualizar_estoque()
        elif operacao == '5':
            print('Você clicou em Registrar Vendas')
        elif operacao == '6':
            print('Você clicou em Visualizar Vendas')
        else:
            print('Desculpe, a operação selecionada não é válida. Tente novamente!')

def adicionar_produto():
    while True:
        nome_produto = str(input('Nome do Produto: ')).strip().capitalize()

        for produto in estoque:
            if produto['nome_produto'] == nome_produto:
                print('Produto já cadastrado no sistema! Utilize a opção de atualizar.')
                return
        #Solicita as informações de preco e quantidade
        try:
            preco = float(input('Preço do Produto: '))
            quantidade = int(input('Quantidade em Estoque: '))
        except ValueError:
            print('ERRO: Digite valores numéricos válidos para preço e quantidade.')
            continue
        # Cria e add novo produto ao estoque
        novo_produto = {
            'nome_produto': nome_produto, 
            'preco': preco, 
            'quantidade': quantidade
        }
        estoque.append(novo_produto)
        print(f'Produto {nome_produto} adicionado com sucesso!')

        resposta = str(input('Deseja cadastrar mais produtos? [S/N]')).upper().strip()
        if resposta == 'N':
            break

def atualizar_produto():
    while True:
        nome = str(input('Nome do produto a ser atualizado: ')).strip().capitalize()

        for produto in estoque:
            if produto['nome_produto'] == nome:
                try:
                    novo_preco = float(input('Novo preço do produto: '))
                    nova_quantidade = int(input('Nova quantidade em estoque: '))
                    produto['preco'] = novo_preco
                    produto['quantidade'] = nova_quantidade
                    print(f'Produto {nome} atualizado com sucesso!')
                    break
                except ValueError:
                    print('ERRO: Preço e quantidade devem ser valores numéricos.')   
                    continue      
        else:
            print('Produto não encontrado!')

        resposta = str(input('Deseja atualizar mais produtos? [S/N]')).strip().upper()
        if resposta == 'N':
            break
    
def excluir_produto():
    while True:
        nome = str(input('Nome do produto a ser excluído: ')).strip().capitalize()

        for produto in estoque:
            if produto['nome_produto'] == nome :
                estoque.remove(produto)
                print(f'Produto {nome} removido com sucesso!')
                break
        else:
            print('Produto não encontrado!')

        resposta = str(input('Deseja excluir mais itens? [S/N]')).strip().upper()
        if resposta == 'N':
            break
    
def visualizar_estoque():
        if not estoque:
            print('Estoque vazio!')
        else:
            print('=' * 15,'ESTOQUE', '=' * 15)
            for produto in estoque:
                print(f'Produto: {produto['nome_produto']}')
                print(f'Preço: {produto['preco']:.2f}')
                print(f'Quantidade: {produto['quantidade']}')
                print('-=' * 15)

        while True:
            resposta = str(input('Pressione Enter para voltar ao menu. ')).strip()
            if resposta == '':
                break
            else:
                print('ERRO: Entrada inválida! Não digite nada, apenas pressione Enter.')

main()



