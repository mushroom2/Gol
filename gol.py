"""
    Место действия этой игры — «вселенная» — это размеченная на клетки поверхность или плоскость — безграничная,
    ограниченная, или замкнутая (в пределе — бесконечная плоскость).
    Каждая клетка на этой поверхности может находиться в двух состояниях: быть «живой» или быть «мёртвой» (пустой).
    Клетка имеет восемь соседей (окружающих клеток).
    Распределение живых клеток в начале игры называется первым поколением.
    Каждое следующее поколение рассчитывается на основе предыдущего по таким правилам:
        в пустой (мёртвой) клетке, рядом с которой ровно три живые клетки, зарождается жизнь;
        если у живой клетки есть две или три живые соседки, то эта клетка продолжает жить; в противном случае
        (если соседей меньше двух или больше трёх) клетка умирает («от одиночества» или «от перенаселённости»)
    Игра прекращается, если
        на поле не останется ни одной «живой» клетки
        конфигурация на очередном шаге в точности (без сдвигов и поворотов)
         повторит себя же на одном из более ранних шагов (складывается периодическая конфигурация)
        при очередном шаге ни одна из клеток не меняет своего состояния (складывается стабильная конфигурация;
        предыдущее правило, вырожденное до одного шага назад)

 Эти простые правила приводят к огромному разнообразию форм, которые могут возникнуть в игре.

 Игрок не принимает прямого участия в игре, а лишь расставляет или генерирует начальную конфигурацию «живых» клеток,
 которые затем взаимодействуют согласно правилам уже без его участия (он является наблюдателем).
"""

from random import *


class Map:
    myMap = []

    def __init__(self, size, startcells):
        self.size = size
        self.startcells = startcells

    def makemap(self):
        print('KapTa CgeJIaHa')
        Map.myMap = [[0 for i in range(self.size)] for i in range(self.size)]

    def getmap(self):
        for line in Map.myMap:
            print(line)

    def make_first_generation(self):
        while sum([sum(i) for i in a.myMap]) < self.startcells:
            Map.myMap[randint(0, self.size-1)][randint(0, self.size-1)] = 1
        return Map.myMap


class Cell:
    neighbors = []
    status = None
    nes = []

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_status(self):
        self.status = Map.myMap[self.y][self.x]
        return self.status


    def make_alive(self):
        Map.myMap[self.y][self.x] = 1
        self.status = 1

    def kill(self):
        Map.myMap[self.y][self.x] = 0
        self.status = 0

    def get_neighbors(self):
        self.neighbors = [[self.y + i, self.x + j]
                          for i in range(-1, 2)
                          for j in range(-1, 2)
                          if not i == j == 0
                          ]

    def check_neighbors(self):
        self.get_neighbors()

        for el in self.neighbors:
            for point in range(2):
                if el[point] == len(Map.myMap):
                    el[point] = 0

    def get_nes(self):

        self.check_neighbors()
        self.nes = []
        for i in self.neighbors:
            self.nes.append(Cell(i[1], i[0]).get_status())


class Round:
    alivelist = []
    skancells = []

    def next_round(self):
        Round.alivelist = []
        for row, i in enumerate(Map.myMap):  # тут поправить
            for col, j in enumerate(i):
                if j == 1:
                    Round.alivelist.append(Cell(col, row))

    def minimap(self):
        for k in Round.alivelist:
            k.check_neighbors()

    def scan(self):
        for k in Round.alivelist:
            for nei in k.neighbors:
                Round.skancells.append(Cell(nei[1], nei[0]))

    def analyze(self):
        Round.skancells.extend(Round.alivelist)
        print('_____')
        for i in Round.skancells:
            i.check_neighbors()

    def desteny(self):
        print('___')
        for i in Round.skancells:
            i.get_nes()

    def fin(self):
        for i in Round.skancells:
            if sum(i.nes) < 2 or sum(i.nes) > 3:
                i.kill()
            elif sum(i.nes) == 3:
                i.make_alive()

    def new_map(self):
        for line in Map.myMap:
            print(line)

a = Map(10, 20)
a.makemap()
a.make_first_generation()
a.getmap()

while True:      # тут будут условия
    a = input('>>> ')
    d = Round()
    d.next_round() #создание списка живых клеток
    d.minimap()     #
    d.scan()
    d.analyze()
    d.desteny()
    d.fin()
    d.new_map()