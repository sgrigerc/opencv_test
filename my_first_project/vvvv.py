class Buffer:
    def __init__(self):
        self.l = []     #список куда будут добавляться числа
        self.miz = 4
        #self.x = 0
        self.sum = 0

        # конструктор без аргументов
    def add(self, *a):
        for a in self.l:
            if a <= 4:
                self.l.append()
        # self.x = 0
        # #self.*a = *a
        # for i in self.l :
        #     self.x += 1
        # if self.x >= 5:
        #     print(("vse ok"))
        # # print(self.x)

        #self.list.clear()      #очистка списка

        # добавить следующую часть последовательности

    def get_current_part(self):
        self.aplp = 5
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
buf = Buffer()
buf.add(1, 2, 3, 4, 5)
buf.get_current_part()