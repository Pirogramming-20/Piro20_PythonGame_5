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



import sys
import random

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("게임시작")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
y_or_n = input("게임을 진행할까요? (y/n) : ")
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
player_alc = int(input("당신의 치사량(주량)은 얼마만큼인가요?(1~5을 선택해주세요 ) : "))

#같이 취할 친구 찾기
g_num = int(input("함께 취할 친구들은 얼마나 필요하신가요?(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!) : "))
game_people = [player_name]
people_alc = [player_alc * 2]
drunk_alc = [0]
rand_name = ["기택", "재관", "웨이", "현정"]
for i in range(g_num):
  rand_num_people = random.randint(0,3)
  rand_num_alc = random.randint(1,5)
  game_people.append(rand_name[rand_num_people])
  people_alc.append(rand_num_alc*2)
  drunk_alc.append(0)
  print("오늘 함께 취할 친구는 {}입니다! (치사량 : {})".format(game_people[i+1], people_alc[i+1]))

#여기서부터 반복예정
#게임 메뉴
while(True):
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  for i in range(len(game_people)):
    print("{}은(는 ) 지금까지 {}! 치사량까지 {}".format(game_people[i], drunk_alc[i], people_alc[i]))

  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("~~~~~~~~~~~~~~오늘의 Alcohol Game~~~~~~~~~~~~~~~")
  print("{:>27}".format("1. 지하철"))
  print("{:>27}".format("2. 금지어 or 왕게임"))
  print("{:>27}".format("3. 아파트"))
  print("{:>27}".format("4. 3 6 9"))
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  if(game_people[0] != player_name):
    exit = input("술게임 진행중! 다른 사람의 턴입니다. 그만하고 싶으면 \"exit\"를, 계속하고 싶으면 아무키나 입력해 주세요 ! : ")
    game_num = random.randint(1,4)
    game_num = ("{}(이 )가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨게임? : {}".format(game_people[0],game_num))
    if (exit == 'exit'):
      print("게임을 종료합니다")
      sys.exit()
  else:
    game_num = input("{}(이 )가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨게임? : ".format(game_people[0]))
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("{} 님이 게임을 선택하셨습니다! ".format(game_people[0]))
  if(game_num == '1'):
    Game1()
  elif(game_num == '2'):
    Game1()
  elif(game_num == '3'):
    Game1()
  elif(game_num == '4'):
    Game1()

  if(0 in people_alc):
    print("{}이(가 ) 전사했습니다... 꿈나라에서는 편히 쉬시길...zzz".format(game_people[people_alc.index(0)]))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("{:>27}".format("다음에 술마시면 또 불러주세요~ 안녕 !"))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

  tmp1 = game_people.pop(0)
  game_people.append(tmp1)
  tmp2 = people_alc.pop(0)
  people_alc.append(tmp2)
  tmp3 = drunk_alc.pop(0)
  drunk_alc.append(tmp3)