# 메소드 오버라이딩
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed): # 스피드 정보 추가
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location): # 이동할 수 있다는 가정 하에 move 추가
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

# 공격 유닛에도 speed 

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) # Unit에도 speed를 추가했기 때문에 이 클래스를 사용하는 곳에도 speed 정보를 추가해야 함. 
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        # 날아다니는 스피드 정보가 있기 때문에 지상 스피드가 필요없음.
        Flyable.__init__(self, flying_speed)
    
    # move 함수 새롭게 정의
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)    

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음.
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")