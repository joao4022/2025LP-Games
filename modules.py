''''
Arquivo de funções utilizadas
2025.06.25
Profe. Berssa
'''

# OBJETIVO: Criar um arquivo de funções que serão utilizadas em nossos Projetos

# BIBLIOTECAS
from random import randint  # Importa a função randint da biblioteca random

# CONSTANTES
TAM = int(50)   # Tamanho da Tela
MAR = int(2)    # Margem da mensagem na Tela
CAR = '#'       # Caractere utilizado para desenhar a linha

# VARIÁVEIS


# LISTAS



# FUNÇÕES
# Função para limpar a tela 
def limpaTela():
    print('\n'*TAM)     # Mostra na tela TAM(50) linhas em branco (\n)

# Função para desenhar uma linha
def mostraLine():
    print(f'{CAR}'*TAM)      # Mostra na tela TAM(50) caracteres '#'

# Função para mostrar uma Msg Centralizada
def msgCenter(msg):
    print(f'{CAR} {msg:^{TAM-MAR-MAR}} {CAR}') # Mostra na tela o valor do parametro msg Centralizado entre TAM(50)-MAR(2)-MAR(2)

# Função para mostrar uma Msg a Esquerda
def msgLeft(msg):
    print(f'{CAR} {msg:<{TAM-MAR-MAR}} {CAR}') # Mostra na tela o valor do parametro msg a esquerda entre TAM(50)-MAR(2)-MAR(2)

# Função para mostrar Cabeçalho
def mostraCabecalho(MSGS):
    mostraLine()            # Chama a função que mostra a linha
    for msg in MSGS:        # Itera sobre a lista MSGS
        msgCenter(msg)      # Chama a função que mostra a mensagem centralizada 
    mostraLine()            # Chama a função que mostra a linha

# Função para mostrar Menu
def mostraMenu(MSGS):   
    mostraLine()            # Chama a função que mostra a linha
    for msg in MSGS:        # Itera sobre a lista MSGS
        msgLeft(msg)        # Chama a função que mostra a mensagem a esquerda 
    mostraLine()            # Chama a função que mostra a linha

# # Função para Sortear um Número
def sortNum(limite):
    key = randint(1, limite)    # Usa a Função randint para sortear um número 
    return key                  # Retorna o número sorteado

# Função para Validar as Entradas
def validaValue(resp, opcoes):
    if resp in opcoes:
        return True
    else:
        MSGS = [f'{resp} não é uma opção válida!', 
                f'Escolha entre {opcoes}']
        mostraMenu(MSGS)
        return False

# Função para obter a entrada do usuário
def getValue(msg):
    resp = input(f'{CAR} {msg}: ').strip()
    return resp

# Função para mostrar uma dica
def mostraDica(resp, key):
    if resp > key:
        mostraCabecalho(['Tente um número menor!'])
    else:
        mostraCabecalho(['Tente um número maior!'])

# Função para perguntar se o jogador quer jogar novamente
def playAgain():
    opcoes = ['1', '0']
    mostraCabecalho(['Deseja jogar novamente?', '[1] Sim', '[0] Não'])
    resp = getValue('Escolha uma opção')
    return resp == '1'
