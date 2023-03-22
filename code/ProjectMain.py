from tkinter import *
import tkinter as tk # 인터페이스를 만들 때
import csv # csv 파일을 불러올 때 사용합니다
import os 
from PIL import Image, ImageTk
import pandas as pd # 데이터 프레임을 만들 수 있는 모듈
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

PATH = os.path.dirname(os.path.realpath(__file__)) # 현재 디렉토리로 이동
os.chdir(PATH)
print(PATH)

class Accident(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartMenu)
        self.title("서울시 사고유형 분석") # ui 제목
        self.geometry("1200x480") # ui 시작 해상도
        photo = ImageTk.PhotoImage(Image.open('car.png')) # ui 아이콘 불러오기
        self.wm_iconphoto(False, photo) # ui 아이콘 적용하기

        # 메뉴 바
        menubar = Menu(self)
        menu=Menu(menubar, tearoff=0)
        menu.add_command(label="사용 설명서") # 하위 메뉴
        menu.add_command(label="종료",command=quit)
        menubar.add_cascade(label="도움말", menu=menu) # 상단 메뉴바 이름
        self.config(menu=menubar)

    # 프레임 이동 함수
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
        tk.Button(self, text="start",width=20,height=2,command=lambda: master.switch_frame(MainMenu1)).pack(side=BOTTOM) # 시작 버튼
        
