import random


class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """

    def __init__(self, name, hp, power, skill_point, speed):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.max_sp = skill_point
        self.sp = skill_point
        self.speed = speed

    def attack(self, other, sp=1):
        self.sp = self.sp - sp
        if other.hp != 0 and self.sp > 0:
            damage = random.randint(self.power - 2, self.power + 2)
            other.hp = max(other.hp - damage, 0)
            print(
                f"{self.name} / HP:{self.hp}/{self.max_hp} / SP:{self.sp}/{self.max_sp} / SPEED:{self.speed}")
            print(f"{self.name}의 몸통박치기! {other.name}에게 {damage}의 데미지를 입혔습니다. \n")
            print("-----------------------------------------")
            if other.hp == 0:
                print(f"{other.name}(이)가 쓰러졌습니다!")
        elif self.sp < 0:
            print(f"{self.name}(은)는 스킬 포인트를 전부 사용하였습니다.")

    def skill(self, other, skill_power=30, sp=2):
        self.sp = self.sp - sp
        if other.hp != 0 and self.sp > 0:
            damage = random.randint(
                skill_power - 2, skill_power + 2)
            other.hp = max(other.hp - damage, 0)
            print(
                f"{self.name} / HP:{self.hp}/{self.max_hp} / SP:{self.sp}/{self.max_sp} / SPEED:{self.speed}")
            print(f"{self.name}의 스킬! {other.name}에게 {damage}의 데미지를 입혔습니다.\n")
            print("----------------------------------------- \n")
            if other.hp == 0:
                print(f"{other.name}(이)가 쓰러졌습니다!")
        elif self.sp < 0:
            print(f"{self.name}(은)는 스킬 포인트를 전부 사용하였습니다.")

    def status(self):
        print(
            f"{self.name} / HP:{self.hp}/{self.max_hp} / SP:{self.sp}/{self.max_sp} / SPEED:{self.speed} \n")

    def cure(self):
        self.hp += (self.max_hp - self.hp)
        self.sp += (self.max_sp - self.sp)


class Pikachu(Character):
    def __init__(self, name, hp, power, skill_point, speed):
        Character.__init__(self, name, hp, power, skill_point, speed)

    def skill(self, other, skill_power=30, sp=2):
        self.sp = self.sp - sp
        if other.hp != 0 and self.sp > 0:
            damage = random.randint(
                skill_power - 2, skill_power + 2)
            other.hp = max(other.hp - damage, 0)
            print(
                f"{self.name} / HP:{self.hp}/{self.max_hp} / SP:{self.sp}/{self.max_sp} / SPEED:{self.speed}")
            print(f"{self.name}의 100만 볼트! {other.name}에게 {damage}의 데미지를 입혔습니다. \n")
            print("----------------------------------------- \n")
            if other.hp == 0:
                print(f"{other.name}(이)가 쓰러졌습니다!")
        elif self.sp < 0:
            print(f"{self.name}(은)는 스킬 포인트를 전부 사용하였습니다.")

    def attack_or_skill(self, other):
        select = random.choice([self.attack, self.skill])
        select(other)

    def skill_name(self):
        return "100만볼트"


class Charmander(Character):
    def __init__(self, name, hp, power, skill_point, speed):
        Character.__init__(self, name, hp, power, skill_point, speed)

    def skill(self, other, ember_power=30, sp=2):
        self.sp = self.sp - sp
        if other.hp != 0 and self.sp > 0:
            damage = random.randint(ember_power - 2, ember_power + 2)
            other.hp = max(other.hp - damage, 0)
            print(
                f"{self.name} / HP:{self.hp}/{self.max_hp} / SP:{self.sp}/{self.max_sp} / {self.speed}")
            print(f"{self.name}의 불꽃세례! {other.name}에게 {damage}의 데미지를 입혔습니다. \n")
            # print(f"{self.name}의 남은 SP: {self.sp}/{self.max_sp}")
            print("----------------------------------------- \n")
            if other.hp == 0:
                print(f"{other.name}(이)가 쓰러졌습니다!")
        elif self.sp < 0:
            print(f"{self.name}(은)는 스킬 포인트를 전부 사용하였습니다.")

    def attack_or_skill(self, other):
        select = random.choice([self.attack, self.skill])
        select(other)

    def skill_name(self):
        return "불꽃세례"


class Squirtle(Character):
    def __init__(self, name, hp, power, skill_point, speed):
        Character.__init__(self, name, hp, power, skill_point, speed)

    def skill(self, other, water_gun_power=30, sp=2):
        self.sp = self.sp - sp
        if other.hp != 0 and self.sp > 0:
            damage = random.randint(water_gun_power - 2, water_gun_power + 2)
            other.hp = max(other.hp - damage, 0)
            print(
                f"{self.name} / HP:{self.hp}/{self.max_hp} / SP:{self.sp}/{self.max_sp} / {self.speed}")
            print(f"{self.name}의 물대포! {other.name}에게 {damage}의 데미지를 입혔습니다. \n")
            # print(f"{self.name}의 남은 SP: {self.sp}/{self.max_sp}")
            print("----------------------------------------- \n")
            if other.hp == 0:
                print(f"{other.name}(이)가 쓰러졌습니다!")
        elif self.sp < 0:
            print(f"{self.name}(은)는 스킬 포인트를 전부 사용하였습니다.")

            # random.choice([self.attack(other), self.skill(other)])

    def attack_or_skill(self, other):
        select = random.choice([self.attack, self.skill])
        select(other)

    def skill_name(self):
        return "물대포"


class Bulbasaur(Character):
    def __init__(self, name, hp, power, skill_point, speed):
        Character.__init__(self, name, hp, power, skill_point, speed)

    def skill(self, other, vine_whip_power=30, sp=2):
        self.sp = self.sp - sp
        if other.hp != 0 and self.sp > 0:
            damage = random.randint(vine_whip_power - 2, vine_whip_power + 2)
            other.hp = max(other.hp - damage, 0)
            print(
                f"{self.name} / HP:{self.hp}/{self.max_hp} / SP:{self.sp}/{self.max_sp} / {self.speed}")
            print(f"{self.name}의 덩굴채찍! {other.name}에게 {damage}의 데미지를 입혔습니다. \n")
            # print(f"{self.name}의 남은 SP: {self.sp}/{self.max_sp}")
            print("----------------------------------------- \n")
            if other.hp == 0:
                print(f"{other.name}(이)가 쓰러졌습니다!")
        elif self.sp < 0:
            print(f"{self.name}(은)는 스킬 포인트를 전부 사용하였습니다.")

    def attack_or_skill(self, other):
        select = random.choice([self.attack, self.skill])
        select(other)

    def skill_name(self):
        return "덩굴채찍"
