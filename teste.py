import random

import copy



class Game:
    def __init__(self):
        self.vidas = 3
        self.score = 0
        self.level = 1
        self.state = StateInitial(self)

    def loop(self):
        self.state.loop()


class StateInitial(GameState):
    def __init__(self, context):
        GameState.__init__(self)
        self.context = context
        self.context.lives = 3
        self.context.score = 0
        self.context.level = 1

    def loop(self):
        message = " LA cucaracha"


class Terrain:
    INIMIGO = (Position(11, 4), Position(10, 6), Position(11, 6), Position(12, 6))

    def is_blocked(self, position, direction):
        try:
            if position.x == 11 and position.y == 5 and direction == Direction.UPWARD: return False
            char = self.terrain[position.y][position.x]
            return char == "|" or char == "=" or char == "-"
        except:
            return True

    def eat(self, context, personagem):
        position = self.terrain[pacman.position.y][pacman.position.x]
        if position == Terrain.BULLET:
            self.terrain[pacman.position.y][pacman.position.x] = ' '
            context.context.score += 1
        elif position == Terrain.GREATER_BULLET:
            self.terrain[pacman.position.y][pacman.position.x] = ' '
            context.context.score += 5
            return True
        return False