# #프로젝트 시작
import os
import tkinter as tk

PATH = os.path.dirname(os.path.realpath(__file__)) #현재 경로로 불러옴
os.chdir(PATH)

window = tk.Tk()

window.title("ㅅㅅ") # 제목
window.geometry("240x150") # 해상도("너비x높이+x좌표+y좌표")
window.resizable(True,True) # 화면 크기 조절(가로, 세로)

count = 0

def countUP(): # 실행됫을 때 숫자가 1씩 증가하는 함수
    
    global image
    image = tk.PhotoImage(file="1085477793720172606.png")
    label.config(image=image,width=150,height=150)



label = tk.Label(window, fg = "red",cursor="umbrella") # 화면에 출력할 문자(윈도우 창, 매개변수1, 매개변수2, 매개변수3)
label.place(x=3,y=5)


button = tk.Button(window,text= "쪼물쪼물", overrelief="solid", command=countUP, repeatdelay=1000,repeatinterval=1000) # 버튼 설정(윈도우, 창, 매개변수1, 매개변수2, 매개변수3)
button.place(x=180,y=100)

window.mainloop() # 창을 띄어줌
