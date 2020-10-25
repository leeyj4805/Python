# 멤버변수 -self.name.. 클래스 내에 정의된 변수

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛, 비행기 , 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)

wraith2 = Unit("빼앗은 레이스", 80,5)
wraith2.clocking= True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# 클로킹이라는 변수에는 Unit 클래스가 없으며 외부에서 클로킹이라는 
# 변수를 추가로 할당시켜서 True를 넣은 것임
# 파이썬에서는 객체에 추가로 변수를 외부에서 만들어 쓸 수 있음
# wraith1에 클로킹을 시도하면 오류가 발생
# 결론은 클래스 외부에서 내가 원하는 변수를 확장할 수 있으며 
# 확장된 변수는 확장된 객체에서 사용되며 다른 객체에 적용이 안됨
