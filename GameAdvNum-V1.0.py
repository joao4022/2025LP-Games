''''
Projeto: Game Adivinhe o Número - V.10
2025.06.24
Profe. Berssa
'''

# Objetivo: Desenvolver um Jogo, onde o Computador sorteia 1 número 1 a 10, o Jogador terá 3 chances para adivinhar com o Jogo fornecendo dicas

# BIBLIOTECAS --> Espaço reservado para a declaração das bibliotecas e funções
from random import randint  # Importa a função randint da biblioteca random 
from time import sleep      # Importa a função sleep da biblioteca time 

# CONSTANTES --> Espaço reservado para a declaração de constantes
TAM = int(50)   # Tamanho da Tela
MAR = int(2)    # Margem da mensagem na Tela

# VARIÁVEIS --> Espaço reservado para a declaração de variáveis
key = 0         # Variável que guarda o número sorteado
resp = 0        # Variável que guarda a resposta do Jogador
vidas = 0       # Variável que guarda o número de vidas do Jogador
limite = 0      # Variável que guarda o número máximo do sorteio
tentativa = 0   # Variável que guarda o número de tentativas do Jogador
msg = ''        # Variável que guarda a mensagem

# LISTAS --> Espaço reservado para a declaração de listas
MSGS = []       # Lista que irá guardar as mensagens
# Lista que guarda msgs do cabeçalho
msgsCab = ['JOGO DO ADIVINHE O NÚMERO', 
           'Desenvolvido por Profe. Berssa'] 
# Lista que guarda msgs do menu de níveis de dificuldade
msgsLevel = ['NÍVEIS DE DIFICULDADE', 
             '[1] Fácil (1 a 10)', 
             '[2] Difícil (1 a 100)', 
             '[3] Impossível (1 a 1000)',
             'Escolha o nível de dificuldade:'] 

# FUNÇÕES DO PROJETO --> Espaço reservado para a declaração das funções do projeto
# Função para limpar a tela 
def limpaTela():
    print('\n'*TAM)     # Mostra na tela TAM(50) linhas em branco (\n)

# Função para desenhar uma linha
def mostraLine():
    print('#'*TAM)      # Mostra na tela TAM(50) caracteres '#'

# Função para mostrar uma Msg Centralizada
def msgCenter(msg):
    print(f'# {msg:^{TAM-MAR-MAR}} #') # Mostra na tela o valor do parametro msg Centralizado entre TAM(50)-MAR(2)-MAR(2)

# Função para mostrar uma Msg a Esquerda
def msgLeft(msg):
    print(f'# {msg:<{TAM-MAR-MAR}} #') # Mostra na tela o valor do parametro msg a esquerda entre TAM(50)-MAR(2)-MAR(2)

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
    resp = input(f'# {msg}: ').strip()
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


# Função Principal do Jogo
def playGame():
    global key, resp, vidas, limite, tentativa, MSGS
    limpaTela()                 # Limpa a Tela
    mostraCabecalho(msgsCab)    # Mostra o Cabeçalho do Jogo
    mostraMenu(msgsLevel)       # Mostra o Menu de Níveis de Dificuldade

    msg = '-> Digite o número correspondente ao nível'
    resp = getValue(msg)
    opcoes = ['1', '2', '3']
    while not validaValue(resp, opcoes):
        resp = getValue(msg)

    # Verifica o Nível de Dificuldade
    if resp == '1':     # Fácil
        vidas = 3  
        limite = 10
    elif resp == '2':   # Difícil
        vidas = 5 
        limite = 100
    elif resp == '3':   # Impossível
        vidas = 10
        limite = 1000

    # Chama Função que Sorteia um Número
    key = sortNum(limite)

    limpaTela()  # Limpa a tela antes de iniciar o jogo
    sleep(1)  # Pausa de 1 segundo para criar expectativa
    mostraCabecalho(msgsCab)   # Mostra o Cabeçalho do Jogo
    mostraCabecalho([f'Adivinhe o número entre 1 e {limite}', 
                     f'Você tem {vidas} tentativas']) # Exibe instruções

    # Loop de tentativas
    for tentativa in range(vidas):
        msg = f'Tentativa {tentativa+1}/{vidas} -> Seu palpite'
        resp = getValue(msg)

        # Validação de entrada numérica
        while not resp.isdigit():
            mostraCabecalho(['Entrada inválida! Por favor, insira um número.'])
            resp = getValue(msg)

        resp = int(resp)

        # Verifica se o palpite é correto
        if resp == key:
            sleep(1)
            mostraCabecalho(['Parabéns!!!', 'Você acertou o número!'])
            break
        else:
            if tentativa < vidas - 1:
                # Dica se o jogador ainda tiver tentativas
                sleep(1)
                mostraCabecalho(['Número incorreto!', 
                                 f'Você ainda tem {vidas - tentativa - 1} tentativas'])
                mostraDica(resp, key)
    else:
        # Mensagem de derrota se o jogador não acertar o número
        sleep(1)
        mostraCabecalho(['Que pena...', 
                         f'O número secreto era {key}', 'Fim de jogo!'])

    # Pergunta se o jogador deseja jogar novamente
    if playAgain():
        playGame()
    else:
        # Mensagem de despedida
        mostraCabecalho(['Obrigado por jogar!', 'Até a próxima!'])

# Início do Jogo
playGame()  # Chama a função principal para iniciar o jogo
