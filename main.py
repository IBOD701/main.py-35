class Chiroq:
    def __init__(self):
        self.holat = False
        self.avtomat = True

    def yoqish(self):
        self.holat = True

    def ochirish(self):
        self.holat = False

class SmartChiroq(Chiroq):
    def __init__(self):
        super().__init__()
        self.rejim = True

    def rejimni_ozgartirish(self):
        self.rejim = not self.rejim

qurilma = SmartChiroq()
qurilma.yoqish()
qurilma.rejimni_ozgartirish()