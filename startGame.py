'''
MIT License
Copyright (c) [2021]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import pygame, os, sys
from pygame.locals import *

# Pass the speed of game we want the game to run,
# the higher GAME_SPEED_VALUE the faster game speed
class GameEntity:
	def __init__(self, game_speed_value=60):
		self.GAME_SPEED_VALUE = game_speed_value
		# The display resolution: 720p
		self.SCREEN_WIDTH = 1280
		self.SCREEN_HEIGHT = 720
		self.GAME_TITLE = 'Banana game (click left button of the mouse to start game)'
		self.BACKGROUND_COLOR = (0, 0, 0)
		self.WHITE_COLOR = (255, 255, 255)
		self.TEXT_FONT_SIZE = 32
		self.TEXT_Y_OFFSET = 32
		# stores list of coordinates(x,y) of each banana
		self.bananas = []
		self.PLAY_GAME = True
		self.MONKEY_WIDTH = 124
		self.BANANA_WIDTH = 78
		self.BANANA_HEIGHT = 16
		self.BANANA_ROW_NUMBER = 6
		self.BANANA_COL_NUMBER = 10
		self.BANANA_ROW_OFFSET = 35
		self.BANANAS_REMAIN = self.BANANA_ROW_NUMBER * self.BANANA_COL_NUMBER
		self.BANANA_SPACE_X = 250
		self.BANANA_SPACE_Y = 100
		self.MONKEY_Y_POSITION = 512
		self.APPLE_Y_POSITION = 200
		self.APPLE_SIZE = 32
		self.APPLE_INIT_X_POSITION = 25
		self.APPLE_MOVE_SPEED = 3
		self.APPLESERVED = False

	def configGameSettings(self):
		# Set up pygame
		pygame.init()
		self.gameSpeedSetting = pygame.time.Clock()

		# Set up the window
		self.windowSurfaceObj = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
		pygame.display.set_caption(self.GAME_TITLE)

		# Set up the background color to Black (R, G, B)
		self.backgroundColor = pygame.Color(self.BACKGROUND_COLOR)

		# Set up the background music
		pygame.mixer.music.load('background.mid')
		pygame.mixer.music.play(-1, 0.0)

	def initMonkey(self):
		self.monkey = pygame.image.load('monkey.png')
		self.monkey = self.monkey.convert_alpha()
		self.playerY = self.MONKEY_Y_POSITION
		self.monkeyRect = self.monkey.get_rect()
		self.mousex, self.mousey = (24, self.playerY)

	def initApple(self):
		self.apple = pygame.image.load('apple.png')
		self.apple = self.apple.convert_alpha()
		self.appleRect = self.apple.get_rect()
		self.appleStartY = self.APPLE_Y_POSITION
		self.appleSpeed = self.APPLE_MOVE_SPEED
		self.bx, self.by = (self.APPLE_INIT_X_POSITION, self.appleStartY)
		self.sx, self.sy = (self.appleSpeed, self.appleSpeed)
		self.appleRect.topleft = (self.bx, self.by)

	def initBanana(self):
		self.banana = pygame.image.load('bananas.png')
		# Draw rows x cols bananas for 2D Graph
		for y in range(self.BANANA_ROW_NUMBER):
			self.bananaY = (y * self.BANANA_ROW_OFFSET) + self.BANANA_SPACE_Y
			for x in range(self.BANANA_COL_NUMBER):
				self.bananaX = (x * self.BANANA_WIDTH) + self.BANANA_SPACE_X
				self.bananas.append((self.bananaX, self.bananaY))

	def initUI(self):
		self.initMonkey()
		self.initApple()
		self.initBanana()

	def updateScore(self):
		self.font = pygame.font.Font(None, self.TEXT_FONT_SIZE)
		self.text = self.font.render("Bananas remain: %d" % self.BANANAS_REMAIN, 0, self.WHITE_COLOR)
		self.text_position = self.text.get_rect(centerx=self.windowSurfaceObj.get_width()/2, top=self.TEXT_Y_OFFSET)
		self.windowSurfaceObj.blit(self.text, self.text_position)

	def startGameLoop(self):
		# Run the game loop
		while self.PLAY_GAME:
			# Fill the background color onto the surface object
			self.windowSurfaceObj.fill(self.backgroundColor)

			# banana draw
			for b in self.bananas:
				self.windowSurfaceObj.blit(self.banana, b)

			# monkey and apple draw, blit(source, dest, ...)
			self.windowSurfaceObj.blit(self.monkey, self.monkeyRect)
			self.windowSurfaceObj.blit(self.apple, self.appleRect)

			# get events from the queue
			# for example mouse move event, keyboard press event
			for event in pygame.event.get():
				# get input event
				if event.type == MOUSEBUTTONUP:
					if not self.APPLESERVED:
						self.APPLESERVED = True

				elif event.type == MOUSEMOTION:
					mousex, mousey = event.pos
					if mousex < self.SCREEN_WIDTH - self.MONKEY_WIDTH:
						self.monkeyRect.topleft = (mousex, self.playerY)
					else:
						self.monkeyRect.topleft = (self.SCREEN_WIDTH - self.MONKEY_WIDTH, self.playerY)

				# Exit by pressing 'q' key
				elif event.type == KEYDOWN:
					keys = pygame.key.get_pressed()
					if (keys[K_q]):
						print("User pressed 'q' to exit game.")
						self.PLAY_GAME = False
						self.stopGame()

			# main game logic
			if self.APPLESERVED:
				self.appleRect.topleft = (self.bx, self.by)
				# apple moving with step n pixels toward x and y (default apple speed)
				self.bx += self.sx
				self.by += self.sy

			# apple hit y lower boundary
			if self.by >= self.SCREEN_HEIGHT - self.APPLE_SIZE:
				self.APPLESERVED = False
				# serve next apple to the initial apple position
				self.bx, self.by = (self.APPLE_INIT_X_POSITION, self.appleStartY)
				self.appleRect.topleft = (self.bx, self.by)

			# apple hit y upper boundary
			if self.by <= 0:
				self.by = 0
				self.sy *= -1

			# apple hit x left boundary
			if self.bx <= 0:
				self.bx = 0
				self.sx *= -1

			# apple hit x right boundary
			if self.bx >= self.SCREEN_WIDTH - self.APPLE_SIZE:
				self.bx = self.SCREEN_WIDTH - self.APPLE_SIZE
				self.sx *= -1

			# Bal and Brick collision detection
			self.bananaForRemoval = None
			for b in self.bananas:
				briX, briY = b
				# Brick rectangle:
				if (self.bx >= briX and self.bx <= briX + self.BANANA_WIDTH):
					if (self.by >= briY and self.by <= briY + self.BANANA_HEIGHT):
						self.bananaForRemoval = b
						# Ball rebound handling when hit the banana (31 x 16)
						# for banana width
						if (self.bx <= briX + 2):
							self.sx *= -1
						elif (self.bx >= briX + 29):
							self.sx *= -1
						# for banana height
						if (self.by <= briY + 2):
							self.sy *= -1
						elif (self.by >= briY + 14):
							self.sy *= -1
						break

			if self.bananaForRemoval != None:
				# remove the banana hit by the apple
				self.bananas.remove(self.bananaForRemoval)
				self.BANANAS_REMAIN -= 1

			# Draw text
			self.updateScore()

			# Ball rebound handling when hit the player's monkey
			if (self.bx >= mousex and self.bx <= mousex + self.MONKEY_WIDTH):
				if (self.by >= self.playerY - self.APPLE_SIZE and self.by <= self.playerY):
					self.sy *= -1

			# Update the score text on the screen.
			pygame.display.update()

			# Passed Frames Per Second we want the game to run, the higher the faster
			self.gameSpeedSetting.tick(self.GAME_SPEED_VALUE)

	def runGame(self):
		self.configGameSettings()
		self.initUI()
		self.startGameLoop()

	def stopGame(self):
		pygame.quit()
		sys.exit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game1 = GameEntity(100).runGame()



