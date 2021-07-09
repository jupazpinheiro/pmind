import pygame, sys
from pygame.locals import *

def draw_grid():
    screen.fill(BLACK)
    for y in range(height, h, height):#horizontal lines
        pygame.draw.line(screen, bg, (width, y), (w - width, y), 1)
    for x in range(width, w, width):#vertical lines
        pygame.draw.line(screen, bg, (x, height), (x, h - height), 1)

def draw_player():
    pygame.draw.rect(screen, [255, 255, 55], [left, top, width, height], 0)

# Mostra a tela final com a pontução obtida. Representa o placar final.
def mostra_pontuacao_final(screen, pokemonCount):
    sys.stdout.write("Capturas: " + str(pokemonCount) + " Pokemons ")

pygame.init()
clock = pygame.time.Clock()
w = 80
h = 80
left = 20
top = 40
width = 20
height = 20
YELLOW = (255, 255, 55)
branco = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
bg = (255, 255, 255)
x = 0
y = 0
isFirstPokemon = True
bulbassauro = 1
charmander = 1
squirtle = 1
pikachu = 1
pokemonCount = 0
screen = pygame.display.set_mode((600, 600))
gameExit = False
mostra_pontuacao_final(screen, pokemonCount)

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if isFirstPokemon and top == 40 and left == 20:
            pokemonCount += 1
            isFirstPokemon = False
            bulbassauro -= 1
        if event.type == KEYDOWN:
            if event.key == K_DOWN and top < 40:
                print("Orientação: S");
                if bulbassauro > 0 and top == 20 and left == 20:  # Bulbassauro
                    pokemonCount += 1
                    bulbassauro -= 1
                elif charmander > 0 and top == 20 and left == 40:  # charmander
                    pokemonCount += 1
                    charmander -= 1
                top += 20
            if event.key == K_UP and top > 20:
                print("Orientação: N");
                if squirtle > 0 and top == 40 and left == 40:  # squirtle
                    pokemonCount += 1
                    squirtle -= 1
                elif pikachu > 0 and top == 40 and left == 20:  # pikachu
                    pokemonCount += 1
                    pikachu -= 1
                top -= 20
            if event.key == K_RIGHT and left < 40:
                print("Orientação: E");
                if charmander > 0 and top == 40 and left == 20:  # charmander
                    pokemonCount += 1
                    charmander -= 1
                elif squirtle > 0 and top == 20 and left == 20:  # squirtle
                    pokemonCount += 1
                    squirtle -= 1
                left += 20
            if event.key == K_LEFT and left > 20:
                print("Orientação: O");
                if bulbassauro > 0 and top == 40 and left == 40:  # Bulbassauro
                    pokemonCount += 1
                    bulbassauro -= 1
                elif pikachu > 0 and top == 20 and left == 40:  # pikachu
                    pokemonCount += 1
                    pikachu -= 1
                left -= 20
            mostra_pontuacao_final(screen, pokemonCount)


    draw_grid()
    draw_player()
    pygame.display.flip()

pygame.quit()
