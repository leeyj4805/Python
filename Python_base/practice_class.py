class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropsship = FlyableUnit()
# Unit 생성자만 호출됨, 처음 부모클래스만 상속됨.