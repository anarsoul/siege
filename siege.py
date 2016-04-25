#!/usr/bin/env python2

import os, sys
import pygame

screen = None
clock = None
brick = None
enemy = None
player = None
bomb = None

def init(width, height):
	global screen, clock, brick, enemy, player, bomb
	pygame.init()
	screen = pygame.display.set_mode((width, height))
	clock = pygame.time.Clock()
	brick = pygame.image.load("img/brick.png")
	enemy = (pygame.image.load("img/enemy-1.png"), pygame.image.load("img/enemy-2.png"))
	player = pygame.image.load("img/player.png")
	bomb = pygame.image.load("img/bomb.png")

def drawWall():
	for x in range(0, 640, 16):
		for y in range(16 * 3, 480, 16):
			screen.blit(brick, [x, y])

def drawPlayer(x, y):
	screen.blit(player, [x, y])
	screen.blit(bomb, [x, y - 16])

def mainLoop():
	done = False
	keysPressed = []
	x = 0
	y = 16 * 2
	BLUE = (0, 0, 192) # Red, Green, Blue
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT or pygame.K_LEFT:
					if event.key not in keysPressed:
						keysPressed.append(event.key)
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT or pygame.K_LEFT:
					keysPressed.remove(event.key)
		if pygame.K_RIGHT in keysPressed and x != 640 - 16:
			x += 4
		if pygame.K_LEFT in keysPressed and x != 0:
			x -= 4
		screen.fill(BLUE)
		drawWall()
		drawPlayer(x, y)
		pygame.display.flip()
		clock.tick(60)


init(640, 480)
mainLoop()
