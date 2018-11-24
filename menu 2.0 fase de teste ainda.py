import pygame, sys, os,text
from gameManager import CloseWindow
from gameManager import Gerenciador
import new1 import new1 


titulo = "Carrera de la Cucaracha"
telaLargura = 1024
telaAltura = 768
branco = (255,255,255)

pygame.init()

pygame.display.set_caption(titulo)
tela = pygame.display.set_mode((telaLargura, telaAltura), 0, 32)

pygame.mixer.init()

#==================== controla a troca de imagens do menu =====================
telas = ['img/fundo.png', 'img/quarto.PNG', 'img/loja.png', ]
telaAtual = 0
podeTrocar = True
# ==============================================================================

# =================== menu sound effects =================================
Move = os.path.join()
MoveSound = pygame.mixer.Sound(Move)
#MoveSound.set_volume(2.0)

Select = os.path.join()
SelectSound = pygame.mixer.Sound(Select)
#SelectSound.set_volume(2.0)

Cancel = os.path.join()
CancelSound = pygame.mixer.Sound(Cancel)
#CancelSound.set_volume(2.0)

BackSound = os.path.join('Sons/La-Cucaracha.mp3')
MenuBackS = pygame.mixer.Sound(BackSound)
MenuBackS.set_volume(0.2)


#ajustaimagem   da telas para plano definido.
#=============================================================================
def ajustaimagem(img):
    global largura, altura, fundo
    telas = pygame.image.load(img)
    telas = pygame.transform.scale(fundo, (telaLargura, telaAltura))

# =============================================================================

# evento e troca imagens cenarios pré estabelecidos
def trocarMenu():
	global telaAtual, podeTrocar,MoveSound,SelectSound,CancelSound,MenuBackS

	for event in pygame.event.get():

		if event.type == pygame.KEYDOWN:

			# =============== mover a selecao (L e R) ==========================
			if event.key == pygame.K_LEFT and podeTrocar:

				if telaAtual > 0:
					MoveSound.play()
					telaAtual -= 1

			elif event.key == pygame.K_RIGHT and podeTrocar:
				if telaAtual < 3:
					MoveSound.play()
					telaAtual += 1
			# =========================================================================

			# ==================  mostra a tela controls =================================
			if (event.key == pygame.K_SPACE ) and (telaAtual == 2):
				SelectSound.play()
				podeTrocar = False
				telaAtual = 4
			# ============================================================================

			# ========== se tela atual for control a acao volta ao menu principal ============
			if telaAtual == 4 and event.key == pygame.K_ESCAPE:
					CancelSound.play()
					podeTrocar = True
					telaAtual = 0
			# ===============================================================================

			# ==================== fecha o game caso selecione exit ======================
			if telaAtual == 3 and event.key == pygame.K_SPACE:
				pygame.quit()
				sys.exit()

			# ================= saltar menu e iniciar o jogo ========================
			if (telaAtual == 0) and (event.key == pygame.K_SPACE):
				MenuBackS.stop()
				#audio = False
				Gerenciador.gameMode = 'easy'
				Gerenciador.onMenu = False
			elif (telaAtual == 1) and (event.key == pygame.K_SPACE):
				MenuBackS.stop()
				#audio = False
				Gerenciador.gameMode = 'hard'
				Gerenciador.onMenu = False
			# ========================================================================

audio = False

def Menu(tela):

	global telaAtual,telas,audio,MenuBackS

	if audio == False:
		MenuBackS.play(-1)
		audio = True

	caminhoMenu = os.path.join('quarto.PNG',telas[telaAtual])
	imgMenu = pygame.image.load(caminhoMenu)

	tela.blit(imgMenu,(0,0))

	if telaAtual != 4:
		text.ExibirTexto(tela,'Press SPACE to select.',0,0,0)
	elif
		text.ExibirTexto(tela,'Press ESC to back.',0,0,0)
	elif
		text.ExibirTexto(tela,' Press ENTER to start.', 0,0,0)#

	CloseWindow()

	trocarMenu()
	
	
def game_intro():
    gameintro = True
    while gameintro:
        screen.blit(Menu, (0, 0))
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if keys[pg.K_j]:
                gameintro = False
            elif keys[pg.K_t]:  # apertar T para tto
                gameintro = False
            elif keys[pg.K_i]:  # apertar I de intro
                game_story()
        pg.display.update()

def game_story():
    pass

	pygame.display.flip()