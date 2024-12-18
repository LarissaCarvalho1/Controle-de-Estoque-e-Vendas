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

# Base de dados
estoque = [{'nome_produto': 'Celular', 'preco': 1500.00, 'quantidade': 10}]
vendas = []

# Inicialização do sistema
def main():
    while True:
        titulo('CONTROLE DE ESTOQUE E VENDAS')
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
            mostrar_erro('Operação selecionada não é válida. \nTente novamente!')

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
            visualizar_vendas()
        else:
            mostrar_erro('Operação selecionada não é válida. \nTente novamente!')

def adicionar_produto():
    titulo('ADICIONAR NOVO PRODUTO')
    while True:
        nome = str(input('Nome do Produto: ')).strip().capitalize()

        if nome == '':
            print('\nO nome não pode estar vazio!\n')
            continue

        for produto in estoque:
            if produto['nome_produto'] == nome:
                print('\nProduto já cadastrado no sistema! \nUtilize a opção ATUALIZAR PRODUTO.\n')
                return
        try:
            preco = float(input('Preço do Produto: '))
            quantidade = int(input('Quantidade em Estoque: '))
            if preco <= 0 or quantidade <= 0:
                mostrar_erro('Preço e quantidade devem ser maior que zero (0)!')
                continue
        except ValueError:
            mostrar_erro('Digite valores numéricos válidos para preço e quantidade.')
            continue
        novo_produto = {
            'nome_produto': nome, 
            'preco': preco, 
            'quantidade': quantidade
        }
        estoque.append(novo_produto)
        print(f'\nProduto: {nome} ADICIONADO com SUCESSO!\n')

        if not confirmar_acao('Cadastrar outro produto?'):
            pausa()
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
            if novo_preco <= 0 or nova_quantidade <= 0:
                mostrar_erro('Preço e quantidade devem ser maior que zero (0)!')
                continue
            else:
                produto_encontrado['preco'] = novo_preco
                produto_encontrado['quantidade'] = nova_quantidade
                print(f'\nProduto: {nome} ATUALIZADO com SUCESSO!\n')
        except ValueError:
            mostrar_erro('Preço e Quantidade devem ser valores numéricos')
            continue

        if not confirmar_acao('Atualizar outro produto?'):
            pausa()
            break
    
def excluir_produto():
    titulo('EXCLUIR PRODUTO')
    while True:
        nome = str(input('Nome do produto a ser excluído: ')).strip().capitalize()

        for produto in estoque:
            if produto['nome_produto'] == nome:
                estoque.remove(produto)
                print(f'\nProduto {nome} REMOVIDO com SUCESSO!\n')
                break
        else:
            print('\nProduto não encontrado!\n')
            return
        
        if not confirmar_acao('Excluir outro produto?'):
            pausa()
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
            pausa()
    aguardar_enter()

def registrar_venda():
    titulo('REGISTRAR VENDA')
    while True:
        nome_cliente = str(input('Nome do Cliente: ')).strip().capitalize()
        nome_produto_venda = str(input('Produto: ')).strip().capitalize()
        produto_encontrado = None

        # Verifica se o nome_produto_venda digitado pelo usuário faz parte da lista estoque
        for produto in estoque:
            if produto['nome_produto'] == nome_produto_venda:
                produto_encontrado = produto
                break
        if not produto_encontrado:
            print(f'Produto: {nome_produto_venda} NÃO encontrado no estoque!')
            break
        if produto_encontrado['quantidade'] == 0:
            print(f'Produto {produto_encontrado["nome_produto"]} está sem estoque!')
            break

        print(f'Preço: R$ {produto_encontrado["preco"]:.2f}')
        print(f'Estoque disponível: {produto_encontrado["quantidade"]}')

        # Valida quantidade de produtos comprados
        while True:
            try:
                quantidade_compra = int(input('Quantidade de produtos comprados: '))
                if quantidade_compra <= 0:
                    mostrar_erro('A quantidade deve ser maior que zero.')
                elif quantidade_compra > produto_encontrado['quantidade']:
                    mostrar_erro('A quantidade solicitada excede o estoque disponével.')
                else:
                    break
            except ValueError:
                mostrar_erro('Insira um número válido para a quantidade.')
                continue
        
        if confirmar_acao('Finalizar Compra?'): 
            produto_encontrado['quantidade'] -= quantidade_compra
            total_compra = produto_encontrado['preco'] * quantidade_compra
            nova_venda = {
                'cliente': nome_cliente,
                'produto': produto_encontrado['nome_produto'],
                'preco': produto_encontrado['preco'],
                'quantidade': quantidade_compra,
                'total': total_compra
            }
            vendas.append(nova_venda)
            print('\nCompra realizada com SUCESSO!\n')
        else:
            print('\nCompra cancelada!\n')

        if not confirmar_acao('REGISTRAR outra venda?'):
            pausa()
            break

def visualizar_vendas():
    titulo('VENDAS REALIZADAS')
    if not vendas:
        print('Nenhuma venda realizada!')
    else:
        for venda in vendas:
            print(f'Cliente: {venda["cliente"]}')
            print(f'Produto: {venda["produto"]}')
            print(f'Preço: {venda["preco"]:.2f}')
            print(f'Quantidade: {venda["quantidade"]}')
            print(f'Total: {venda["total"]:.2f}')
            print('--'*26)
            pausa()
    aguardar_enter()

def titulo(txt):
    print('--'*26)
    print(f"|{txt:^50}|")
    print('--'*26)

def aguardar_enter():
    while True:
        resposta = str(input('Pressione Enter para voltar ao menu. ')).strip()
        if resposta == '':
            break
        else:
            mostrar_erro('Não digite nada, apenas pressione Enter.')

def mostrar_erro(mensagem):
    print(f'\nERRO: {mensagem}\n')

def confirmar_acao(mensagem):
    while True:
        resposta = str(input(f'{mensagem} [S/N] ')).strip().upper()
        if resposta in ['S', 'N']:
            return resposta == 'S'

        mostrar_erro('Escolha apenas [S] ou [N] para prosseguir.')

def pausa():
    sleep(1)
main()