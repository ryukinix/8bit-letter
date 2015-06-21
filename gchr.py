#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from random import choice
from random import randint as rand
from pieces import pieces_dic, ascii_dic

pygame.init()
info_screen = pygame.display.Info()

PANEL = '''* ryukinix_software *    * * * * * 8bit_chars * f10 to input'''
WIDTH = int(info_screen.current_w // 1.2)
SIZE = 5
HEIGHT = 10*(SIZE - 1)*(1 + PANEL.count('\n'))


SIZESCREEN = WIDTH, HEIGHT
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

class cell(object):
	def __init__(self, x, y, size, color):
		self.rect = pygame.Rect(x, y, size, size)
		self.color = color
	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)
	def move(self, dx, dy):
		self.rect = self.rect.move(dx, dy)

class charObj(object):
	def __init__(self, x, y, piece, size):
		self.rect = pygame.Rect(x, y, size*8, size*8)
		self.char = piece
		self.size = size
		self.pulse = [5, 5, 5]
		self.setup()
	def setup(self):
		self.cells = []
		self.color = rand(0, 255), rand(0, 255), rand(0, 255)
		x, y = self.rect.x, self.rect.y
		for line in self.char:
			x = self.rect.x
			for c in line:
				if c != '.':
					self.cells.append(cell(x, y, self.size, self.color))
				x += self.size
			y += self.size
	def draw(self, screen):
		for cell in self.cells:
			cell.draw(screen)
	def move(self, dx = 0, dy = 0):
		self.rect = self.rect.move(dx, dy)
		for cell in self.cells:
			cell.move(dx, dy)
		self.pulseColor()
	def colisionLeft(self):
		if self.rect.left < 0:
			return True
		return False
	def colisionRight(self):
		if self.rect.right >= WIDTH:
			return True
		return False
	def changeColor(self, color):
		self.color = color
		for cell in self.cells:
			cell.color = color
	def pulseColor(self):
		dr, dg, db = self.pulse
		r, g, b = self.color
		if r + dr >= 255 or r + dr <= 0:
			dr = -dr
		if g + dg >= 255 or g + dg <= 0:
			dg = -dg
		if b + db >= 255 or b + db <= 0:
			db = -db

		r += dr; g += dg; b += db

		self.color = r, g, b
		self.pulse = [dr, dg, db]

		self.changeColor(self.color)

class stringObj(object):
	def __init__(self, string, x = WIDTH, y = 0):
		self.x = x
		self.y = y
		self.string = string
		self.chars = []
		self.setup()
	def add(self, string):
		if self.length() > 0:
			tail = self.chars[-1]
			x, y = tail.rect.x, tail.rect.y
			x += SIZE *8*1.3
		else:
			x, y = self.x, self.y
		for c in string:
			p = pieces_dic[c]
			char = charObj(x, y, p, SIZE)
			self.chars.append(char)
			x += SIZE*8*1.3
	def setup(self):
		for c in self.string:
			self.add(c)
	def draw(self, screen):
		for c in self.chars:
			c.draw(screen)
	def move(self, dx = 0, dy = 0):
		for c in self.chars:
			c.move(dx, dy)
	def reset(self):
		if self.length() > 0:
			tail = self.chars[-1]
			if tail.colisionLeft():
				tail.rect.x = WIDTH
				self.setup()
	def remove(self):
		if self.length() > 0:
			tail = self.chars[-1]
			self.chars.remove(tail)
	def length(self):
		return len(self.chars)
		
def main():
	pygame.init()
	screen = pygame.display.set_mode(SIZESCREEN)
	pygame.display.set_caption('Chars \/\ 8bits')
	main_clock = pygame.time.Clock()

	text = stringObj(PANEL)

	vel = -5
	dx = vel; inputMode = False
	running =  True
	while running:
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
				elif event.key == K_F10:
					dx = 0
					inputMode = True
					buff = ''
					text = stringObj('', x = 0)
				elif inputMode == True:
					if event.key == K_RETURN:
						dx = vel
						text = stringObj(buff)
						inputMode = False
						break
					elif event.key == K_BACKSPACE:
						text.remove()
						buff = buff[:-1]
					elif event.key in ascii_dic.keys():
						char = ascii_dic[event.key]
						text.add(char)
						buff += char
						if text.length() > 0:
							tail = text.chars[-1]
							while tail.colisionRight():
								text.move(vel)
				elif event.key == K_SPACE:
					if dx != 0:
						dx = 0
					else:
						dx = vel
				
				
		screen.fill(BLACK)

		text.draw(screen)
		text.move(dx)
		text.reset()

		pygame.display.update()
		main_clock.tick(FPS)

	pygame.quit()

if __name__ == '__main__':
	main()