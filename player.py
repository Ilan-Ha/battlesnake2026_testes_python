from snake import Snake as SModule
from choices import Choices as CE
import random
class Player:
    snake: SModule
    def __init__(self,snake):
        self.snake = snake

    def choice(self,gamestate:dict):
        # print(gamestate)
        size = gamestate['size']
        possibilities = list()
        head = self.snake.head.copy()
        coordinates_n_t = list()
        for player in gamestate['players']:
            aux = player.snake.coordinates.copy()
            aux.pop()
            for co in aux:
                coordinates_n_t.append(co)
        # print(coordinates_n_t)
        up = head[0] - 1
        if up > 0:
            if [up,head[1]] not in coordinates_n_t:
                possibilities.append(CE.UP)

        down = head[0] + 1
        if down < size - 1:
            if [down,head[1]] not in coordinates_n_t:
                possibilities.append(CE.DOWN)

        left = head[1] - 1
        if left > 0:
            if [head[0],left] not in coordinates_n_t:
                possibilities.append(CE.LEFT)

        right = head[1] + 1
        if right < size - 1:
            if [head[0],right] not in coordinates_n_t:
                possibilities.append(CE.RIGHT)
        if possibilities.__len__()>0:
            ch = random.randrange(0,possibilities.__len__())
            return possibilities[ch]
        else:
            return CE.UP

    def move(self,head:list[int]):
        self.snake.move(head)
