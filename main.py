import random


class WhiteShark:

    def __init__(self):
        self.name = 'WhiteShark'
        self.hp = 400
        self.intellect = 5
        self.speed = 5
        self.size = 10
        self.strength = 11

    def drop(self):
        loot = ['TOOTH', 'FIN']
        print('Drop:' + random.choice(loot))

    def scream(self):
        speech = 'BOOM!!!'
        print(speech)

    def dead(self):
        WhiteShark().drop()
        WhiteShark().scream()
        print('WhiteShark DEAD!!!')


class SwordFish:

    def __init__(self):
        self.name = 'SwordFish'
        self.hp = 300
        self.intellect = 5
        self.speed = 6
        self.size = 15
        self.strength = 11

    def drop(self):
        loot = ['SWORD', 'FISH OIL', 'FIN']
        print('Drop:' + random.choice(loot))

    def scream(self):
        speech = 'FIP FIP FIP'
        print(speech)

    def dead(self):
        SwordFish().drop()
        SwordFish().scream()
        print('SwordFish DEAD!!!')


class Barracuda:

    def __init__(self):
        self.name = 'Barracuda'
        self.hp = 550
        self.intellect = 4
        self.speed = 6
        self.size = 8
        self.strength = 10

    def drop(self):
        loot = ['FANG', 'FISH OIL', 'FIN']
        print('Drop:' + random.choice(loot))

    def scream(self):
        speech = 'GRRR'
        print(speech)

    def dead(self):
        Barracuda().drop()
        Barracuda().scream()
        print('Barracuda DEAD!!!')


class MackerelSapedHydrolysis:

    def __init__(self):
        self.name = 'MackerelSapedHydrolysis'
        self.hp = 250
        self.intellect = 8
        self.speed = 5
        self.size = 10
        self.strength = 9

    def drop(self):
        loot = ['SWORD', 'FISH OIL', 'FIN']
        print('Drop:' + random.choice(loot))

    def scream(self):
        speech = 'BOOP!!!'
        print(speech)

    def dead(self):
        MackerelSapedHydrolysis().drop()
        MackerelSapedHydrolysis().scream()
        print('MackerelSapedHydrolysis DEAD!!!')


class Piranhas:

    def __init__(self):
        self.name = 'Piranhas'
        self.hp = 250
        self.intellect = 10
        self.speed = 9
        self.size = 3
        self.strength = 8

    def drop(self):
        loot = ['JAW', 'FIN']
        print('Drop:' + random.choice(loot))

    def scream(self):
        speech = 'HR HR HR!!!'
        print(speech)

    def dead(self):
        Piranhas().drop()
        Piranhas().scream()
        print('Piranhas DEAD!!!')


class Perch:

    def __init__(self):
        self.name = 'Perch'
        self.hp = 200
        self.intellect = 7
        self.speed = 8
        self.size = 9
        self.strength = 9

    def drop(self):
        loot = ['TAIL', 'JAW']
        print('Drop:' + random.choice(loot))

    def scream(self):
        speech = 'KLAK!!!'
        print(speech)

    def dead(self):
        Perch().drop()
        Perch().scream()
        print('Perch DEAD!!!')


class Stingray:

    def __init__(self):
        self.name = 'Stingray'
        self.hp = 600
        self.intellect = 6
        self.speed = 5
        self.size = 8
        self.strength = 7

    def drop(self):
        loot = ['SPIKE', 'FISH MEAT']
        print('Drop:' + random.choice(loot))

    def scream(self):
        speech = 'Mua!!!'
        print(speech)

    def dead(self):
        Stingray().drop()
        Stingray().scream()
        print('Stingray DEAD!!!')


class Catfish:

    def __init__(self):
        self.name = 'Catfish'
        self.hp = 500
        self.intellect = 4
        self.speed = 6
        self.size = 5
        self.strength = 7

    def drop(self):
        loot = ['FISH OIL', 'TAIL']
        print('Drop:' + random.choice(loot))

    def scream(self):
        speech = 'BOOL!!!'
        print(speech)

    def dead(self):
        Catfish().drop()
        Catfish().scream()
        print('Catfish DEAD!!!')


fish = [WhiteShark(), SwordFish(), Barracuda(),
        MackerelSapedHydrolysis(), Piranhas(), Perch(), Stingray(),
        Catfish()]
random.shuffle(fish)


def fight():
    while len(fish) != 1:
        fish_lose = []
        for i in range(0, len(fish), 2):
            health_point_1 = fish[i].hp
            health_point_2 = fish[i + 1].hp
            while fish[i].hp > 0 and fish[i + 1].hp > 0:
                health_point_1 = health_point_1 - fish[i + 1].strength * \
                                 fish[i + 1].intellect
                if health_point_1 <= 0:
                    fish_lose.append(fish[i])
                    fish[i].dead()
                    break
                health_point_2 = health_point_2 - fish[i].strength * \
                                 fish[i].intellect
                if health_point_2 <= 0:
                    fish_lose.append(fish[i + 1])
                    fish[i + 1].dead()
                    break
        for i in fish_lose:
            fish.remove(i)
    print('WINNER:' + fish[0].name)


fight()
