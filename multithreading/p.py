import winsound as w
import threading as t
from os import system

def heli():
    c=0
    while(c<1000):
        system('CLS')
        if c%2==0 :
            print(3*' ',11*'*')
        else:
            print(15*' ',11*'*')
        print(14*' ','*')
        print(14*' ','*')
        print(5*' ',15*'*')
        for i in range(5):
            print((5-i-1)*' ','*',(12+i)*' ','*',end="")
            if i==2:
                print(7*'*',end="")
            print()
        
        print(20*'*')
        c+=1
def play():
    w.PlaySound('helicopter.wav',w.SND_NODEFAULT)
t1=t.Thread(target=heli,args=())
t2=t.Thread(target=play,args=())
t1.start()
t2.start()
