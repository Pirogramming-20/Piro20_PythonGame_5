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

    if(game_people[0] == player_name):
      betting = int(input("이번판에 몇잔을 걸지 알려주세요!(1~3 중 하나를 입력) : "))
    else:
      betting = random.randint(1,3)
    print(game_people[0],"이 이번판에 건 술은 ",betting,"잔입니다!")

    while True:
        time.sleep(1)
        correct_response = ''
        for digit in str(current_number):
            if digit in ['3', '6', '9']:
                correct_response += 'X'

        # 진짜 플레이어
        if game_people[player_turn] == player_name:
            print()
            player_input = input(f"{player_name},님 게임을 진행할 [숫자] 또는 [👏 (박수 대신 'X')] 를 입력하세요 : ").strip().upper()
            print()
        # NPC
        else:
          if correct_response:  # 3,6,9 해야 될 때
            npc_mistake = random.choice([True, False]) # NPC가 실수를 할지 말지 결정 50% 확률
            # NPC가 실수를 한 케이스
            if npc_mistake:
              incorrect_response_type = random.choice([1, 2]) # 50% 확률로 (1) , (2) 케이스 결정
              # (1) 박수 대신 숫자를 말함
              if incorrect_response_type == 1:
                player_input = str(current_number)
              # (2) 박수 개수 틀림
              else:
                num_of_X = random.randint(1, len(correct_response) + 1)
                player_input = 'X' * num_of_X
            # NPC가 정답을 말함 케이스
            else:
              player_input = correct_response 
          else: # 3,6,9가 아닐 때 맞춰야 하는 숫자를 말함
                player_input = str(current_number)

          print(f"{game_people[player_turn]}👤: {player_input.replace('X', '👏')} ")

        game_sequence += player_input.replace('X', '👏') + " → "
        print("~~~~~~~ 🎮 현재 진행 상황 🎮 ~~~~~~~~    " + game_sequence.rstrip(" → "))

        # 승패 결정
        if (correct_response and player_input != correct_response) or (not correct_response and player_input != str(current_number)):
            print(f"오답입니다! {game_people[player_turn]} 님이 게임에서 패배하셨습니다!")
            print(f"\n누가 술을 마셔 {game_people[player_turn]} 가(이) 술을 마셔 원샷~~~\n")
            # 술을 마시는 경우
            drunk_alc[player_turn] += betting  
            people_alc[player_turn] -= betting
            return

        # 다음 사람 차례로 넘기기
        current_number += 1
        player_turn = (player_turn + 1) % len(game_people)