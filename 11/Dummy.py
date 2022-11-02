# class Star:
#     name = "star"
#     x = 100
#
#     def change():
#         x= 200
#         print('x is ', x)
#
# print('x IS ', Star.x)
# Star.change()
# print('x IS ', Star.x)
#
# #star = Star()           # 굳이 객체를 생성하는 것도 가능?
# #print('x IS ', star.x)  # 객체 변수로 액세스하지만, 뭘로 귀착? 클래스 변수 x를 가리킨다
# #star.change()           # 실행 안된다
#
# class Player:
#     name = "player" # 클래스 변수
#
#     def __init__(self):
#         self.x = 100
#     def where(my):      # 어차피 자기 자신을 나타내는 객체다, 관습적으로 self라 적은거지
#         print('player is ', my.x)
#
# player = Player()
# player.where()
#
# print(Player.name)  # 클래스 변수 출력
# print(player.name)  # name이라는 객체 변수가 없으면, 같은 이름의 클래스 변수가 선택된다
#
#
# player.where() # ==> (Player.where(player) # 원칙적인 파이썬의 멤버 함수 호출) 와 동일
# #Player.where() # Error

# dictonary의 dictonary
table = {
    "SLEEP": {"HIT", "WAKE"},
    "WAKE": {"TIMER10", "SLEEP"}
}

cur_state = "SLEEP"
next_state = table[cur_state]["HIT"]
