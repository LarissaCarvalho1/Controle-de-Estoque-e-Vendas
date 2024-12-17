from time import sleep

MENU = """
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
estoque = [{'nome_produto': 'Celular', 'preco': 1500.00, 'quantidade': 150}]
vendas = []

# Ponto de entrada no sistema
def main():
    while True:
        titulo('CONTROLE DE ESTOQUE')
        print(f"{'SERVIÇOS DISPONÍVEIS':^50}")
        print(MENU)
        operacao = input('Escolha um dos serviços: ')

        if operacao in ['1', '2', '3', '4','5', '6', '0']:
            if operacao == '0':
                print('\nSaindo do sistema...\n')
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
            registrar_venda()
        elif operacao == '6':
            print('Você clicou em Visualizar Vendas')
        else:
            print('Desculpe, a operação selecionada não é válida. Tente novamente!')

def adicionar_produto():
    titulo('ADICIONAR NOVO PRODUTO')
    while True:
        nome_produto = str(input('Nome do Produto: ')).strip().capitalize()

        for produto in estoque:
            if produto['nome_produto'] == nome_produto:
                print('\nProduto já cadastrado no sistema! Utilize a opção de atualizar.\n')
                return
        #Solicita as informações de preco e quantidade
        try:
            preco = float(input('Preço do Produto: '))
            quantidade = int(input('Quantidade em Estoque: '))
        except ValueError:
            print('\nERRO: Digite valores numéricos válidos para preço e quantidade.\n')
            continue
        # Cria e add novo produto ao estoque
        novo_produto = {
            'nome_produto': nome_produto, 
            'preco': preco, 
            'quantidade': quantidade
        }
        estoque.append(novo_produto)
        print(f'\nProduto: {nome_produto} adicionado com sucesso!\n')

        while True:
            resposta = str(input('Deseja cadastrar mais produtos? [S/N] ')).upper().strip()
            if resposta in ['S', 'N']:
                break
            else:
                print('\nERRO: Escolha apenas [S] ou [N] para prosseguir.\n')
        
        if resposta == 'N':
            break

def atualizar_produto():
    titulo('ATUALIZAR PRODUTO')
    while True:
        nome = str(input('Nome do produto a ser atualizado: ')).strip().capitalize()
        produto_encontrado = None

        for produto in estoque:
            if produto['nome_produto'] == nome:
                produto_encontrado = produto
                break

        if not produto_encontrado:
            print(f'\nProduto {nome} NÃO encontrado no estoque!\n')
            break

        try:
            novo_preco = float(input('Novo Preço: '))
            nova_quantidade = int(input('Nova Quantidade: '))
            produto_encontrado['preco'] = novo_preco
            produto_encontrado['quantidade'] = nova_quantidade
            print(f'\nProduto: {nome} atualizado com SUCESSO!\n')
        except ValueError:
            print('\nERRO: Preço e Quantidade devem ser valores numéricos\n')
            continue

        while True:
            resposta = str(input('Deseja atualizar mais produtos? [S/N] ')).strip().upper()
            if resposta in ['S', 'N']:
                break
            else:
                print('\nERRO: Escolha apenas [S] ou [N] para prosseguir.\n')
        
        if resposta == 'N':
            break
    
def excluir_produto():
    titulo('EXCLUIR PRODUTO')
    while True:
        nome = str(input('Nome do produto a ser excluído: ')).strip().capitalize()

        for produto in estoque:
            if produto['nome_produto'] == nome:
                estoque.remove(produto)
                print(f'\nProduto {nome} removido com sucesso!\n')
                break
        else:
            print('\nProduto não encontrado!\n')
            return

        while True:
            resposta = str(input('Deseja excluir mais itens? [S/N] ')).strip().upper()
            if resposta in ['S', 'N']:
                break
            elif resposta != 'S':
                print('\nERRO: Escolha apenas [S] ou [N] para prosseguir.\n')

        if resposta == 'N':
            print('\nEncerrando a exclusão de produtos...\n')
            break
                
def visualizar_estoque():
    titulo('ESTOQUE')
    if not estoque:
        print('Estoque vazio!')
    else:
        for produto in estoque:
            print(f'Produto: {produto['nome_produto']}')
            print(f'Preço: {produto['preco']:.2f}')
            print(f'Quantidade: {produto['quantidade']}')
            print('--'*26)

    while True:
        resposta = str(input('Pressione Enter para voltar ao menu. ')).strip()
        if resposta == '':
            break
        else:
            print('\nERRO: Não digite nada, apenas pressione Enter.\n')

def registrar_venda():
    titulo('REGISTRAR VENDA')
    while True:
        nome_cliente = str(input('Nome do Cliente: ')).strip()
        nome_produto_venda = str(input('Produto: ')).strip().capitalize()
        produto_encontrado = None

        for produto in estoque:
            if produto['nome_produto'] == nome_produto_venda:
                produto_encontrado = produto
                break

        if not produto_encontrado:
            print(f'Produto: {nome_produto_venda} NÃO encontrado no estoque!')
            break

        if produto_encontrado['quantidade'] != 0:
            print(f'No estoque há {produto_encontrado['quantidade']} produto {produto_encontrado['nome_produto']} ')
            break



def visualizar_vendas():
    print('Visualizar vendas')

def titulo(txt):
    print('--'*26)
    print(f"|{txt:^50}|")
    print('--'*26)

main()



