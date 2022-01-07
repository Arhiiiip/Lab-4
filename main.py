import random


class Fish:

    def __init__(self, name, hp, intellect, speed, size, strength, loot,
                 speech):
        self.name = name
        self.hp = hp
        self.intellect = intellect
        self.speed = speed
        self.size = size
        self.strength = strength
        self.loot = loot
        self.speech = speech

    def drop(self):
        print('Drop:' + random.choice(self.loot))

    def scream(self):
        print(self.speech)

    def dead(self):
        Fish.drop
        Fish.scream
        print(f'{self.name} DEAD!!!')


class WhiteShark(Fish):
    def __init__(self):
        super().__init__('WhiteShark', 400, 4, 5, 10, 60,
                         ['TOOTH', 'FIN'], 'BOOM!!!')


class SwordFish(Fish):
    def __init__(self):
        super().__init__('SwordFish', 300, 5, 6, 15, 50,
                         ['SWORD', 'FISH OIL', 'FIN'], 'FIP FIP FIP')


class Barracuda(Fish):
    def __init__(self):
        super().__init__('Barracuda', 500, 4, 6, 8, 50,
                         ['FANG', 'FISH OIL', 'FIN'], 'GRRR')


class MackerelSapedHydrolysis(Fish):
    def __init__(self):
        super().__init__('MackerelSapedHydrolysis', 250, 8, 5, 10, 60,
                         ['SWORD', 'FISH OIL', 'FIN'], 'BOOP!!!')


class Piranhas(Fish):
    def __init__(self):
        super().__init__('Piranhas', 300, 9, 9, 3, 60, ['JAW', 'FIN'],
                         'HR HR HR!!!')


class Perch(Fish):
    def __init__(self):
        super().__init__('Perch', 250, 7, 8, 9, 60, ['TAIL', 'JAW'],
                         'KLAK!!!')


class Stingray(Fish):
    def __init__(self):
        super().__init__('Stingray', 600, 5, 5, 8, 50,
                         ['SPIKE', 'FISH MEAT'], 'Mua!!!')


class Catfish(Fish):
    def __init__(self):
        super().__init__('Catfich', 500, 4, 6, 5, 60,
                         ['FISH OIL', 'TAIL'], 'BOOL!!!')


first_fish = WhiteShark()
second_fish = SwordFish()
third_fish = Barracuda()
fourth_fish = MackerelSapedHydrolysis()
fifth_fish = Piranhas()
sixth_fish = Perch()
seventh_fish = Stingray()
eighth_fish = Catfish()

fishes = [first_fish, second_fish, third_fish, fourth_fish, fifth_fish,
          sixth_fish, seventh_fish, eighth_fish]
random.shuffle(fishes)


def fight():
    while len(fishes) != 1:
        fish_lose = []
        for i in range(0, len(fishes), 2):
            health_point_1 = fishes[i].hp
            health_point_2 = fishes[i + 1].hp
            chance_crit_dam_1 = fishes[i].intellect
            chance_crit_dam_2 = fishes[i + 1].intellect
            while fishes[i].hp > 0 and fishes[i + 1].hp > 0:
                ran_num_1 = random.uniform(0, 10)
                ran_num_2 = random.uniform(0, 10)
                if ran_num_1 <= chance_crit_dam_1:
                    health_point_2 = health_point_2 - fishes[
                        i].strength * random.randint(2, 5)
                else:
                    health_point_2 = health_point_2 - fishes[i].strength
                if health_point_2 <= 0:
                    fish_lose.append(fishes[i + 1])
                    fishes[i + 1].dead()
                    break
                if ran_num_2 <= chance_crit_dam_2:
                    health_point_1 = health_point_1 - fishes[
                        i + 1].strength * random.randint(2, 5)
                else:
                    health_point_1 = health_point_1 - fishes[
                        i + 1].strength
                if health_point_1 <= 0:
                    fish_lose.append(fishes[i])
                    fishes[i].dead()
                    break
        for i in fish_lose:
            fishes.remove(i)
    print('WINNER:' + fishes[0].name)


fight()
