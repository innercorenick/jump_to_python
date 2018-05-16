#-*-coding: utf-8-*-
cof=10 #coffee는 10개가 있다.
print("돈을 넣어주세요")
money=int(input())
while True:
    print("돈을 넣어주세요")
    money=int(input())
    print("커피를 드리겠습니다.\n잠시만 기다려 주세요")
    money-=300 #money에 change를 넣는다.
    if money==300:
        cof-=1
        print("커피입니당\n남은 커피는 %d개 입니다." %cof)
        
    elif money>300:
        cof-=1
        print("커피입니당\n남은 커피는 %d개, 거스름돈은 %d입니다." %cof, %money)
    
    else:
        print("wrong")
    if not cof:
        print("이런 coffee가 없어요")
        break