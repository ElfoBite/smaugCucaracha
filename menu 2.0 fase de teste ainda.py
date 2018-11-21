import pygame, sys, os,text
from gameManager import CloseWindow
from gameManager import Gerenciador

pygame.mixer.init()

#==================== controla a troca de imagens do menu =====================
telas = []
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

BackSound = os.path.join()
MenuBackS = pygame.mixer.Sound(BackSound)
MenuBackS.set_volume(0.2)

# =============================================================================


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

	caminhoMenu = os.path.join('menu_imgs',telas[telaAtual])
	imgMenu = pygame.image.load(caminhoMenu)

	tela.blit(imgMenu,(0,0))

	if telaAtual != 4:
		text.ExibirTexto(tela,'Press SPACE to select.',235,570,15)
	else:
		text.ExibirTexto(tela,'Press ESC to back.',270,570,15)

	CloseWindow()

	trocarMenu()

	pygame.display.flip()