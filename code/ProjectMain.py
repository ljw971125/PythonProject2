from tkinter import *
import tkinter as tk # 인터페이스를 만들 때import os 
from PIL import Image, ImageTk
import pandas as pd # 데이터 프레임을 만들 수 있는 모듈
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os 

PATH = os.path.dirname(os.path.realpath(__file__))
os.chdir(PATH)

class Accident(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartMenu)
        self.title("서울시 사고유형 분석") # ui 제목
        self.geometry("1180x700") # ui 시작 해상도
        photo = ImageTk.PhotoImage(Image.open('car.png')) # ui 아이콘 불러오기
        self.wm_iconphoto(False, photo) # ui 아이콘 적용하기

    def switch_frame(self, frame_class): 
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

# 시작 화면
class StartMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="서울시 교통사고 조사", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5) # 시작 화면 상단 라벨
        self.photo = ImageTk.PhotoImage(Image.open('car.png')) # ui 아이콘 불러오기
        tk.Label(self,image=self.photo).pack() # 이미지 라벨
        tk.Label(self, text="2팀 : 김민수, 이지운, 장기헌, 장윤종, 전장현", font=('Helvetica', 10, "bold")).pack(side="top", fill="x", pady=5) #시작 화면 팀 라벨
        tk.Button(self, text="start",width=20,height=2,command=lambda: master.switch_frame(MainMenu)).pack(side=BOTTOM) # 시작 버튼

class MainMenu(tk.Frame):
     def __init__(self, master):
        tk.Frame.__init__(self, master)
        frame = tk.Frame()
        frame.pack(fill=BOTH)
        bt=Button(self,text="사고 유형 분석",width=43,height=3,background='white',font=20,command=lambda: master.switch_frame(Menu1))
        bt.pack(side=LEFT,expand=True,fill=BOTH)
        bt2=Button(self,text="사고 유형 상세 분석",width=43,height=3,background='white',font=20,command=lambda: master.switch_frame(Menu2))
        bt2.pack(side=LEFT,expand=True,fill=BOTH)
        bt3=Button(self,text="유형별 최다 사고",width=43,height=3,background='white',font=20,command=lambda: master.switch_frame(Menu3))
        bt3.pack(side=LEFT,expand=True,fill=BOTH)

class Menu1(tk.Frame):
     def __init__(self, master):
        tk.Frame.__init__(self, master)
        bt=Button(self,text="사고 유형 분석",width=40,height=3,background='grey',font=20)
        bt.grid(row=0,column=0,sticky='NSEW')
        bt2=Button(self,text="사고 유형 상세 분석",width=40,height=3,background='white',font=20,command=lambda: master.switch_frame(Menu2))
        bt2.grid(row=0,column=1,sticky='NSEW')
        bt3=Button(self,text="상세 분석",width=40,height=3,background='white',font=20)
        bt3.grid(row=0,column=2,sticky='NSEW')
        listbox = tk.Listbox(self, selectmode='extended', height=0)

        df1=pd.read_csv('서울시 사고유형.csv',encoding='cp949')
        for i in range(0,25):
            listbox.insert(tk.END, df1.loc[i][0])
        listbox.grid(row=1,column=0,sticky='w')
        
class Menu2(tk.Frame):
     def __init__(self, master):
        tk.Frame.__init__(self, master)
        bt=Button(self,text="사고 유형 분석",width=40,height=3,background='white',font=20,command=lambda: master.switch_frame(Menu1))
        bt.pack(side=LEFT,expand=True,fill=BOTH)
        bt2=Button(self,text="사고 유형 상세 분석",width=40,height=3,background='grey',font=20)
        bt2.grid(side=LEFT,expand=True,fill=BOTH)



if __name__ == "__main__":
    app = Accident()
    app.mainloop()