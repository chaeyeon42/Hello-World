#스토리 설명은 한 문단씩 출력, 시간차를 두고 출력

import time
start = time.time()

print("상명대학교에 재학중인 A는 강아지를 키우며 자취를 하고 있다.")
time.sleep(2.5)
print("하지만 수업이 대면으로 전환이 되었고, 급하게 강아지를 돌보아줄 사람을 수소문 하였지만 찾지 못한 상황이다.")
time.sleep(2.5)
print("수업을 코앞에 두고 A의 뇌리에는 자동 급식기를 만들자는 아이디어가 스쳤고, 이를 실행에 옮기려고 한다.")
time.sleep(2.5)
print("A를 도와 자동 급식기를 만들어보자.")
time.sleep(2.5)

#공급 방식 기획
#큐 or 스택 방식 중 어느 방식으로 사료를 공급할지 선택을 하도록
#큐, 스택 설명문 출력 후 선택하도록
print("\n\n**stage1. 공급 방식 기획**")
time.sleep(2.5)
print("\n스택과 큐 방식 중 어느 방식으로 지급할 지 보기에서 선택하자.")
time.sleep(1.5)
print("<보기>\n1. 스택\n2. 큐 \n3. 힌트")

time.sleep(2)
select1 = int(input("번호를 선택하세요 : "))
if select1 == 3 :
        print("스택 방식은 선입후출先入先出 방식입니다. \n큐 방식은 선입선출先入後出 방식입니다.")
        select2 = int(input("번호를 선택하세요 : "))
        if select2 == 1 :
                print("스택 방식으로 공급합니다. \n공급방식이 결정되었다! \nstage1 클리어!")
        elif select2 == 2 :
                print("큐 방식으로 공급합니다. \n공급방식이 결정되었다! \nstage1 클리어!")


elif select1 == 1 :
        print("스택 방식으로 공급합니다. \n공급방식이 결정되었다! \nstage1 클리어!")
elif select1 == 2 :
        print("큐 방식으로 공급합니다. \n공급방식이 결정되었다! \nstage1 클리어!")



#자동 급식기 조립
#조립코드는 이미지로 띄우고, 빈칸blank을 채우도록
print("\n\n**stage2. 자동 급식기 조립**")
time.sleep(2.5)
print("\n자동 급식기를 조립하자.")
time.sleep(1.5)
print("자동 급식기는 하늘색의 사각형 형태로 만들 계획이다.")
time.sleep(1.5)
print("입구의 색은 회색, 크기는 본체의 4분의 1 정도이다.")
time.sleep(2)
print("조립 코드는 다음과 같다. (blank)를 채워나가자.")

time.sleep(2.5)

from PIL import Image
im = Image.open('조립코드.jpg')
im.show()


puzzle = [
    ["(blank1)에 들어갈 코드는? \n1.math \n2.turtle \n3.time \n4.random","2"],
    ["(blank2)에 들어갈 코드는? \n1. 0 \n2. 90 \n3. 180\n4. 360","2"],
    ["(blank3)에 들어갈 코드는? \n1. 181 \n2. 180 \n3. 281 \n4. 280","3"],
    ["(blank4)에 들어갈 코드는? \n1. 110 \n2. 120 \n3. 130 \n4. 140","4"],
    ["(blank5)에 들어갈 코드는? \n1. gray \n2. skyblue \n3. pink \n4. yellow","1"],
    ["(blank6)에 들어갈 코드는? \n1. 1 \n2. 2 \n3. 3 \n4. 4","4"],
    ]

for x, y in puzzle:
    print(x)
    user_input = input()

    if user_input == y:
        print("정답!")
        time.sleep(1.5)
    else:
        while True:
            print("오답. 다시 생각해 보자.")
            print(x)
            user_input = input()
            if user_input == y:
                print("정답!")
                time.sleep(1.5)
                break
        continue

print("stage2 클리어!")

#배식 시간과 사료 종류 결정
#리스트를 출력하고, 빈칸blank을 채우도록
print("\n\n**stage3. 배식 시간과 사료 종류 결정**")
time.sleep(2.5)
print("\n자동 급식 시간과 사료 종류를 설정하자.")
time.sleep(1.5)
print("시간과 사료 종류를 연결할 수 있어야 하고, 수정이 용이해야 한다.")
time.sleep(1.5)
puzzle = [
    ["어떤 함수를 사용해야 할 지 보기에서 선택하자. \n<보기>\n1. 리스트\n2. 딕셔너리\n3. 튜플","2"],
    ]

