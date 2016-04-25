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
	for y in range(16 * 3, 480, 16):
		screen.blit(brick, [0, y])

def drawPlayer(x, y):
	screen.blit(player, [x, y])
	screen.blit(bomb, [x, y - 16])

def mainLoop():
	done = False
	x = 0
	y = 16 * 2
	BLUE = (0, 0, 192) # Red, Green, Blue
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT and x != 640 - 16:
					x += 16
				if event.key == pygame.K_LEFT and x != 0:
					x -= 16
		screen.fill(BLUE)
		drawWall()
		drawPlayer(x, y)
		pygame.display.flip()
		clock.tick(60)


init(640, 480)
mainLoop()
