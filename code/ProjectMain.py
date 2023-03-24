from tkinter import *
import tkinter as tk # 인터페이스를 만들 때
import csv # csv 파일을 불러올 때 사용합니다
import os 
from PIL import Image, ImageTk
import pandas as pd # 데이터 프레임을 만들 수 있는 모듈
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

PATH = os.path.dirname(os.path.realpath(__file__))
os.chdir(PATH)


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

    def del_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def double_check_graph(self,mylist,var):
        try:
                global canvas
                canvas.get_tk_widget().pack_forget()
                df1=pd.read_csv('1번.csv',encoding='cp949')
                index = mylist.curselection()[0]
                info = mylist.get(index)
                year_list=['2017','2018','2019','2020','2021']
                for i in range(1,26):
                    if(info == df1.loc[i][2]):
                        if(var=='무면허'):
                            title_name=df1.loc[i][2]
                            fig=plt.figure()
                            plt.rc('font', family='Malgun Gothic')
                            plt.bar(range(3,16,3), df1.loc[i][range(3,16,3)], label=var, color='skyblue')
                            plt.xticks(range(2,16,3),year_list)
                            plt.title(title_name+' 사고 유형 연도별 분석')
                            canvas = FigureCanvasTkAgg(fig,master=self)         
                            canvas.get_tk_widget().pack(side=LEFT)
                        elif(var=='스쿨존사고'):
                            title_name=df1.loc[i][2]
                            fig=plt.figure()
                            plt.rc('font', family='Malgun Gothic')
                            plt.bar(range(2,16,3), df1.loc[i][range(2,16,3)], label=var, color='royalblue')
                            plt.xticks(range(2,16,3),year_list)
                            plt.title(title_name+' 사고 유형 연도별 분석')
                            canvas = FigureCanvasTkAgg(fig,master=self)         
                            canvas.get_tk_widget().pack(side=LEFT)
                        else:
                            title_name=df1.loc[i][2]
                            fig=plt.figure()
                            plt.rc('font', family='Malgun Gothic')
                            plt.bar(range(1,16,3),df1.loc[i][range(1,16,3)] , label=var, color='grey') 
                            plt.xticks(range(2,16,3),year_list)
                            plt.title(title_name+' 사고 유형 연도별 분석')
                            canvas = FigureCanvasTkAgg(fig,master=self)         
                            canvas.get_tk_widget().pack(side=LEFT)
                    else:
                        continue
        except:
            df1=pd.read_csv('1번.csv',encoding='cp949')
            index = mylist.curselection()[0]
            info = mylist.get(index)
            year_list=['2017','2018','2019','2020','2021']
            for i in range(1,26):
                if(info == df1.loc[i][2]):
                    title_name=df1.loc[i][2]
                    fig=plt.figure()
                    plt.rc('font', family='Malgun Gothic')
                    plt.bar(range(1,16,3),df1.loc[i][range(1,16,3)] , label='음주운전', color='grey') 
                    plt.bar(range(2,16,3), df1.loc[i][range(2,16,3)], label='스쿨존 사고', color='royalblue')
                    plt.bar(range(3,16,3), df1.loc[i][range(3,16,3)], label='무면허', color='skyblue')
                    plt.xticks(range(2,16,3),year_list)
                    plt.title(title_name+' 사고 유형 연도별 분석')
                    canvas = FigureCanvasTkAgg(fig,master=self)         
                    canvas.get_tk_widget().pack(side=LEFT)
                else:
                    continue
    def graph(self,mylist):
            try:
                global canvas
                canvas.get_tk_widget().pack_forget()
                df1=pd.read_csv('1번.csv',encoding='cp949')
                index = mylist.curselection()[0]
                info = mylist.get(index)
                year_list=['2017','2018','2019','2020','2021']
                for i in range(1,26):
                    if(info == df1.loc[i][2]):
                        title_name=df1.loc[i][2]
                        fig=plt.figure()
                        plt.rc('font', family='Malgun Gothic')
                        plt.bar(range(1,16,3),df1.loc[i][range(1,16,3)] , label='음주운전', color='grey') 
                        plt.bar(range(2,16,3), df1.loc[i][range(2,16,3)], label='스쿨존 사고', color='royalblue')
                        plt.bar(range(3,16,3), df1.loc[i][range(3,16,3)], label='무면허', color='skyblue')
                        plt.xticks(range(2,16,3),year_list)
                        plt.legend()
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack(side=LEFT)
                        
                        
                    else:
                        continue
            except:
                df1=pd.read_csv('1번.csv',encoding='cp949')
                index = mylist.curselection()[0]
                info = mylist.get(index)
                year_list=['2017','2018','2019','2020','2021']
                for i in range(1,26):
                    if(info == df1.loc[i][2]):
                        title_name=df1.loc[i][2]
                        fig=plt.figure()
                        plt.rc('font', family='Malgun Gothic')
                        plt.bar(range(1,16,3),df1.loc[i][range(1,16,3)] , label='음주운전', color='grey') 
                        plt.bar(range(2,16,3), df1.loc[i][range(2,16,3)], label='스쿨존 사고', color='royalblue')
                        plt.bar(range(3,16,3), df1.loc[i][range(3,16,3)], label='무면허', color='skyblue')
                        plt.xticks(range(2,16,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack(side=LEFT)
                    else:
                        continue
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
        frame1=tk.Frame()
        frame1.pack(fill='both')
        bt=Button(frame1,text="사고 유형 분석",width=40,height=3,background='white',font=20,command=lambda: [master.del_frame(),master.switch_frame(Menu1)])
        bt.pack(side=LEFT,expand=True,fill=BOTH)
        bt2=Button(frame1,text="사고 유형 상세 분석" ,width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu2)])
        bt2.pack(side=LEFT,expand=True,fill=BOTH)
        bt3=Button(frame1,text="유형별 최다 사고",width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu3)])
        bt3.pack(side=LEFT,expand=True,fill=BOTH)
    
        
