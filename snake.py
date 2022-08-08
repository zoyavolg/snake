import pygame as pg


W_W = 800
W_H = 600
C_S = 50

snake = []
sc = pg.display.set_mode((W_W, W_H))

food = (5, 5)


class Snake:
	def __init__(self, x, y, color, direction):
		self.body = [(x, y)]
		self.color = color
		self.dir = direction

	def changeDir(self, key):
		if key[pg.K_s]:
			self.dir = (0, 1)
		elif key[pg.K_w]:
			self.dir = (0, -1)
		elif key[pg.K_d]:
			self.dir = (1, 0)
		elif key[pg.K_a]:
			self.dir = (-1, 0)

	def move(self):
		self.body.insert(0, (self.body[0][0] + self.dir[0], self.body[0][1] + self.dir[1]))

	def isAte(self):
		return self.body[0][0] == food[0] and self.body[0][1] == food[1]

	def draw(self):
		for bd in self.body:
			pg.draw.rect(sc, self.color, (bd[0]*C_S, bd[1]*C_S, C_S, C_S))


def init():
	sc = pg.display.set_mode((W_W, W_H))
	snake.append(Snake(0, 0, pg.Color("green"), (1, 0)))
#	snake.append(Snake(0, 2, pg.Color("red"), (1, 0)))


def change_all():
	key = pg.key.get_pressed()
	for sn in snake:
		sn.changeDir(key)

	for sn in snake:
		sn.move()

	for sn in snake:
		if not sn.isAte():
			sn.body.pop()


def draw_all():
	sc.fill("black")
	for sn in snake:
		sn.draw()
	pg.draw.rect(sc, pg.Color("blue"), (food[0]*C_S, food[1]*C_S, C_S, C_S))


def key_down(key):
	for sn in snake:
		sn.changeDir(key)


def main():
	pg.init()
	init()

	clock = pg.time.Clock()
	while True:
		change_all()
		draw_all()
		pg.display.update()
		clock.tick(2)

		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				exit()
#			elif event.type == pg.KEYDOWN:
#				key = pg.key.get_pressed()
#				key_down(key)


main()
