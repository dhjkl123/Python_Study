class calc:
    def __init__(self,inacount,inname,inmoney):
        self.acount = int(inacount)
        self.name = inname
        self.money = inmoney

    def AddMoney(self,inmoney):
        self.money += inmoney

    def SubMoney(self,inmoney):
        self.money -= inmoney

    def PrintAcount(self):
        print("계좌번호")
        print(self.acount)
        print("이름")
        print(self.name)
        print("금액")
        print(self.money)

client = {}
Continue = True

def start():
    print("1. 계좌개설")
    print("2. 입금")
    print("3. 출금")
    print("4. 계좌정보 전체 출력")
    print("5. 프로그램 종료")


while(Continue) :
    start()
    sel = int(input())

    if(sel == 1):
        print("이름 계좌번호를 입력해주세요")
        name,acount = map(str, input().split())
        client[acount] = calc(acount,name,0)

    elif(sel == 2):
        print("입금 계좌 번호")
        anct = input()
        print("입금 금액")
        money = int(input())
        client[anct].AddMoney(money)

    elif(sel == 3):
        print("출금 계좌 번호")
        anct = input()
        print("출금 금액")
        money = int(input())
        client[anct].SubMoney(money)

    elif (sel == 4):
        print("계좌정보 전체 출력")
        for k in client.keys():
            print(f"계좌번호 : {client[k].acount} / 이름 : {client[k].name} / 잔액 : {client[k].money}")

    elif(sel == 5):
        print("프로그램을 종료합니다")
        Continue = False