# 사고 유형 분석 메뉴
class Menu1(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        # 콜백 함수 정의
        # frame=tk.Frame(self)
        # frame.pack()
        frame1=tk.Frame()
        frame1.pack(fill='both')
        frame2=tk.Frame()
        frame2.pack(side=LEFT,anchor='n',fill='both')
        frame3=tk.Frame()
        frame3.pack(side=BOTTOM)

        scrollbar = Scrollbar(frame2) # 스크롤바 생성
        scrollbar.pack(side=RIGHT, fill=Y) # 스크롤바를 프레임의 오른쪽에 붙임
        mylist = Listbox(frame2, yscrollcommand=scrollbar.set, height=0, selectbackground='pink', selectforeground='black',font=20) # 리스트바 생성, 스크롤바 연결, 높이 0으로 설정
        df1=pd.read_csv('1번.csv',encoding='cp949')
        for i in range(1,26):
            mylist.insert(tk.END, df1.loc[i][2])
        mylist.pack(side=LEFT,anchor='n',fill=BOTH,expand=True) # 리스트바를 프레임의 왼쪽에 붙임
        scrollbar.config(command=mylist.yview)
        
        bt=Button(frame1,text="사고 유형 분석",width=40,height=3,background='white',font=20,command=lambda: [master.del_frame(),master.switch_frame(Menu1)])
        bt.pack(side=LEFT,expand=True,fill=BOTH)
        bt2=Button(frame1,text="사고 유형 상세 분석" ,width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu2)])
        bt2.pack(side=LEFT,expand=True,fill=BOTH)
        bt3=Button(frame1,text="유형별 최다 사고",width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu3)])
        bt3.pack(side=LEFT,expand=True,fill=BOTH)
        bt3=Button(frame3,text="그래프 보기",width=40,height=3,background='white',font=20,command=lambda: master.graph(mylist))
        bt3.pack(side=TOP,expand=True,fill=BOTH)

