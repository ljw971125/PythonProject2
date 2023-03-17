# #프로젝트 시작
import os
import tkinter

PATH = os.path.dirname(os.path.realpath(__file__)) #현재 경로로 불러옴
os.chdir(PATH)

window = tkinter.Tk()

window.title("ㅅㅅ") # 제목
window.geometry("640x400") # 해상도("너비x높이+x좌표+y좌표")
window.resizable(True,True) # 화면 크기 조절(가로, 세로)

count = 0

def countUP(): # 실행됫을 때 숫자가 1씩 증가하는 함수
    
    global image
    for i in range(1,400,50):
        image = tkinter.PhotoImage(file="1085477793720172606.png")
        label.config(image=image,width=i,height=150)



label = tkinter.Label(window, fg = "red",cursor="umbrella") # 화면에 출력할 문자(윈도우 창, 매개변수1, 매개변수2, 매개변수3)
label.place(x=50, y= 30)


button = tkinter.Button(window,text= "쪼물쪼물", overrelief="solid", command=countUP, repeatdelay=1000,repeatinterval=1000) # 버튼 설정(윈도우, 창, 매개변수1, 매개변수2, 매개변수3)
button.place(x=3,y=5)

window.mainloop() # 창을 띄어줌

