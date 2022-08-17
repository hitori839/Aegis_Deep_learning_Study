import turtle
import random
import time
import winsound

#setting으로 처음 그림 세팅
#이후 ing로 게임 중 클릭 해야할 화면 제시
import setting
import ing
    
score = 0
nice = 0

def add_one():
    global gg
    gg += 1

#마우스로 클릭하면 배열에 위치 추가
def onClick(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    poli1[gg-1] = x
    poli2[gg-1] = y
    t.penup()

#랜덤으로 주어진 시간에 클릭 기능
def aw(x):
    max_time_end = time.time() + x
    while True:
        scr.onclick(onClick)
        if time.time() > max_time_end:
            break

while True:
    gg = 0
    
#게임 시작 알림
    turtle.penup()
    turtle.goto(-250,200)
    turtle.pendown()
    turtle.write("두더지 잡기 게임을 시작합니다! (제한시간은 60초 입니다)", font = ("맑은고딕",15,"bold"))

    hazime = 20
    
#onClick에서 쓰기 위한 터틀 설정 
    t=turtle.Turtle()
    t.hideturtle()
    t.speed(1000000)

#스크린 설정
    scr=turtle.Screen()
    scr.bgcolor('white')

#게임 음악 반복 재생
    winsound.PlaySound('Walking.wav',winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)

#나중의 맞춘 개수 세기 위한 배열 3개 선언 후 값 미리 삽입
    poli1 = []
    poli2 = []
    for si in range(1000):
        poli1.append(10000)
        poli2.append(10000)
    check = []

#게임 제한시간 
    tm = time.time() + 60

#제한 시간 동안 게임 시작 
    while (time.time() <= tm):
        qud = random.randint(2,5)
        qu = qud / hazime
        st = random.randint(1,9)

#랜덤하게 받은 수에 따라 제시될 위치 선정
        if(st == 1):
            check.append(1)
            ing.one1()
            aw(qu)
            add_one()
            ing.one2()

        elif(st == 2):
            check.append(2)
            ing.two1()
            aw(qu)
            add_one()
            ing.two2()
        
        elif(st == 3):
            check.append(3)
            ing.three1()
            aw(qu)
            add_one()
            ing.three2()

        elif(st == 4):
            check.append(4)
            ing.four1()
            aw(qu)
            add_one()
            ing.four2()

        elif(st == 5):
            check.append(5)
            ing.five1()
            aw(qu)
            add_one()
            ing.five2()

        elif(st == 6):
            check.append(6)
            ing.six1()
            aw(qu)
            add_one()
            ing.six2()

        elif(st == 7):
            check.append(7)
            ing.seven1()
            aw(qu)
            add_one()
            ing.seven2()

        elif(st == 8):
            check.append(8)
            ing.eight1()
            aw(qu)
            add_one()
            ing.eight2()

        elif(st == 9):
            check.append(9)
            ing.nine1()
            aw(qu)
            add_one()
            ing.nine2()

#전체 횟수
    score = len(check)

#맞은 수 체크
    for a in range(0,score):
        if (check[a] == 1):
            if ((-150 < poli1[a]) and (poli1[a] < -50)) and ((-150 < poli2[a]) and (poli2[a] < -50)):
                nice = nice + 1
            
        elif (check[a] == 2):
            if ((-50 < poli1[a]) and (poli1[a] < 50)) and ((-150 < poli2[a]) and (poli2[a] < -50)):
                nice = nice + 1
            
        elif (check[a] == 3):
            if ((50 < poli1[a]) and (poli1[a] < 150)) and ((-150 < poli2[a]) and (poli2[a] < -50)):
                nice = nice + 1
            
        elif (check[a] == 4):
            if ((-150 < poli1[a]) and (poli1[a] < -50)) and ((-50 < poli2[a]) and (poli2[a] < 50)):
                nice = nice + 1
            
        elif (check[a] == 5):
            if ((-50 < poli1[a]) and (poli1[a] < 50)) and ((-50 < poli2[a]) and (poli2[a] < 50)):
                nice = nice + 1
            
        elif (check[a] == 6):
            if ((-50 < poli1[a]) and (poli1[a] < 150)) and ((-50 < poli2[a]) and (poli2[a] < 50)):
                nice = nice + 1
            
        elif (check[a] == 7):
            if ((-150 < poli1[a]) and (poli1[a] < -50)) and ((50 < poli2[a]) and (poli2[a] < 150)):
                nice = nice + 1
            
        elif (check[a] == 8):
            if ((-50 < poli1[a]) and (poli1[a] < 50)) and ((50 < poli2[a]) and (poli2[a] < 150)):
                nice = nice + 1
            
        elif (check[a] == 9):
            if ((50 < poli1[a]) and (poli1[a] < 150)) and ((50 < poli2[a]) and (poli2[a] < 150)):
                nice = nice + 1

#결과 음악 재생
    winsound.PlaySound('LevelUP.wav', winsound.SND_FILENAME)

#결과 발표 & 다시 할지 입력 받기
    if (score == nice):
        oh = "Perfect!!!"
    else:
        oh = "유감..."
        
    tasuk = turtle.textinput("결과","%s\n전체 경우의 수 : %d / 맞춘 개수 : %d\nReplay - 1 / Stop - 아무 버튼" %(oh, score, nice))
    tasu = int(tasuk)
    if (tasu == 1):
        continue
    else:
        break
    
scr.listen()
scr.mainloop()