class Menu2(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        frame1=tk.Frame()
        frame1.pack(fill='both')
        frame2=tk.Frame()
        frame2.pack(side=LEFT,anchor='n')
        frame3=tk.Frame()
        frame3.pack(side=BOTTOM)
        frame4=tk.Frame()
        frame4.pack(side=RIGHT)

        var=StringVar()
        var.set(NONE)

        scrollbar = Scrollbar(frame2) # 스크롤바 생성
        scrollbar.pack(side=RIGHT, fill=Y) # 스크롤바를 프레임의 오른쪽에 붙임

        mylist = Listbox(frame2, yscrollcommand=scrollbar.set, height=0, selectbackground='pink', selectforeground='black',font=20) # 리스트바 생성, 스크롤바 연결, 높이 0으로 설정
        df1=pd.read_csv('1번.csv',encoding='cp949')
        for i in range(1,26):
            mylist.insert(tk.END, df1.loc[i][2])
        
            
        mylist.pack(side=LEFT,anchor='n',fill=BOTH) # 리스트바를 프레임의 왼쪽에 붙임
        scrollbar.config(command=mylist.yview)
        
        R1 = Radiobutton(frame4, text='음주운전',variable=var, value="음주운전",font=20) # 오른쪽 프레임 체크박스 추가
        R1.pack(anchor='w') # 왼쪽으로 정렬
        R2 = Radiobutton(frame4, text='무면허',variable=var, value="무면허",font=20)
        R2.pack(anchor='w')
        R3 = Radiobutton(frame4, text='스쿨존',variable=var, value="스쿨존",font=20)
        R3.pack(anchor='w')
        
        bt=Button(frame1,text="사고 유형 분석",width=40,height=3,background='white',font=20,command=lambda: [master.del_frame(),master.switch_frame(Menu1)])
        bt.pack(side=LEFT,expand=True,fill=BOTH)
        bt1=Button(frame1,text="사고 유형 상세 분석" ,width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu2)])
        bt1.pack(side=LEFT,expand=True,fill=BOTH)
        bt2=Button(frame1,text="유형별 최다 사고",width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu3)])
        bt2.pack(side=LEFT,expand=True,fill=BOTH)
        bt3=Button(frame3,text="그래프 보기",width=40,height=3,background='white',font=20,command=lambda: master.double_check_graph(mylist,var))
        bt3.pack(side=TOP,expand=True,fill=BOTH)
            
class Menu3(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        frame1=tk.Frame()
        frame1.pack(fill='both')
        frame4=tk.Frame()
        frame4.pack(side=RIGHT)
        var=StringVar()
        var.set(NONE)
        # def selection():  
        #     label.config(text="선택한 옵션: " + var.get())

        
        R1 = Radiobutton(frame4, text='음주운전',variable=var, value="음주운전",font=20) # 오른쪽 프레임 체크박스 추가
        R1.pack(anchor='w') # 왼쪽으로 정렬
        R2 = Radiobutton(frame4, text='무면허',variable=var, value="무면허",font=20)
        R2.pack(anchor='w')
        R3 = Radiobutton(frame4, text='스쿨존',variable=var, value="스쿨존",font=20)
        R3.pack(anchor='w')
        R4 = Radiobutton(frame4, text='과속',variable=var, value="과속",font=20)
        R4.pack(anchor='w')
        R5 = Radiobutton(frame4, text='신호위반',variable=var, value="신호위반",font=20)
        R5.pack(anchor='w')
        
        
        bt=Button(frame1,text="사고 유형 분석",width=40,height=3,background='white',font=20,command=lambda: [master.del_frame(),master.switch_frame(Menu1)])
        bt.pack(side=LEFT,expand=True,fill=BOTH)
        bt2=Button(frame1,text="사고 유형 상세 분석" ,width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu2)])
        bt2.pack(side=LEFT,expand=True,fill=BOTH)
        bt3=Button(frame1,text="유형별 최다 사고",width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu3)])
        bt3.pack(side=LEFT,expand=True,fill=BOTH)

if __name__ == "__main__":
    app = Accident()
    app.mainloop()