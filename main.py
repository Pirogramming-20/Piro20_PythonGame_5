import random
from collections import deque

def apart_game():
    print("\n아파트 게임을 시작합니다\n")
    hands_3 = deque(random.sample(game_people * 2, g_num * 2))

    tagger_3 = random.choice(game_people)
    print(f"\n술래는 {tagger_3}입니다!")

    if tagger_3 == player_name:
        floor_num_3 = int(input("\n층수를 입력하세요! : "))
    else:
        floor_num_3 = random.randint(1, 5 * g_num)
    
    print("\n아파트 몇 층?")
    print(f"\n{tagger_3} : 아파트 {floor_num_3}층!\n")


    for i in range(1, floor_num_3 + 1):
        hand_3 = hands_3.popleft()
        hands_3.append(hand_3)
        print(f"\n{hand_3} : {i}층!")

        if i == floor_num_3:
            print(f"\n\n누가 술을 마셔 {hand_3}가(이) 술을 마셔 원샷~")
            for j in range(1, g_num):
                if game_people[j] == hand_3:
                    people_alc[j] -= 1
                    drunk_alc[j] += 1
                    return