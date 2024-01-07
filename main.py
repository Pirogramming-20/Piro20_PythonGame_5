def apart_game():
    import random
    from collections import deque

    print("\n。　♡ 。　　♡。　　♡\n")
    print("♡。　＼　　｜　　／。　♡\n")
    print("　\t아파트 게임\n")
    print("♡。　／　　｜　　＼。　♡\n")
    print("。　♡。 　　。　　♡。\n")
    print("\n--------!!아파트 게임을 시작합니다!!--------\n")
    hands_3 = deque(random.sample(game_people + game_people, g_num * 2))

    if game_people[0] == player_name:
        tagger_3 = player_name
        print(f"\n술래는 {tagger_3}입니다!")
        floor_num_3 = int(input("\n층수를 입력하세요! : "))
    else:
        tagger_3 = game_people[0]
        print(f"\n술래는 {tagger_3}입니다!")
        floor_num_3 = random.randint(1, 5 * g_num)
    
    print("\n아파트 몇 층?")
    print(f"\n{tagger_3} : 아파트 {floor_num_3}층!\n")


    for i in range(1, floor_num_3 + 1):
        hand_3 = hands_3.popleft()
        hands_3.append(hand_3)
        print(f"\n{hand_3} : {i}층!")

        if i == floor_num_3:
            print(f"\n\n누가 술을 마셔 {hand_3}가(이) 술을 마셔 원샷~~~\n")
            for j in range(0, g_num):
                if game_people[j] == hand_3:
                    people_alc[j] -= 1
                    drunk_alc[j] += 1
                    return


