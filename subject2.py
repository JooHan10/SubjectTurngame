from subject_class import *
import time
import random
import sys

while True:
    print("-----------------------------------------")
    player_name = input("사용하실 플레이어 이름을 입력해 주세요.     ")
    print("-----------------------------------------")
    time.sleep(1)
    print("-----------------------------------------")
    print(f"안녕하세요! {player_name}! 모험을 떠나볼까요?")
    adventure = int(input("1.Yes / 2.No     "))
    print("-----------------------------------------")
    if adventure == 1:
        adventure_tf = 1
    elif adventure == 2:
        adventure_tf = 2
        print("..........................................")
        print("모험을 포기합니다.")
        print("..........................................")
        sys.exit()

    pikachu_hp = random.randrange(40, 48)
    pikachu_power = random.randrange(10, 13)
    pikachu_speed = random.randrange(10, 13)

    charmander_hp = random.randrange(40, 51)
    charmander_power = random.randrange(10, 16)
    charmander_speed = random.randrange(8, 11)

    squirtle_hp = random.randrange(40, 54)
    squirtle_power = random.randrange(10, 16)
    squirtle_speed = random.randrange(6, 9)

    bulbasaur_hp = random.randrange(40, 51)
    bulbasaur_power = random.randrange(10, 16)
    bulbasaur_speed = random.randrange(6, 9)

    pikachu = Pikachu("피카츄", pikachu_hp, pikachu_power, 10, pikachu_speed)
    charmander = Charmander("파이리", charmander_hp,
                            charmander_power, 10, charmander_speed)
    squirtle = Squirtle("꼬부기", squirtle_hp, squirtle_power, 10, squirtle_speed)
    bulbasaur = Bulbasaur("이상해씨", bulbasaur_hp,
                          bulbasaur_power, 10, bulbasaur_speed)

    monsters = [
        {'name': '피카츄', 'instance_name': pikachu},
        {'name': '파이리', 'instance_name': charmander},
        {'name': '꼬부기', 'instance_name': squirtle},
        {'name': '이상해씨', 'instance_name': bulbasaur}
    ]
    time.sleep(1)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    time.sleep(1)
    print(". . . . . z    z    z    z")
    time.sleep(2)
    print("z    z    z    z    z    z")
    time.sleep(2)
    print("z    z    z    z    z    z")
    time.sleep(2)
    print("z    z    z    z    z    z\n")
    time.sleep(2)
    print(f"{player_name}: ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !\n")
    time.sleep(0.5)
    print(f"{player_name}: 지각이다!!!\n")
    time.sleep(0.5)
    print(f"{player_name}: 빨리 몬스터를 받으러 가야해!!!\n")
    time.sleep(0.5)
    print(".........................................\n")
    time.sleep(1)
    print(".........................................\n")
    time.sleep(1)
    print(".........................................\n")
    time.sleep(1)
    print(f"{player_name}: 오박사님~~~!!!\n")
    time.sleep(2)
    print(f"오박사님: 오! {player_name}(이)구나!\n")
    time.sleep(2)
    print(f"{player_name}: 죄송해요! 늦잠을 자버렸어요! 몬스터는 남아있나요??\n")
    time.sleep(2)
    print("오박사님: 너무 늦었구나... 방금 마지막 남은 몬스터까지 모험가들이 받아갔단다. \n")
    time.sleep(2)
    print(f"{player_name}: .....ㅠㅠ 이런 날 늦잠이라니... \n")
    time.sleep(2)
    print("오박사님: 흠... 사실 아직 한 마리가 남아있기는 한데.... \n")
    time.sleep(2)
    print(f"{player_name}: !!! 정말요??? \n")
    time.sleep(2)
    print("오박사님: 하지만 이녀석은 길들이기 어려울거야... \n")
    time.sleep(2)
    print(f"{player_name}: 괜찮아요!! 저는 어떤 녀석이든 좋아요! \n")
    time.sleep(2)
    print("오박사님: 그래... 그렇다면... 이녀석을 데려가거라! \n")
    time.sleep(1)
    print("-----------------------------------------")
    print("가장 마음에 드는 몬스터를 선택해 주세요.")
    print("-----------------------------------------")
    select_character = int(input("1.피카츄 2.파이리 3.꼬부기 4.이상해씨     "))
    print("-----------------------------------------\n")
    print(".........................................\n")
    time.sleep(1)
    print(".........................................\n")
    time.sleep(1)
    print(".........................................\n")
    time.sleep(1)
    if select_character == 1:
        p_monster = pikachu
        wild_monster = random.choice([charmander, squirtle, bulbasaur])
        print("-------------------------")
        print("피카츄! 넌 내꺼야!")
        print("-------------------------\n")
    if select_character == 2:
        p_monster = charmander
        wild_monster = random.choice([pikachu, squirtle, bulbasaur])
        print("-------------------------")
        print("파이리! 넌 내꺼야!")
        print("-------------------------\n")
    if select_character == 3:
        p_monster = squirtle
        wild_monster = random.choice([pikachu, charmander, bulbasaur])
        print("-------------------------")
        print("꼬부기! 넌 내꺼야!")
        print("-------------------------\n")
    if select_character == 4:
        p_monster = bulbasaur
        wild_monster = random.choice([pikachu, charmander, squirtle])
        print("-------------------------")
        print("이상해씨! 넌 내꺼야!")
        print("-------------------------\n")

    time.sleep(1)
    print(".........................................\n")
    time.sleep(1)
    print(".........................................\n")
    time.sleep(1)
    print(".........................................\n")
    time.sleep(1)
    print(f".............{player_name}(은)는 {p_monster.name}(을)를 받았다!\n")
    time.sleep(1)
    print(".............................................\n")
    time.sleep(1)
    print(f"{player_name}: 오박사님 고마워요! 저는 이제 모험을 떠날게요! \n")
    time.sleep(2)
    print("오박시님: 그래! 행운을 빈다! \n")
    print("-----------------------------------------\n")
    time.sleep(2)
    print("모험을 시작합니다!\n")
    time.sleep(2)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    time.sleep(2)
    # 여기에 while문을 하나 더 만들어서 싸움에서 도망치면 다른 행동을 할 수 있게 만들 수 있을 것 같음
    # 도망치거나 배틀이 끝나면 몬스터 찾아다니기 부터 다시 시작됨
    while adventure_tf == 1:
        if select_character == 1:
            p_monster = pikachu
            wild_monster = random.choice([charmander, squirtle, bulbasaur])
        if select_character == 2:
            p_monster = charmander
            wild_monster = random.choice([pikachu, squirtle, bulbasaur])
        if select_character == 3:
            p_monster = squirtle
            wild_monster = random.choice([pikachu, charmander, bulbasaur])
        if select_character == 4:
            p_monster = bulbasaur
            wild_monster = random.choice([pikachu, charmander, squirtle])
        print("모험을 계속합니다!\n")
        print("몬스터를 잡을까요? 마을에 갈까요?")
        hunt_or_town = int(input("1.사냥 / 2.마을"))
        if hunt_or_town == 1:
            time.sleep(2)
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            time.sleep(2)
            print("^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            print("  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            print(" ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            print("^   ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            print(
                " ^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^\n")
            time.sleep(2)
            print(" ^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            print("^   ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            print(" ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            print("  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            print("^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^\n")
            time.sleep(2)
            print("^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            print("  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            print(" ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            print("^   ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            print("^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^\n")
            time.sleep(2)
            print("!\n")
            time.sleep(0.5)
            print("!\n")
            time.sleep(0.5)
            print("!\n")
            time.sleep(0.5)
            print("!\n")
            time.sleep(0.5)
            print("!\n")
            time.sleep(0.5)
            print(f"야생의 {wild_monster.name}(이)가 나타났다!\n")
            print("싸울까요??")
            time.sleep(0.5)
            fight_or_run = int(input("1.Yes / 2.No     "))
            print("")
            if fight_or_run == 1:
                time.sleep(1)
                print("----------------------------------------- \n")
                p_monster.status()
                wild_monster.status()
                print("----------------------------------------- \n")
                time.sleep(1)
                if p_monster.speed >= wild_monster.speed:
                    first_attack = 1
                elif p_monster.speed < wild_monster.speed:
                    first_attack = 2

                while True:
                    if first_attack == 1:
                        print("내 포켓몬이 더 빠르다! 어떤 공격을 할까?")
                        time.sleep(0.5)
                        attack_input1 = int(
                            input(f"1.몸통박치기 / 2.{p_monster.skill_name()}     "))
                        print("")
                        if attack_input1 == 1:
                            time.sleep(2)
                            p_monster.attack(wild_monster)
                            if wild_monster.hp != 0:
                                time.sleep(2)
                                wild_monster.attack_or_skill(p_monster)
                                if p_monster.hp != 0 and wild_monster.hp != 0:
                                    time.sleep(2)
                                    p_monster.status()
                                    wild_monster.status()
                                    print(
                                        "-----------------------------------------")
                            elif p_monster.hp == 0 or wild_monster.hp == 0:
                                time.sleep(2)
                                p_monster.status()
                                wild_monster.status()
                                p_monster.cure()
                                wild_monster.cure()
                                time.sleep(2)
                                print("배틀 종료! \n")
                                print(
                                    "----------------------------------------- \n")
                                time.sleep(2)
                                break
                        elif attack_input1 == 2:
                            time.sleep(2)
                            p_monster.skill(wild_monster)
                            if wild_monster.hp != 0:
                                time.sleep(2)
                                wild_monster.attack_or_skill(p_monster)
                                if p_monster.hp != 0 and wild_monster.hp != 0:
                                    time.sleep(2)
                                    p_monster.status()
                                    wild_monster.status()
                                    print(
                                        "-----------------------------------------")
                            elif p_monster.hp == 0 or wild_monster.hp == 0:
                                time.sleep(2)
                                p_monster.status()
                                wild_monster.status()
                                p_monster.cure()
                                wild_monster.cure()
                                time.sleep(2)
                                print("배틀 종료! \n")
                                print(
                                    "-----------------------------------------\n")
                                time.sleep(2)
                                break

                    elif first_attack == 2:
                        print("상대 포켓몬이 더 빠르다! 어떤 공격을 할까?")
                        time.sleep(0.5)
                        attack_input2 = int(
                            input(f"1.몸통박치기 / 2.{p_monster.skill_name()}     "))
                        print("")
                        if attack_input2 == 1:
                            time.sleep(2)
                            wild_monster.attack_or_skill(p_monster)
                            if p_monster.hp != 0:
                                time.sleep(2)
                                p_monster.attack(wild_monster)
                                if wild_monster.hp != 0 and p_monster.hp != 0:
                                    time.sleep(2)
                                    wild_monster.status()
                                    p_monster.status()
                                    print(
                                        "-----------------------------------------")
                            elif p_monster.hp == 0 or wild_monster.hp == 0:
                                time.sleep(2)
                                p_monster.status()
                                wild_monster.status()
                                p_monster.cure()
                                wild_monster.cure()
                                time.sleep(2)
                                print("배틀 종료! \n")
                                print(
                                    "-----------------------------------------\n")
                                time.sleep(2)
                                break
                        elif attack_input2 == 2:
                            time.sleep(2)
                            wild_monster.attack_or_skill(p_monster)
                            if p_monster.hp != 0:
                                time.sleep(2)
                                p_monster.skill(wild_monster)
                                if wild_monster.hp != 0 and p_monster.hp != 0:
                                    time.sleep(2)
                                    wild_monster.status()
                                    p_monster.status()
                                    print(
                                        "-----------------------------------------")
                            elif p_monster.hp == 0 or wild_monster.hp == 0:
                                time.sleep(2)
                                p_monster.status()
                                wild_monster.status()
                                p_monster.cure()
                                wild_monster.cure()
                                time.sleep(2)
                                print("배틀 종료!\n")
                                print(
                                    "-----------------------------------------\n")
                                time.sleep(2)
                                break
            elif fight_or_run == 2:
                time.sleep(0.5)
                print(".........................................")
                print(".........................................")
                print(".................................도망쳤다!\n")
                time.sleep(2)

        elif hunt_or_town == 2:
            print("마을에 왔습니다 게임을 종료합니다.")
            sys.exit()
