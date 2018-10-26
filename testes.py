#teste abrindo janela

#importação da biblioteca
import pygame
pygame.init()
#definição de titulo
titulo = "Carrera de la Cucaracha"
largura = 800
altura = 600

fundo = pygame.image.load('img/fundo.png')
tela = pygame.display.set_mode((largura, altura), 0, 32)
pygame.display.set_caption(titulo)
tela.blit(fundo, (9, 4))
Sair = True
while Sair:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Sair = False
#configuração de teclas inicais do MENU
    #tecla enter para avançar.
    #substituir tecla enter para qualquer tecla
    #definir tecla enter para iniciar a classe jogo
    #qualquer tecla para vançar da introdução para o menu

    #OBS : SUBSTITUIR COMANDO pygame.key.set_mods( ) PARA USAR COMO TECLAS TEMPORARIAS PARA
    #REUTILIZAR AS TECLAS DENTRO DA CLASSE JOGO. E PARA QUE AS TECLAS DEFINIDAS
    #DENTRO DESTE WHILE SEJA APENAS PARA O MENU E NAO PARA TODO O CODIGO ESTRUTURAL DO JOGO

    if(pygame.key.get_pressed()[pygame.K_RETURN]):
        fundo = pygame.image.load('img/quarto.JPG')
        tela.blit(fundo, (99, 76))
        #tecla esc para  sair do jogo
    if(pygame.key.get_pressed()[pygame.K_ESCAPE]):
        # funçao update para atualizar a tela de acordo com a chamada de imagem definida.
        Sair = False
        #substituir a função print tecla o para abrir as opções do jogo
    if(pygame.key.get_pressed()[pygame.K_o]):
        print("tecla de opção foi definida, mas nao possui imagem")
        # funçao update para atualizar a tela de acordo com a chamada de imagem definida.
        pygame.display.update()
    # substituir função print por imagem da opção da loja
    if(pygame.key.get_pressed()[pygame.K_l]):
        print("tecla da loja foi pressionada, porem nenhuma imagem foi carregada ainda.")
        # funçao update para atualizar a tela de acordo com a chamada de imagem definida.
        pygame.display.update()
   #tecla de apagar funcionando como tecla para voltar ao  menu quando alguma opção for selecionada.
    if(pygame.key.get_pressed()[pygame.K_BACKSPACE]):
        fundo = pygame.image.load('img/quarto.JPG')
        tela.blit(fundo, (99, 76))
        #funçao update para atualizar a tela de acordo com a chamada de imagem definida.
        pygame.display.update()


pygame.quit()