def Game1():
  import random
  import requests
  from bs4 import BeautifulSoup 

  #url1에 주소를 받아오고 응답이 정상이 아닐경우 오류를 발생시킴
  url1 = "https://coding232624.tistory.com/85"
  response1 = requests.get(url1)
  response1.raise_for_status()

  #받아온 주소에서 subway1을 클래스로 갖는 태그를 가져오고 그안에서 td태그를 text1에 저장 값을 저장할 딕셔너리 변수 dic1생성
  soup1 = BeautifulSoup(response1.text,"html.parser")
  texts_subway1 = soup1.find(class_="subway1")
  texts1 = texts_subway1.find_all("td")
  dic1 = {}

  #반복문 돌며 딕셔너리에 저장
  for i in range(len(texts1)//2):
    dic1[texts1[i*2].get_text()] = texts1[i*2+1].get_text()


  print("지하철~ 지하철~ 몇호선~ 몇호선~")
  line1 = (input("게임을 진행할 지하철의 노선을 입력하세요! : "))
  record1 = []
  check1 = False
  while(True):    
    for i in range(len(game_people)):
      if(game_people[i] == player_name):
        sub1 = input("지하철역 이름을 입력하세요! : ")
      else:
        sub1, line_now = random.choice(list(dic1.items()))
      print(i ,' : ',  sub1)
      if(sub1 in dic1 and not(sub1 in record1)):
        if(dic1[sub1] != line1):
          print("오답입니다!" ,game_people[i],"님이 게임에서 패배하셨습니다!")
          drunk_alc[i] += 1
          people_alc[i] -= 1
          check1 = True
          break
      else:
        print("오답입니다!" ,game_people[i],"님이 게임에서 패배하셨습니다!")
        drunk_alc[i] += 1
        people_alc[i] -= 1
        check1 = True
        break
      record1.append(sub1)
    if(check1):
      break
########################################################################################################
# 왕게임
# 랜덤으로 왕을 뽑고 랜덤하게 지시를 내림
# 술 마시라는 지시를 내리면 게임종료
# player가 왕이 되었을 시 지시를 직접 내린다 (이름을 먼저 말하고 "술"이 포함된 지시를 내리면 게임종료)
def game2():
  pick_king2 = random.randint(1, g_num+2)
  #pick_king2 = 6

  if pick_king2 == g_num + 2:
      print(f"{player_name}이 왕입니다!!")
  else:
      print(f"{game_people[pick_king2-1]}이(가) 왕입니다!!")

  can_pick_num2 = []
  for k2 in range(1, g_num + 2):
      if k2 != pick_king2:
          can_pick_num2.append(k2)
  
  commands2 = ["뉴진스 춤춰~!",
              "신나는 노래해~!",
              "메로나 사와~!",
              "술 마셔~!",
              "안주 만들어 와~",
              "성대모사 하나 하기!"]
  i2 = 0
  while True:
      i2 += 1
      if pick_king2 == g_num + 2:
          x2 = input("지시를 입력하세요: ")
          if "술" in x2:
              print(f"왕의 {i2}번째 지시:  " + x2)
              ##x2에서 처음 두글자를 따로 저장해서 game_people 안에 있는 값과 비교하기
              for i in range(len(game_people)):
                  if x2[:2] == game_people[i]:
                     pick_num2 = i + 1  # 왕이 지목한 사람의 인덱스
                     drunk_alc[pick_num2-1] += 1
                     people_alc[pick_num2-1] -= 1
              break
          print(f"왕의 {i2}번째 지시:  " + x2)
      else:
          pick_num2 = random.choice(can_pick_num2)

          random_command2 = random.randint(0, len(commands2) - 1)

          print(f"왕의 {i2}번째 지시: {game_people[pick_num2-1]}이(가) " + commands2[random_command2])
          if random_command2 == 3:
              drunk_alc[pick_num2-1] += 1
              people_alc[pick_num2-1] -= 1
              break

######################################################################################################
######################################################################################################
def Game4():
    print()
    print("🎲🌟🎲🌟🎲🌟🎲🌟🎲🌟🎲🌟🎲🌟🎲🌟🎲")
    print("  ###      ###      ###  ")
    print("    #     #        #   # ")
    print("  ###     ####      #### ")
    print("    #     #   #        # ")
    print("  ###      ###      ###  ")
    print("🎲🌟🎲🌟🎲🌟🎲🌟🎲🌟🎲🌟🎲🌟🎲🌟🎲")
    print()

    current_number = 1
    player_turn = 0
    game_sequence = "" 

    while True:
        correct_response = ''
        for digit in str(current_number):
            if digit in ['3', '6', '9']:
                correct_response += 'X'

        # 진짜 플레이어
        if game_people[player_turn] == player_name:
            print()
            player_input = input(f"{player_name},님 게임을 진행할 [숫자] 또는 ['X'👏] 를 입력하세요 : ").strip().upper()
            print()
        # NPC
        else:
          if correct_response:  # 3,6,9 일 때
            npc_mistake = random.choice([True, False])
            # NPC가 실수를 한 케이스
            if npc_mistake:
              incorrect_response_type = random.choice([1, 2])
              # 박수 대신 숫자를 말함
              if incorrect_response_type == 1:
                player_input = str(current_number)
              # 박수 개수 틀림
              else:
                num_of_X = random.randint(1, len(correct_response) + 1)
                player_input = 'X' * num_of_X
            # # NPC가 정답을 말함 케이스
            else:
              player_input = correct_response 
          else: # 3,6,9가 아닐 때
                player_input = str(current_number)

          print(f"{game_people[player_turn]}👤: {player_input.replace('X', '👏')} ")

        game_sequence += player_input.replace('X', '👏') + " → "
        print("~~~~~~~ 🎮 현재 진행 상황 🎮 ~~~~~~~~    " + game_sequence.rstrip(" → "))

        # 승패 결정
        if (correct_response and player_input != correct_response) or (not correct_response and player_input != str(current_number)):
            print(f"오답입니다! {game_people[player_turn]} 님이 게임에서 패배하셨습니다!")
            print(f"\n누가 술을 마셔 {game_people[player_turn]} 가(이) 술을 마셔 원샷~~~\n")
            # 술을 마시는 경우
            drunk_alc[player_turn] += 1  
            people_alc[player_turn] -= 1  
            return

        # 다음 사람 차례로 넘기기
        current_number += 1
        player_turn = (player_turn + 1) % len(game_people)
######################################################################################################
def print_remain_alc():
   for i in range(len(game_people)):
    print("{}은(는 ) 지금까지 {}! 치사량까지 {}".format(game_people[i], drunk_alc[i], people_alc[i]))
######################################################################################################
def get_valid_input(prompt, valid_values):
    while True:
        try:
            value = input(prompt)
            if value.lower() in valid_values:
                return value.lower()
            print("입력이 잘못되었습니다. 다시 입력해주세요.")
        except ValueError:
            print("입력이 잘못되었습니다. 다시 입력해주세요.")

def print_remain_alc():
   for i in range(len(game_people)):
    print("{}은(는 ) 지금까지 {}! 치사량까지 {}".format(game_people[i], drunk_alc[i], people_alc[i]))

def get_valid_number(prompt, min_value, max_value):
    while True:
        try:
            number = int(input(prompt))
            if min_value <= number <= max_value:
                return number
            else:
                print(f" {min_value} 과 {max_value} 사이 입력해주세요.")
        except ValueError:
            print("입력이 잘못되었습니다. 다시 입력해주세요.")
######################################################################################################
            
import sys
import random

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("게임시작")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
y_or_n = get_valid_input("게임을 진행할까요? (y/n) : ", ['y', 'n'])
if(y_or_n == 'n'):
  print("게임을 종료합니다")
  sys.exit()

#플레이어 이름 설정
player_name = input("오늘 거하게 취해볼 당신의 이름은? : ")
print("~~~~~~~~~~~~~소주 기준 당신의 주량은?~~~~~~~~~~~~~")
print("{:>27}".format("1. 소주 반병(2잔)"))
print("{:>27}".format("2. 소주 반병에서 한병(4잔)"))
print("{:>27}".format("3. 소주 한병에서 한병 반(6잔)"))
print("{:>27}".format("4. 소주 한병 반에서 두병(8잔)"))
print("{:>27}".format("5. 소주 두병 이상(10잔)"))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#본인 주량 설정
player_alc = get_valid_number("당신의 치사량(주량)은 얼마만큼인가요?(1~5을 선택해주세요 ) : ", 1, 5)

#같이 취할 친구 찾기
g_num = get_valid_number("함께 취할 친구들은 얼마나 필요하신가요?(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!) : ", 0, 3)
game_people = [player_name]
people_alc = [player_alc * 2]
drunk_alc = [0]
rand_name = ["기택", "재관", "웨이", "현정"]
for i in range(g_num):
  rand_num_alc = random.randint(1,5)
  while True:
    rand_num_people = random.randint(0,3)
    if rand_name[rand_num_people] not in game_people:
      game_people.append(rand_name[rand_num_people])
      break
    else:
       continue
  people_alc.append(rand_num_alc*2)
  drunk_alc.append(0)
  print("오늘 함께 취할 친구는 {}입니다! (치사량 : {})".format(game_people[i+1], people_alc[i+1]))

#여기서부터 반복예정
#게임 메뉴
dur = True
while(dur):
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print_remain_alc()

  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("~~~~~~~~~~~~~~오늘의 Alcohol Game~~~~~~~~~~~~~~~")
  print("{:>27}".format("1. 지하철"))
  print("{:>27}".format("2. 왕게임"))
  print("{:>27}".format("3. 아파트"))
  print("{:>29}".format("4. 3 6 9"))
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  if(game_people[0] != player_name):
    exit = input("술게임 진행중! 다른 사람의 턴입니다. 그만하고 싶으면 \"exit\"를, 계속하고 싶으면 아무키나 입력해 주세요 ! : ")
    game_num = random.randint(1,4)
    # game_num = ("{}(이 )가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨게임? : {}".format(game_people[0],game_num))
    if (exit == 'exit'):
      print("게임을 종료합니다")
      sys.exit()
  else:
    game_num = get_valid_number("{}(이 )가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨게임? : ".format(game_people[0]), 1, 4)
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("{} 님이 게임을 선택하셨습니다! ".format(game_people[0]))

  if game_num == '1' or game_num == 1:
        Game1()  
  elif game_num == '2' or game_num == 2:
        game2()  
  elif game_num == '3' or game_num == 3:
        apart_game()  
  elif game_num == '4' or game_num == 4:
        Game4()


  if(0 in people_alc):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print_remain_alc()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print('='*60)
    print('='*60)
    print("\n")
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⢀⣤⣤⣤⣶⣶⣷⣤⣀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣶⣶⠀⠀⠀⠀⣠⣾⣿⣿⡇⠀⣿⣿⣿⣿⠿⠛⠉⠉⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⠀⠀⠀⠀⠀⢀⣿⣿⣶⡀⠀⠀⠀⠀⠀⣾⣿⣿⣿⡄⠀⢀⣴⣿⣿⣿⣿⠁⢸⣿⣿⣿⣀⣤⡀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⣼⣿⣿⣿⣧⠀⠀⠀⠀⢰⣿⣿⣿⣿⣇⣠⣿⣿⣿⣿⣿⡏⢠⣿⣿⣿⣿⣿⡿⠗⠂⠀⠀
    ⠀⠀⠀⣰⣾⣿⣿⠟⠛⠉⠉⠉⠉⠋⠀⠀⠀⣰⣿⣿⣿⣿⣿⣇⣠⣤⣤⣿⣿⣿⢿⣿⣿⣿⣿⢿⣿⣿⡿⠀⣼⣿⣿⡟⠉⠁⢀⣀⡄⠀⠀
    ⠀⢀⣾⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣴⣿⣿⣿⣿⡿⣿⣿⣿⡏⠈⢿⣿⣿⠏⣾⣿⣿⠃⢠⣿⣿⣿⣶⣶⣿⣿⣿⡷⠦⠀
    ⢠⣾⣿⡿⠀⠀⠀⣀⣠⣴⣶⣿⣿⡷⠀⣠⣿⣿⣿⣿⡿⠟⣿⣿⣿⣠⣿⣿⣿⠀⠀⠀⠀⠁⢸⣿⣿⡏⠀⣼⣿⣿⣿⠿⠛⠛⠉⠀⠀⠀⠀
    ⢸⣿⣿⠣⣴⣾⣿⣿⣿⣿⣿⣿⡿⠃⣰⣿⣿⣿⠋⠁⠀⠀⠸⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠸⠿⠿⠀⠀⠛⠛⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠸⣿⣿⣆⣉⣻⣭⣿⣿⣿⡿⠋⠀⠀⢿⣿⡿⠁⠀⠀⠀⠀⠀⠹⠟⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠙⠿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣶⣶⣶⣶⣦⣄⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣷⠄⣤⣤⣤⣤⣶⣾⣷⣴⣿⣿⣿⣿⠿⠿⠛⣻⣿⣿⣷⡄
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣄⠀⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠋⢠⣿⣿⣿⠿⠛⠋⠉⠛⣿⣿⣿⠏⢀⣤⣾⣿⣿⡿⠋⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⠓⢹⣿⣿⣷⠀⠀⠀⠀⢀⣶⣿⡿⠁⠀⣾⣿⣿⣟⣠⣤⠀⠀⢸⣿⣿⣿⣾⣿⣿⣿⡟⠋⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⡿⠛⠉⠸⣿⣦⡈⣿⣿⣿⡇⠀⠀⣰⣿⣿⡿⠁⠀⢸⣿⣿⣿⣿⣿⠿⠷⢀⣿⣿⣿⣿⡿⠛⣿⣿⣿⡀⠀⠀⠀
    ⠀⠀⠀⠀⢀⣼⣿⣿⡿⠋⠀⠀⠀⠀⣿⣿⣧⠘⣿⣿⣿⡀⣼⣿⣿⡟⠀⠀⢀⣿⣿⣿⠋⠁⠀⣀⣀⣼⣿⣿⡟⠁⠀⠀⠘⣿⣿⣧⠀⠀⠀
    ⠀⠀⠀⠀⣼⣿⣿⡟⠀⠀⠀⠀⠀⣠⣿⣿⣿⠀⢹⣿⣿⣿⣿⣿⡟⠀⠀⠀⣼⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠸⣿⣿⡆⠀⠀
    ⠀⠀⠀⠀⢹⣿⣿⣇⠀⠀⢀⣠⣴⣿⣿⣿⡿⠀⠈⣿⣿⣿⣿⡟⠀⠀⠀⢰⣿⣿⣿⠿⠟⠛⠉⠁⠸⢿⡟⠀⠀⠀⠀⠀⠀⠀⠘⠋⠁⠀⠀
    ⠀⠀⠀⠀⠈⢻⣿⣿⣿⣾⣿⣿⣿⣿⣿⠟⠁⠀⠀⠸⣿⣿⡿⠁⠀⠀⠀⠈⠙⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠉⠛⠿⠿⠿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
    print('='*60)
    print('='*60)
    print("{}이(가 ) 전사했습니다... 꿈나라에서는 편히 쉬시길...zzz".format(game_people[people_alc.index(0)]))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("{:>27}".format("다음에 술마시면 또 불러주세요~ 안녕 !"))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    dur = False

    break

  tmp1 = game_people.pop(0)
  game_people.append(tmp1)
  tmp2 = people_alc.pop(0)
  people_alc.append(tmp2)
  tmp3 = drunk_alc.pop(0)
  drunk_alc.append(tmp3)
