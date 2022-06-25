import pygame
import math

pygame.init()

# set up display
WIDTH, HEIGHT = 800, 500
SCREEN = (WIDTH, HEIGHT)
win = pygame.display.set_mode(SCREEN)
pygame.display.set_caption('Hangman Game!')

# fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# load images
images: list = []
for i in range(7):
	image = pygame.image.load(f'images/hangman{i}.png')
	images.append(image)

# game variables
hangman_status = 0 # the first doll
word: str = 'DEVELOPER'
guessed: list = []

# button variables
RADIUS = 20
GAP = 15
letters: list = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
	x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
	y = starty + ((i // 13) * (GAP + RADIUS * 2))
	letters.append([x, y, chr(A + i), True])

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw():
	win.fill(WHITE)
	
	# draw title
	text = TITLE_FONT.render('Hangman Game!', 1, BLACK)
	win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

	# draw word
	display_word = ''
	for letter in word:
		if letter in guessed:
			display_word += letter + ' '
		else:
			display_word += '_ '
	text = WORD_FONT.render(display_word, 1, BLACK)
	win.blit(text, (400, 200))

	# draw buttons
	for letter in letters:
		x, y, ltr, visible = letter
		if visible:
			pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
			text = LETTER_FONT.render(ltr, 1, BLACK)
			win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

	win.blit(images[hangman_status], (150, 100))
	pygame.display.update()


def end_game_message(msg):
	win.fill(WHITE)
	text = WORD_FONT.render(msg, 1, BLACK)
	win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
	pygame.display.update()
	pygame.time.delay(3000)


def main():
	FPS = 60
	clock = pygame.time.Clock()

	run = True
	while run:
		global hangman_status, guessed

		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				m_x, m_y = pygame.mouse.get_pos()
				for letter in letters:
					x, y, ltr, visible = letter
					if visible:
						dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
						if dis < RADIUS:
							letter[3] = False
							guessed.append(ltr)
							if ltr not in word:
								hangman_status += 1

		draw()

		won = True
		for letter in word:
			if letter not in guessed:
				won = False
				break

		if won:
			end_game_message('You won!! :)')
			break

		if hangman_status == 6:
			end_game_message('You lost! :C')
			break

	pygame.quit()


if __name__ == '__main__':
	main()