for x, y in puzzle:
    print(x)
    user_input = input()

    if user_input == y:
        print("정답!")
        time.sleep(1.5)
    else:
        while True:
            print("오답. 다시 생각해 보자.")
            print(x)
            user_input = input()
            if user_input == y:
                print("정답!")
                time.sleep(1.5)
                break
        continue

time.sleep(1.5)

from PIL import Image
im = Image.open('딕셔너리 코드.jpg')
im.show()


print("\n딕셔너리 함수를 사용해 설정을 마쳤다.")
time.sleep(2.5)
print("\nA : 아차! 이전에 먹이던 간식이 품절돼서 새로운 간식으로 바꿨다는 걸 깜빡했다.")
time.sleep(2.5)
print("\n간식 딕셔너리 속 '사료 종류' 값을 '리리펫 치킨트릿'으로 변경하려먼 어떤 명령어를 입력해야 할지 선택하자.\n")
time.sleep(1.5)

puzzle = [
    ["어떤 함수를 사용해야 할 지 보기에서 선택하자. \n<보기>\n1. snack['사료 종류']='리리펫 치킨트릿'\n2. snack[사료 종류]='리리펫 치킨트릿'\n3. snack['사료 종류']=리리펫 치킨트릿 \n4. snack[사료 종류]=리리펫 치킨트릿","1"],
    ]

for x, y in puzzle:
    print(x)
    user_input = input()

    if user_input == y:
        print("정답!")
        time.sleep(2.5)
    else:
        while True:
            print("오답. 다시 생각해 보자.")
            print(x)
            user_input = input()
            if user_input == y:
                print("정답!")
                time.sleep(2.5)
                break
        continue

time.sleep(1.5)

from PIL import Image
im = Image.open('딕셔너리 코드(2).jpg')
im.show()

print("\n설정이 완료되었다!")
time.sleep(1.5)
print("stage3 클리어!")


#배식량 계산
#소수점 아래 14자리까지 계산하므로 두 자리에서 반올림해야 함
print("\n\n**stage4. 배식량 계산**")
time.sleep(2.5)
weight = 0
amount = 0
amount2 = 0
RER = 0
DER = 0


weight = float(input("\n강아지 몸무게를 kg 단위로 입력하자 : "))

RER = weight * 30 + 70
DER = RER*1.6

amount = DER/3654*1000
amount2 = amount/3

time.sleep(1.5)
print("일일 에너지 요구량은", round(DER),"kcal이며")
time.sleep(1.5)
print("하루 총 급여 양은", round(amount), "g이므로,")
time.sleep(2.5)
print("식사는 한 번에", round(amount2),"g씩 세 번 급여하자.")
time.sleep(1.5)
print("간식은 공강인 날에 급여하도록 하자.")
time.sleep(2.5)
print("stage4 클리어!")

#튜플 설정
#모든 코드를 튜플화 하여야 하나, 명령어를 찾지 못하여 문구만 띄우도록 함
print("\n\n**stage5. 저작권 보호**")
time.sleep(2.5)
print("\n지금까지 A를 도와 자동 급식기를 완성하였다.")
time.sleep(2.5)
print("A는 완성한 자동 급식기에 대한 저작권 보호를 위하여 보안 설정을 하고자 한다.")
time.sleep(2.5)
print("이때 필요한 코드를 보기에서 선택하자.")
time.sleep(2.5)
print("<보기>\n1. 리스트\n2. 딕셔너리\n3. 튜플\n4. 함수")

while True :
    select = int(input("번호를 선택하세요 : "))
    if select == 3 :
         print("정답! 모든 코드가 튜플화 되었다.")
         time.sleep(2.5)
    else :
         print("오답. 다시 생각해 보자.")
    if select == 3:
        time.sleep(2.5)
        break

#게임 엔딩
print("\n\n이로서 A를 도와 자동 급식기를 완성하였다!")
print("제작까지 걸린 시간은" , round((time.time() - start)/60, 0), "분이 걸렸다.")