# 사고 유형 분석 메뉴
class MainMenu1(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        # 콜백 함수 정의
        f = open('서울시.csv') # csv 파일을 불러오기
        reader = csv.reader(f) 
        data = [row[2] for row in reader] #csv 파일에서 2열부터의 값을 가져오기
        
        var=StringVar()
        var.set(NONE)
        def selection():  
            label.config(text="선택한 옵션: " + var.get())
 

        # 프레임 생성
        frame1 = tk.Frame()
        frame2 = tk.Frame() # 프레임 생성
        frame3 = tk.Frame()

        frame1.pack(fill=BOTH)
        frame2.pack(side=LEFT,anchor='n') # 프레임을 왼쪽 정렬
        frame3.pack(side=RIGHT)


        scrollbar = Scrollbar(frame2) # 스크롤바 생성
        scrollbar.pack(side=RIGHT, fill=Y) # 스크롤바를 프레임의 오른쪽에 붙임

        mylist = Listbox(frame2, yscrollcommand=scrollbar.set, height=0, selectbackground='pink', selectforeground='black',font=20) # 리스트바 생성, 스크롤바 연결, 높이 0으로 설정
        for data in data[2:]: # csv 파일의 3행부터 불러옴
            mylist.insert(tk.END, data)
        mylist.pack(side=LEFT,anchor='n',fill=BOTH) # 리스트바를 프레임의 왼쪽에 붙임
        scrollbar.config(command=mylist.yview)
        
        
        R1 = Radiobutton(frame3, text='음주운전',variable=var, value="음주운전",command=selection,font=20) # 오른쪽 프레임 체크박스 추가
        R1.pack(anchor='w') # 왼쪽으로 정렬
        R2 = Radiobutton(frame3, text='무면허',variable=var, value="무면허",command=selection,font=20)
        R2.pack(anchor='w')
        R3 = Radiobutton(frame3, text='스쿨존',variable=var, value="스쿨존",command=selection,font=20)
        R3.pack(anchor='w')
        R4 = Radiobutton(frame3, text='과속',variable=var, value="과속",command=selection,font=20)
        R4.pack(anchor='w')
        R5 = Radiobutton(frame3, text='신호위반',variable=var, value="신호위반",command=selection,font=20)
        R5.pack(anchor='w')
        # 버튼을 눌럿을때 나오는 그래프 추가
        def graph():
            try:
                global canvas
                canvas.get_tk_widget().pack_forget()
                df1=pd.read_csv('서울시.csv',encoding='cp949')
                df1=df1.iloc[:,1:]
                index = mylist.curselection()[0]
                info = mylist.get(index)
                for i in range(1,26):
                    if(info == df1.iloc[i,1]):
                        if(var.get()=='신호위반'):   
                            fig=plt.figure(figsize=(7,3),dpi=300)
                            ax=fig.add_subplot(111)
                            ax.plot(df1.columns[4::5],list(map(int,df1.iloc[i,4::5])))
                            #ax.set_title(info+"의 신호위반")
                            canvas = FigureCanvasTkAgg(fig,master=self)
                            canvas.get_tk_widget().pack()
                        elif(var.get()=='과속'):
                            fig=plt.figure(figsize=(7,3),dpi=300)
                            ax=fig.add_subplot(111)
                            ax.plot(df1.columns[3::5],list(map(int,df1.iloc[i,3::5])))
                            canvas = FigureCanvasTkAgg(fig,master=self)
                            canvas.get_tk_widget().pack()
                        elif(var.get()=='스쿨존'):
                            fig=plt.figure(figsize=(7,3),dpi=300)
                            ax=fig.add_subplot(111)
                            ax.plot(df1.columns[6::5],list(map(int,df1.iloc[i,6::5])))
                            canvas = FigureCanvasTkAgg(fig,master=self)
                            canvas.draw()
                            canvas.get_tk_widget().pack()
                        elif(var.get()=='무면허'):
                            fig=plt.figure(figsize=(7,3),dpi=300)
                            ax=fig.add_subplot(111)
                            ax.plot(df1.columns[7::5],list(map(int,df1.iloc[i,7::5])))
                            canvas = FigureCanvasTkAgg(fig,master=self)
                            canvas.get_tk_widget().pack()
                        elif(var.get()=='음주운전'):
                            fig=plt.figure(figsize=(7,3),dpi=300)
                            ax=plt.plot(df1.columns[5::5],list(map(int,df1.iloc[i,5::5])))
                            #ax=fig.add_subplot(111)
                            #ax.plot(df1.columns[5::5],list(map(int,df1.iloc[i,5::5])))
                            canvas = FigureCanvasTkAgg(fig,master=self)         
                            canvas.get_tk_widget().pack()
                        else:
                            continue
            except:
                df1=pd.read_csv('서울시.csv',encoding='cp949')
                df1=df1.iloc[:,1:]
                index = mylist.curselection()[0]
                info = mylist.get(index)
                for i in range(1,26):
                    if(info == df1.iloc[i,1]):
                        if(var.get()=='신호위반'):   
                            fig=plt.figure(figsize=(7,3),dpi=300)
                            ax=fig.add_subplot(111)
                            ax.plot(df1.columns[4::5],list(map(int,df1.iloc[i,4::5])))
                            #ax.set_title(info+"의 신호위반")
                            canvas = FigureCanvasTkAgg(fig,master=self)
                            canvas.get_tk_widget().pack()
                        elif(var.get()=='무면허'):
                            fig=plt.figure(figsize=(7,3),dpi=300)
                            ax=fig.add_subplot(111)
                            ax.plot(df1.columns[3::5],list(map(int,df1.iloc[i,3::5])))
                            canvas = FigureCanvasTkAgg(fig,master=self)
                            canvas.get_tk_widget().pack()
                        elif(var.get()=='스쿨존'):
                            fig=plt.figure(figsize=(7,3),dpi=300)
                            ax=fig.add_subplot(111)
                            ax.plot(df1.columns[6::5],list(map(int,df1.iloc[i,6::5])))
                            canvas = FigureCanvasTkAgg(fig,master=self)
                            canvas.draw()
                            canvas.get_tk_widget().pack()
                        elif(var.get()=='과속'):
                            fig=plt.figure(figsize=(7,3),dpi=300)
                            ax=fig.add_subplot(111)
                            ax.plot(df1.columns[7::5],list(map(int,df1.iloc[i,7::5])))
                            canvas = FigureCanvasTkAgg(fig,master=self)
                            canvas.get_tk_widget().pack()
                        elif(var.get()=='신호위반'):
                            fig=plt.figure(figsize=(7,3),dpi=300)
                            ax=plt.plot(df1.columns[5::5],list(map(int,df1.iloc[i,5::5])))
                            #ax=fig.add_subplot(111)
                            #ax.plot(df1.columns[5::5],list(map(int,df1.iloc[i,5::5])))
                            canvas = FigureCanvasTkAgg(fig,master=self)         
                            canvas.get_tk_widget().pack()
                        else:
                            continue


        bt=Button(frame1,text="사고 유형 분석",command=graph,width=40,height=3,background='white',font=20)
        bt.pack(side=LEFT,expand=True,fill=BOTH)
        bt2=Button(frame1,text="사고 유형 상세 분석" ,width=40,height=3,background='white',font=20)
        bt2.pack(side=LEFT,expand=True,fill=BOTH)
        bt3=Button(frame1,text="유형별 최다 사고",width=40,height=3,background='white',font=20)
        bt3.pack(side=LEFT,expand=True,fill=BOTH)


        # 레이블 생성
        label = tk.Label()
        label.pack()

        def show_info(event):
            # 선택된 항목의 인덱스와 정보를 레이블에 표시
            index = mylist.curselection()[0]
            info = mylist.get(index)
            label.config(text=f"선택한 지역: {info}")

        # 리스트박스에 콜백 함수 연결
        mylist.bind("<<ListboxSelect>>", show_info)

        #window.mainloop()

if __name__ == "__main__":
    app = Accident()
    app.mainloop()