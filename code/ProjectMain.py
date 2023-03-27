from tkinter import *
import tkinter as tk # 인터페이스를 만들 때
import os 
from PIL import Image, ImageTk
import pandas as pd # 데이터 프레임을 만들 수 있는 모듈
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
import sys
#import time

PATH = os.path.dirname(os.path.realpath(__file__))
os.chdir(PATH)

class Accident(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartMenu)
        self.title("서울시 사고유형 분석") # ui 제목
        self.geometry("1200x700") # ui 시작 해상도
        photo = ImageTk.PhotoImage(Image.open('car.png')) # ui 아이콘 불러오기
        self.wm_iconphoto(False, photo) # ui 아이콘 적용하기

        # 메뉴 바
        menubar = Menu(self)
        menu=Menu(menubar, tearoff=0)
        menu.add_command(label="사용 설명서") # 하위 메뉴
        menu.add_command(label="종료",command=sys.exit)
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
    def graph_time(self,mylist,var):
        try:
            global canvas
            canvas.get_tk_widget().pack_forget()
            df1=pd.read_csv('1번.csv',encoding='cp949')
            index = mylist.curselection()[0]
            info = mylist.get(index)
            year_list=['2017','2018','2019','2020','2021']
            for i in range(1,26):
                if(info == df1.loc[i][2]):
                    if(var=='음주운전'):
                        title_name=df1.loc[i][2]
                        fig=plt.figure()
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(4,19,3),list(map(int,df1.iloc[i,4::3])),color='grey',label='음주운전')
                        plt.yticks(range(4,19,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    elif(var=='스쿨존'):
                        title_name=df1.loc[i][2]
                        fig=plt.figure()
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(5,19,3),list(map(int,df1.iloc[i,5::3])),color='royalblue',label='스쿨존 사고')
                        plt.yticks(range(5,19,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    elif(var=='무면허'):
                        title_name=df1.loc[i][2]
                        fig=plt.figure()
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(6,19,3),list(map(int,df1.iloc[i,6::3])),color='violet',label='무면허')
                        plt.yticks(range(6,19,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    else:
                        continue
                else:
                    continue
        except:
            df1=pd.read_csv('1번.csv',encoding='cp949')
            index = mylist.curselection()[0]
            info = mylist.get(index)
            year_list=['2017','2018','2019','2020','2021']
            for i in range(1,26):
                if(info == df1.loc[i][2]):
                    if(var=='음주운전'):
                        title_name=df1.loc[i][2]
                        fig=plt.figure()
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(4,19,3),list(map(int,df1.iloc[i,4::3])),color='grey',label='음주운전')
                        plt.yticks(range(2,16,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    elif(var=='스쿨존'):
                        title_name=df1.loc[i][2]
                        fig=plt.figure()
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(5,19,3),list(map(int,df1.iloc[i,5::3])),color='royalblue',label='스쿨존 사고')
                        #plt.bar(range(2,16,3), df1.loc[i][range(2,16,3)], label=var, color='royalblue')
                        plt.yticks(range(2,16,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    elif(var=='무면허'):
                        title_name=df1.loc[i][2]
                        fig=plt.figure()
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(6,19,3),list(map(int,df1.iloc[i,6::3])),color='violet',label='무면허')
                        #plt.bar(range(1,16,3),df1.loc[i][range(1,16,3)] , label=var, color='grey') 
                        plt.yticks(range(2,16,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    else:
                        continue
                else:
                    continue
    def graph_year(self,mylist,var):
        try:
            global canvas
            canvas.get_tk_widget().pack_forget()
            df1=pd.read_csv('1번.csv',encoding='cp949')
            index = mylist.curselection()[0]
            info = mylist.get(index)
            year_list=['2017','2018','2019','2020','2021']
            for i in range(1,26):
                if(info == df1.loc[i][2]):
                    if(var=='음주운전'):
                        title_name=df1.loc[i][2]
                        fig=plt.figure()
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(4,19,3),list(map(int,df1.iloc[i,4::3])),color='grey',label='음주운전')
                        plt.yticks(range(4,19,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    elif(var=='스쿨존'):
                        title_name=df1.loc[i][2]
                        fig=plt.figure()
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(5,19,3),list(map(int,df1.iloc[i,5::3])),color='royalblue',label='스쿨존 사고')
                        plt.yticks(range(5,19,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    elif(var=='무면허'):
                        title_name=df1.loc[i][2]
                        fig=plt.figure()
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(6,19,3),list(map(int,df1.iloc[i,6::3])),color='violet',label='무면허')
                        plt.yticks(range(6,19,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    else:
                        continue
                else:
                    continue
        except:
            df1=pd.read_csv('1번.csv',encoding='cp949')
            index = mylist.curselection()[0]
            info = mylist.get(index)
            year_list=['2017','2018','2019','2020','2021']
            for i in range(1,26):
                if(info == df1.loc[i][2]):
                    if(var=='음주운전'):
                        title_name=df1.loc[i][2]
                        fig=plt.figure()
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(4,19,3),list(map(int,df1.iloc[i,4::3])),color='grey',label='음주운전')
                        plt.yticks(range(2,16,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    elif(var=='스쿨존'):
                        title_name=df1.loc[i][2]
                        fig=plt.figure()
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(5,19,3),list(map(int,df1.iloc[i,5::3])),color='royalblue',label='스쿨존 사고')
                        plt.yticks(range(2,16,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    elif(var=='무면허'):
                        title_name=df1.loc[i][2]
                        fig=plt.figure()
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(6,19,3),list(map(int,df1.iloc[i,6::3])),color='violet',label='무면허')
                        plt.yticks(range(2,16,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    else:
                        continue
                else:
                    continue
    
    def save_image(self,mylist):
        # 이미지 저장 대화상자 띄우기
        file_path = filedialog.asksaveasfilename(defaultextension='.png')

        # 이미지 저장하기
        if file_path:
            df1=pd.read_csv('1번.csv',encoding='cp949')
            index = mylist.curselection()[0]
            info = mylist.get(index)
            year_list=['2017','2018','2019','2020','2021']
            for i in range(1,26):
                if(info == df1.loc[i][2]):
                    title_name=df1.loc[i][2]
                    fig=plt.figure()
                    plt.rc('font', family='Malgun Gothic')
                    plt.bar(range(4,19,3),list(map(int,df1.iloc[i,4::3])),color='grey',label='음주운전')
                    plt.bar(range(5,19,3),list(map(int,df1.iloc[i,5::3])),color='royalblue',label='스쿨존 사고')
                    plt.bar(range(6,19,3),list(map(int,df1.iloc[i,6::3])),color='skyblue',label='무면허')
                    plt.xticks(range(5,19,3),year_list)
                    plt.legend()
                    plt.title(title_name+' 사고 유형 연도별 분석')
                    plt.savefig(file_path)

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
        frame1=tk.Frame()
        frame1.pack(fill='both')
        frame2=tk.Frame()
        frame2.pack(side=LEFT,anchor='n',fill='both')
        frame3=tk.Frame()
        frame3.pack(side=BOTTOM)
        frame4=tk.Frame()
        frame4.pack(side=RIGHT)
        self.text=tk.StringVar()
        self.text.set('')
        scrollbar = Scrollbar(frame2) # 스크롤바 생성
        scrollbar.pack(side=RIGHT, fill=Y) # 스크롤바를 프레임의 오른쪽에 붙임
        mylist = Listbox(frame2, yscrollcommand=scrollbar.set, height=0, selectbackground='pink', selectforeground='black',font=20) # 리스트바 생성, 스크롤바 연결, 높이 0으로 설정
        df1=pd.read_csv('1번.csv',encoding='cp949')
        for i in range(1,26):
            mylist.insert(tk.END, df1.loc[i][2])
        mylist.pack(side=LEFT,anchor='n',fill=BOTH,expand=True) # 리스트바를 프레임의 왼쪽에 붙임
        scrollbar.config(command=mylist.yview)
        bt=Button(frame1,text="사고 유형 분석",width=40,height=3,background='grey',font=20)
        bt.pack(side=LEFT,expand=True,fill=BOTH)
        bt2=Button(frame1,text="사고 유형 상세 분석" ,width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu2)])
        bt2.pack(side=LEFT,expand=True,fill=BOTH)
        bt3=Button(frame1,text="유형별 최다 사고",width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu3)])
        bt3.pack(side=LEFT,expand=True,fill=BOTH)
        bt4=Button(frame3,text="그래프 저장",width=40,height=3,background='white',font=20,command=lambda: [master.save_image(mylist)])
        bt4.pack(side=LEFT,expand=True,fill=BOTH)
        tk.Label(frame4,textvariable=self.text,font=('Helvetica', 10, "bold")).pack(side=RIGHT,padx=10)
        mylist.bind("<<ListboxSelect>>", lambda event : [self.graph(mylist,event),self.show_info(mylist)])

    def graph(self,mylist,event):
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
                    plt.bar(range(4,19,3),list(map(int,df1.iloc[i,4::3])),color='grey',label='음주운전')
                    plt.bar(range(5,19,3),list(map(int,df1.iloc[i,5::3])),color='royalblue',label='스쿨존 사고')
                    plt.bar(range(6,19,3),list(map(int,df1.iloc[i,6::3])),color='skyblue',label='무면허')
                    plt.xticks(range(5,19,3),year_list)
                    plt.legend()
                    plt.title(title_name+' 사고 유형 연도별 분석')
                    canvas = FigureCanvasTkAgg(fig,master=self)         
                    canvas.get_tk_widget().pack()
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
                    plt.bar(range(4,19,3),list(map(int,df1.iloc[i,4::3])),color='grey',label='음주운전')
                    plt.bar(range(5,19,3),list(map(int,df1.iloc[i,5::3])),color='royalblue',label='스쿨존 사고')
                    plt.bar(range(6,19,3),list(map(int,df1.iloc[i,6::3])),color='skyblue',label='무면허')
                    plt.xticks(range(5,19,3),year_list)

                    plt.legend()
                    plt.title(title_name+' 사고 유형 연도별 분석')
                    canvas = FigureCanvasTkAgg(fig,master=self)         
                    canvas.get_tk_widget().pack()
                else:
                    continue
    
    def show_info(self,mylist):
        df=pd.read_csv('1번.csv',encoding='cp949')
        df1=df.iloc[1:,4:].astype(int)
        result1=df1.iloc[:,0::3].sum(axis=1)
        result2=df1.iloc[:,1::3].sum(axis=1)
        result3=df1.iloc[:,2::3].sum(axis=1)
        index = mylist.curselection()[0]
        info = mylist.get(index)
        result1=result1.rank(ascending=False).astype(int)
        result2=result2.rank(ascending=False).astype(int)
        result3=result3.rank(ascending=False).astype(int)
        for i in range(1,26):
            if(info == df.loc[i][2]):
                self.text.set(df.loc[i][2]+'의 음주운전 사고 순위 : '+result1[i].astype(str)+'위'+'\n'
                             +df.loc[i][2]+'의 스쿨존 사고 순위 : '+result2[i].astype(str)+'위'+'\n'
                             +df.loc[i][2]+'의 무면허 사고 순위 : '+result3[i].astype(str)+'위')

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
        R2 = Radiobutton(frame4 ,text='무면허',variable=var, value="무면허",font=20)
        R2.pack(anchor='w')
        R3 = Radiobutton(frame4, text='스쿨존',variable=var, value="스쿨존",font=20)
        R3.pack(anchor='w')
        
        bt=Button(frame1,text="사고 유형 분석",width=40,height=3,background='white',font=20,command=lambda: [master.del_frame(),master.switch_frame(Menu1)])
        bt.pack(side=LEFT,expand=True,fill=BOTH)
        bt1=Button(frame1,text="사고 유형 상세 분석" ,width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu2)])
        bt1.pack(side=LEFT,expand=True,fill=BOTH)
        bt2=Button(frame1,text="유형별 최다 사고",width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu3)])
        bt2.pack(side=LEFT,expand=True,fill=BOTH)
        bt3=Button(frame4,text="연도별",width=40,height=3,background='white',font=20,command=lambda: master.graph_year(mylist,var.get()))
        bt3.pack(side=TOP,fill=BOTH)
        bt3=Button(frame4,text="시간대별",width=40,height=3,background='white',font=20,command=lambda: master.graph_time(mylist,var.get()))
        bt3.pack(side=TOP,fill=BOTH)

            
class Menu3(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)

        frame1=tk.Frame()
        frame1.pack(fill='both')
        frame2=tk.Frame()
        frame2.pack(side=RIGHT)
        var=StringVar()
        var.set(NONE)

        
        R1 = Radiobutton(frame2, text='음주운전',variable=var, value="음주운전",font=20) # 오른쪽 프레임 체크박스 추가
        R1.pack(anchor='w') # 왼쪽으로 정렬
        R2 = Radiobutton(frame2, text='무면허',variable=var, value="무면허",font=20)
        R2.pack(anchor='w')
        R3 = Radiobutton(frame2, text='스쿨존',variable=var, value="스쿨존",font=20)
        R3.pack(anchor='w')
        
        
        bt=Button(frame1,text="사고 유형 분석",width=40,height=3,background='white',font=20,command=lambda: [master.del_frame(),master.switch_frame(Menu1)])
        bt.pack(side=LEFT,expand=True,fill=BOTH)
        bt2=Button(frame1,text="사고 유형 상세 분석" ,width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu2)])
        bt2.pack(side=LEFT,expand=True,fill=BOTH)
        bt3=Button(frame1,text="유형별 최다 사고",width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu3)])
        bt3.pack(side=LEFT,expand=True,fill=BOTH)

if __name__ == "__main__":
    app = Accident()
    app.mainloop()