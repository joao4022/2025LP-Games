''''
Game Par ou Ímpar V.1.0
2025.06.25
Profe. Berssa
'''

# OBJETIVO: Desenvolver um Jogo onde o Jogador escolhe Par ou Ímpar e faz sua Jogada, o PC sorteia um Número entre 1 e 10 e soma com a Jogada do Jogador, se o resultado for Par e o Jogador escolheu Par, ele ganha, se for Ímpar e o Jogador escolheu Ímpar, ele ganha, caso contrário o PC ganha. 

# BIBLIOTECAS
from modules import limpaTela, mostraCabecalho, mostraMenu, getValue, validaValue, sortNum, playAgain

# CONSTANTES
limite = 10  # Limite do Sorteio (1 a 10)

# VARIÁVEIS
escolha = ''  # Variável que guarda a escolha do Jogador (Par ou Ímpar)
msg = ''  # Variável que guarda a mensagem

# LISTAS
msgsCab = ['JOGO PAR OU ÍMPAR', 'Desenvolvido por Profe. Berssa']  
msgsMenu = ['Escolha:', '[0] para Par', '[1] para Ímpar']

# FUNÇÃO PRINCIPAL DO JOGO
def playGame():
    global escolha, msg, msgsCab, msgsMenu
    limpaTela()
    mostraCabecalho(msgsCab)  # Mostra o Cabeçalho do Jogo
    mostraMenu(msgsMenu)
    msg = '-> Sua escolha: '
    escolha = getValue(msg)
    opcoes = ['0', '1'] 
    while not validaValue(escolha, opcoes):
        escolha = getValue(msg)
    if escolha == '0':
        escolhaTexto = 'Par'
    else:
        escolhaTexto = 'Ímpar'
    msg = '-> Sua Jogada: '
    userJogada = getValue(msg)
    while not userJogada.isdigit():
        userJogada = getValue(msg)
    userJogada = int(userJogada)  # Converte a Jogada do Jogador para inteiro
    pcJogada = sortNum(limite)  # Sorteia um número entre 1 e 10 para o PC
    result = userJogada + pcJogada  # Soma a Jogada do Jogador com a Jogada do PC
    if (result%2 == 0 and escolha == '0') or (result%2 != 0 and escolha == '1'):
        ganhador = 'Jogador'
    else:
        ganhador = 'PC'
    MSGS = [f'PC Jogou: {pcJogada}',
            f'Jogador Jogou: {userJogada}',
            f'Resultado: {result}',
            f'Escolha do Jogador: {escolhaTexto}',
            f'Escolha do PC: {"Par" if escolha == "1" else "Ímpar"}',
            f'Ganhador: {ganhador}'
            ]
    mostraCabecalho(MSGS)  # Mostra o resultado do Jogo
    # Pergunta se o jogador deseja jogar novamente
    if playAgain():
        playGame()
    else:
        # Mensagem de despedida
        mostraCabecalho(['Obrigado por jogar!', 'Até a próxima!'])

        
# CÓDIGO PRINCIPAL
playGame()  # Chama a função principal do Jogo