import random


DRAGON_BASE_HIT_POINTS = random.randint(50, 100)
STATUS_ALIVE = 'alive'
STATUS_DEAD = 'dead'


class Dragon:
    def __init__(self, name, position_x=0, position_y=0, texture='dragon.png'):
        self.name = name
        self.hit_points = DRAGON_BASE_HIT_POINTS
        self.position_x = position_x
        self.position_y = position_y
        self.texture = texture
        self.status = STATUS_ALIVE

    def move(self, left=0, down=0, up=0, right=0):
        self.position_x += right - left
        self.position_y += down - up

    def set_position(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y

    def get_position(self):
        return self.position_x, self.position_y

    def drop_gold(self):
        gold = random.randint(1, 100)
        print(f'Dropped {gold} gold at position {self.get_position()}')

    def make_dead(self):
        print('Dragon is dead')
        self.status = STATUS_DEAD
        self.texture = 'dragon-dead.png'
        self.drop_gold()

    def take_damage(self, damage=0):
        if self.status == STATUS_DEAD:
            return None

        self.hit_points -= damage
        print(f'Dragon damage taken: {damage}, HP left: {self.hit_points}')

        if self.hit_points <= 0:
            self.make_dead()

    def make_damage(self):
        if self.status != STATUS_DEAD:
            return random.randint(5, 20)


if __name__ == '__main__':
    wawelski = Dragon(name='Wawelski', position_x=0, position_y=0)

    wawelski.move(left=10, down=20)
    wawelski.move(right=15, up=5)

    wawelski.take_damage(10)
    wawelski.take_damage(50)
    wawelski.take_damage(35)
    wawelski.take_damage(20)
