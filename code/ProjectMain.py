from tkinter import *
import tkinter as tk # 인터페이스를 만들 때
import os # 운영체제와 상호 작용을 하기 위한 모듈
from PIL import Image, ImageTk # 파이썬으로 이미지를 다룰 수 있게 해주는 모듈
import pandas as pd # 데이터 프레임을 만들 수 있는 모듈
import matplotlib.pyplot as plt # 그래프 그려주는 모듈
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Tkinter 모듈과 matplotlib 모듈을 이어주는 모듈
from tkinter import filedialog # 파일 저장 창을 만들어 주는 모듈
import sys # 파이썬의 인터프리터를 제어할 수 있는 모듈
#import time

PATH = os.path.dirname(os.path.realpath(__file__)) # 현재 디렉토리로 이동
os.chdir(PATH)

# Ui 정의
class Accident(tk.Tk): 
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None # 현재 프레임을 None으로 초기화
        self.switch_frame(StartMenu) # StartMeun라는 프레임으로 전환
        self.title("서울시 사고유형 분석") # ui 제목
        self.geometry("1200x700") # ui 시작 해상도
        photo = ImageTk.PhotoImage(Image.open('car.png')) # ui 아이콘 불러오기
        self.wm_iconphoto(False, photo) # ui 아이콘 적용하기

        # 메뉴 바
        menubar = Menu(self)
        menu=Menu(menubar, tearoff=0) # 메뉴바 추가(tearoff = 메뉴바를 새 창으로 분리 할 수 있는가(1=예, 2 아니오))
        menu.add_command(label="사용 설명서") # 하위 메뉴에 사용 설명서 추가
        menu.add_command(label="종료",command=sys.exit)  #하위 메뉴에 종료 추가
        menubar.add_cascade(label="도움말", menu=menu) # 상단 메뉴바 이름
        self.config(menu=menubar) # 메뉴바를 ui에 보이도록

    # 프레임 이동 함수
    def switch_frame(self, frame_class): 
        new_frame = frame_class(self)
        if self._frame is not None: # 프레임이 비어 있지 않을 때
            self._frame.destroy() # 프레임을 비움
        self._frame = new_frame
        self._frame.pack() # pack 메소드는 프레임의 크기와 위치를 자동으로 조절하여 윈도우에 적절하게 맞춤

    # 프레임을 지우는 함수
    def del_frame(self):
        for widget in self.winfo_children(): # 윈도우의 모든 자식 위젯을 지움
            widget.destroy()
    
    # 데이터를 분석 정제하고 그래프를 출력하는 함수
    def graph_time(self,mylist,var):
        try:
            global canvas
            canvas.get_tk_widget().pack_forget()
            TrafficAccident=pd.read_csv('1번.csv',encoding='cp949') #csv 파일을 cp949로 인코딩 후 파일을 불러오는 함수 
            index = mylist.curselection()[0] # 리스트박스의 선택된 항목의 인덱스를 반환하는 메소드
            info = mylist.get(index) # 인덱스에 해당하는 항목의 값을 반환하는 메소드
            year_list=['2017','2018','2019','2020','2021'] #그래프 x축에 표시할 연도
            for i in range(1,26): # csv파일의 25행까지
                if(info == TrafficAccident.loc[i][2]): # 리스트박스에서 선택한 항목이 csv파일의 해당 자치구 일때
                    if(var=='음주운전'):
                        title_name=TrafficAccident.loc[i][2] #타이틀의 이름을 리스트박스에서 선택한 항목으로 지정
                        fig=plt.figure() #그래프를 그릴 figure 객체 생성
                        plt.rc('font', family='Malgun Gothic') # 폰트가 깨지는 걸 방지 
                        plt.barh(range(4,19,3),list(map(int,TrafficAccident.iloc[i,4::3])),color='grey',label='음주운전') # 그래프의(범위,표시할 범위,색깔,소제목)
                        plt.yticks(range(4,19,3),year_list) # 그래프의 y축에 표시할 데이터 값
                        plt.title(title_name+' 사고 유형 연도별 분석') # 그래프의 제목
                        canvas = FigureCanvasTkAgg(fig,master=self) # 그래프를 tkinter ui에 표시
                        canvas.get_tk_widget().pack() # pack 메소드는 프레임의 크기와 위치를 자동으로 조절하여 윈도우에 적절하게 맞춤
                    elif(var=='스쿨존'):
                        title_name=TrafficAccident.loc[i][2] #타이틀의 이름을 리스트박스에서 선택한 항목으로 지정
                        fig=plt.figure() #그래프를 그릴 figure 객체 생성
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(5,19,3),list(map(int,TrafficAccident.iloc[i,5::3])),color='royalblue',label='스쿨존 사고')
                        plt.yticks(range(5,19,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    elif(var=='무면허'):
                        title_name=TrafficAccident.loc[i][2] #타이틀의 이름을 리스트박스에서 선택한 항목으로 지정
                        fig=plt.figure() #그래프를 그릴 figure 객체 생성
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(6,19,3),list(map(int,TrafficAccident.iloc[i,6::3])),color='violet',label='무면허')
                        plt.yticks(range(6,19,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)
                        canvas.get_tk_widget().pack()
                    else:
                        continue
                else:
                    continue
        except:
            TrafficAccident=pd.read_csv('1번.csv',encoding='cp949') #csv 파일을 cp949로 인코딩 후 파일을 불러오는 함수
            index = mylist.curselection()[0] # 리스트박스의 선택된 항목의 인덱스를 반환하는 메소드
            info = mylist.get(index) # 인덱스에 해당하는 항목의 값을 반환하는 메소드
            year_list=['2017','2018','2019','2020','2021'] #그래프 x축에 표시할 연도 
            for i in range(1,26):
                if(info == TrafficAccident.loc[i][2]):
                    if(var=='음주운전'):
                        title_name=TrafficAccident.loc[i][2] #타이틀의 이름을 리스트박스에서 선택한 항목으로 지정
                        fig=plt.figure() #그래프를 그릴 figure 객체 생성
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(4,19,3),list(map(int,TrafficAccident.iloc[i,4::3])),color='grey',label='음주운전')
                        plt.yticks(range(2,16,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    elif(var=='스쿨존'):
                        title_name=TrafficAccident.loc[i][2] #타이틀의 이름을 리스트박스에서 선택한 항목으로 지정
                        fig=plt.figure() #그래프를 그릴 figure 객체 생성
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(5,19,3),list(map(int,TrafficAccident.iloc[i,5::3])),color='royalblue',label='스쿨존 사고')
                        plt.yticks(range(2,16,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    elif(var=='무면허'):
                        title_name=TrafficAccident.loc[i][2] #타이틀의 이름을 리스트박스에서 선택한 항목으로 지정
                        fig=plt.figure() #그래프를 그릴 figure 객체 생성
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(6,19,3),list(map(int,TrafficAccident.iloc[i,6::3])),color='violet',label='무면허')
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
            canvas.get_tk_widget().pack_forget() # ui에 그려져 있는 그래프를 지움
            TrafficAccident=pd.read_csv('1번.csv',encoding='cp949') #csv 파일을 cp949로 인코딩 후 파일을 불러오는 함수
            index = mylist.curselection()[0] # 리스트박스의 선택된 항목의 인덱스를 반환하는 메소드
            info = mylist.get(index) # 인덱스에 해당하는 항목의 값을 반환하는 메소드
            year_list=['2017','2018','2019','2020','2021'] #그래프 x축에 표시할 연도
            for i in range(1,26):
                if(info == TrafficAccident.loc[i][2]):
                    if(var=='음주운전'):
                        title_name=TrafficAccident.loc[i][2] #타이틀의 이름을 리스트박스에서 선택한 항목으로 지정
                        fig=plt.figure() #그래프를 그릴 figure 객체 생성
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(4,19,3),list(map(int,TrafficAccident.iloc[i,4::3])),color='grey',label='음주운전')
                        plt.yticks(range(4,19,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    elif(var=='스쿨존'):
                        title_name=TrafficAccident.loc[i][2] #타이틀의 이름을 리스트박스에서 선택한 항목으로 지정
                        fig=plt.figure() #그래프를 그릴 figure 객체 생성
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(5,19,3),list(map(int,TrafficAccident.iloc[i,5::3])),color='royalblue',label='스쿨존 사고')
                        plt.yticks(range(5,19,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    elif(var=='무면허'):
                        title_name=TrafficAccident.loc[i][2] #타이틀의 이름을 리스트박스에서 선택한 항목으로 지정
                        fig=plt.figure() #그래프를 그릴 figure 객체 생성
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(6,19,3),list(map(int,TrafficAccident.iloc[i,6::3])),color='violet',label='무면허')
                        plt.yticks(range(6,19,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    else:
                        continue
                else:
                    continue
        except:
            TrafficAccident=pd.read_csv('1번.csv',encoding='cp949') #csv 파일을 cp949로 인코딩 후 파일을 불러오는 함수
            index = mylist.curselection()[0] # 리스트박스의 선택된 항목의 인덱스를 반환하는 메소드
            info = mylist.get(index) # 인덱스에 해당하는 항목의 값을 반환하는 메소드
            year_list=['2017','2018','2019','2020','2021'] #그래프 x축에 표시할 연도
            for i in range(1,26):
                if(info == TrafficAccident.loc[i][2]):
                    if(var=='음주운전'):
                        title_name=TrafficAccident.loc[i][2] #타이틀의 이름을 리스트박스에서 선택한 항목으로 지정
                        fig=plt.figure() #그래프를 그릴 figure 객체 생성
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(4,19,3),list(map(int,TrafficAccident.iloc[i,4::3])),color='grey',label='음주운전')
                        plt.yticks(range(2,16,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    elif(var=='스쿨존'):
                        title_name=TrafficAccident.loc[i][2] #타이틀의 이름을 리스트박스에서 선택한 항목으로 지정
                        fig=plt.figure() #그래프를 그릴 figure 객체 생성
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(5,19,3),list(map(int,TrafficAccident.iloc[i,5::3])),color='royalblue',label='스쿨존 사고')
                        plt.yticks(range(2,16,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    elif(var=='무면허'):
                        title_name=TrafficAccident.loc[i][2] #타이틀의 이름을 리스트박스에서 선택한 항목으로 지정
                        fig=plt.figure() #그래프를 그릴 figure 객체 생성
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(6,19,3),list(map(int,TrafficAccident.iloc[i,6::3])),color='violet',label='무면허')
                        plt.yticks(range(2,16,3),year_list)
                        plt.title(title_name+' 사고 유형 연도별 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    else:
                        continue
                else:
                    continue
    # 이미지를 저장하는 함수
    def save_image(self,mylist):
        # 이미지 저장 대화상자 띄우기
        file_path = filedialog.asksaveasfilename(defaultextension='.png') # 파일을 저장할 경로를 선택할 수 있는 창을 띄워주는 함수

        # 이미지 저장하기
        if file_path:
            TrafficAccident=pd.read_csv('1번.csv',encoding='cp949') #csv 파일을 cp949로 인코딩 후 파일을 불러오는 함수 
            index = mylist.curselection()[0] # 리스트박스의 선택된 항목의 인덱스를 반환하는 메소드
            info = mylist.get(index) # 인덱스에 해당하는 항목의 값을 반환하는 메소드
            year_list=['2017','2018','2019','2020','2021'] #그래프 x축에 표시할 연도
            for i in range(1,26):
                if(info == TrafficAccident.loc[i][2]):
                    title_name=TrafficAccident.loc[i][2] #타이틀의 이름을 리스트박스에서 선택한 항목으로 지정
                    fig=plt.figure() #그래프를 그릴 figure 객체 생성
                    plt.rc('font', family='Malgun Gothic')
                    plt.bar(range(4,19,3),list(map(int,TrafficAccident.iloc[i,4::3])),color='grey',label='음주운전')
                    plt.bar(range(5,19,3),list(map(int,TrafficAccident.iloc[i,5::3])),color='royalblue',label='스쿨존 사고')
                    plt.bar(range(6,19,3),list(map(int,TrafficAccident.iloc[i,6::3])),color='skyblue',label='무면허')
                    plt.xticks(range(5,19,3),year_list)
                    plt.legend() #범례 표시
                    plt.title(title_name+' 사고 유형 연도별 분석')
                    plt.savefig(file_path) # 경로를 지정하는 창을 띄워 원하는 위치에 그래프 이미지를 저장
# 시작메뉴 설정
class StartMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="서울시 교통사고 조사", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5) # 시작 화면 상단 라벨
        self.photo = ImageTk.PhotoImage(Image.open('car.png')) # ui 아이콘 불러오기
        tk.Label(self,image=self.photo).pack() # 이미지 라벨
        tk.Label(self, text="2팀 : 김민수, 이지운, 장기헌, 장윤종, 전장현", font=('Helvetica', 10, "bold")).pack(side="top", fill="x", pady=5) #시작 화면 팀 라벨
        tk.Button(self, text="start",width=20,height=2,command=lambda: master.switch_frame(MainMenu)).pack(side=BOTTOM) # 시작 버튼
# 메인메뉴 설정
class MainMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        frame1=tk.Frame() # 프레임 생성
        frame1.pack(fill='both') # 프레임의 위치 지정
        bt=Button(frame1,text="사고 유형 분석",width=40,height=3,background='white',font=20,command=lambda: [master.del_frame(),master.switch_frame(Menu1)])
        bt.pack(side=LEFT,expand=True,fill=BOTH) # 버튼의 위치를 조정(side는 방향, expand는 확장 여부, fill은 공간 채움 여부)
        bt2=Button(frame1,text="사고 유형 상세 분석" ,width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu2)])
        bt2.pack(side=LEFT,expand=True,fill=BOTH)
        bt3=Button(frame1,text="유형별 최다 사고",width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu3)])
        bt3.pack(side=LEFT,expand=True,fill=BOTH)


# 사고 유형 분석 메뉴
class Menu1(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        frame1=tk.Frame() # 프레임 생성
        frame1.pack(fill='both') # 프레임의 위치 지정
        frame2=tk.Frame()
        frame2.pack(side=LEFT,anchor='n',fill='both') # anchor는 방위 이용해서 위치 지정
        frame3=tk.Frame()
        frame3.pack(side=BOTTOM)
        frame4=tk.Frame()
        frame4.pack(side=RIGHT)
        self.text=tk.StringVar()
        self.text.set('')
        scrollbar = Scrollbar(frame2) # 스크롤바 생성
        scrollbar.pack(side=RIGHT, fill=Y) # 스크롤바를 프레임의 오른쪽에 붙임
        mylist = Listbox(frame2, yscrollcommand=scrollbar.set, height=0, selectbackground='pink', selectforeground='black',font=20) # 리스트바 생성, 스크롤바 연결, 높이 0으로 설정
        TrafficAccident=pd.read_csv('1번.csv',encoding='cp949') #csv 파일을 cp949로 인코딩 후 파일을 불러오는 함수
        for i in range(1,26):
            mylist.insert(tk.END, TrafficAccident.loc[i][2])
        mylist.pack(side=LEFT,anchor='n',fill=BOTH,expand=True) # 리스트바를 프레임의 왼쪽에 붙임
        scrollbar.config(command=mylist.yview) #스크롤바와 리스트 박스를 연결하는 함수
        bt=Button(frame1,text="사고 유형 분석",width=40,height=3,background='grey',font=20)
        bt.pack(side=LEFT,expand=True,fill=BOTH) # 버튼의 위치를 조정(side는 방향, expand는 확장 여부, fill은 공간 채움 여부)
        bt2=Button(frame1,text="사고 유형 상세 분석" ,width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu2)])
        bt2.pack(side=LEFT,expand=True,fill=BOTH)
        bt3=Button(frame1,text="유형별 최다 사고",width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu3)])
        bt3.pack(side=LEFT,expand=True,fill=BOTH)
        tk.Label(frame4,textvariable=self.text,font=('Helvetica', 10, "bold")).pack(side=RIGHT,padx=10)
        mylist.bind("<<ListboxSelect>>", lambda event : [self.graph(mylist,event),self.show_info(mylist)]) # 리스트바에서 값을 선택 할 때 바로 그래프가 출력 되도록 해줌
    # 그래프 생성 함수
    def graph(self,mylist,event):
        try:
            global canvas
            canvas.get_tk_widget().pack_forget()
            TrafficAccident=pd.read_csv('1번.csv',encoding='cp949') #csv 파일을 cp949로 인코딩 후 파일을 불러오는 함수
            index = mylist.curselection()[0] # 리스트박스의 선택된 항목의 인덱스를 반환하는 메소드
            info = mylist.get(index) # 인덱스에 해당하는 항목의 값을 반환하는 메소드
            year_list=['2017','2018','2019','2020','2021'] #그래프 x축에 표시할 연도
            for i in range(1,26):
                if(info == TrafficAccident.loc[i][2]):
                    title_name=TrafficAccident.loc[i][2] #타이틀의 이름을 리스트박스에서 선택한 항목으로 지정
                    fig=plt.figure() #그래프를 그릴 figure 객체 생성
                    plt.rc('font', family='Malgun Gothic')
                    plt.bar(range(4,19,3),list(map(int,TrafficAccident.iloc[i,4::3])),color='grey',label='음주운전')
                    plt.bar(range(5,19,3),list(map(int,TrafficAccident.iloc[i,5::3])),color='royalblue',label='스쿨존 사고')
                    plt.bar(range(6,19,3),list(map(int,TrafficAccident.iloc[i,6::3])),color='skyblue',label='무면허')
                    plt.xticks(range(5,19,3),year_list)
                    plt.legend() #범례 표시
                    plt.title(title_name+' 사고 유형 연도별 분석')
                    canvas = FigureCanvasTkAgg(fig,master=self)         
                    canvas.get_tk_widget().pack()
                else:
                    continue
        except:
            TrafficAccident=pd.read_csv('1번.csv',encoding='cp949') #csv 파일을 cp949로 인코딩 후 파일을 불러오는 함수
            index = mylist.curselection()[0] # 리스트박스의 선택된 항목의 인덱스를 반환하는 메소드
            info = mylist.get(index) # 인덱스에 해당하는 항목의 값을 반환하는 메소드
            year_list=['2017','2018','2019','2020','2021'] #그래프 x축에 표시할 연도
            for i in range(1,26):
                if(info == TrafficAccident.loc[i][2]):
                    title_name=TrafficAccident.loc[i][2] #타이틀의 이름을 리스트박스에서 선택한 항목으로 지정
                    fig=plt.figure() #그래프를 그릴 figure 객체 생성
                    plt.rc('font', family='Malgun Gothic')
                    plt.bar(range(4,19,3),list(map(int,TrafficAccident.iloc[i,4::3])),color='grey',label='음주운전')
                    plt.bar(range(5,19,3),list(map(int,TrafficAccident.iloc[i,5::3])),color='royalblue',label='스쿨존 사고')
                    plt.bar(range(6,19,3),list(map(int,TrafficAccident.iloc[i,6::3])),color='skyblue',label='무면허')
                    plt.xticks(range(5,19,3),year_list)

                    plt.legend() #범례 표시
                    plt.title(title_name+' 사고 유형 연도별 분석')
                    canvas = FigureCanvasTkAgg(fig,master=self)         
                    canvas.get_tk_widget().pack()
                else:
                    continue
    # 자료의 발생 건수를 모두 더하고 순위를 보여주는 함수
    def show_info(self,mylist):
        df=pd.read_csv('1번.csv',encoding='cp949')
        TrafficAccident=df.iloc[1:,4:].astype(int)
        result1=TrafficAccident.iloc[:,0::3].sum(axis=1) # csv파일에서 음주운전의 값을 모두 더함
        result2=TrafficAccident.iloc[:,1::3].sum(axis=1) # csv파일에서 스쿨존의 값을 모두 더함
        result3=TrafficAccident.iloc[:,2::3].sum(axis=1) # csv파일에서 무면허 사고의 값을 모두 더함
        index = mylist.curselection()[0] # 리스트박스의 선택된 항목의 인덱스를 반환하는 메소드
        info = mylist.get(index) # 인덱스에 해당하는 항목의 값을 반환하는 메소드
        result1=result1.rank(ascending=False).astype(int) # 
        result2=result2.rank(ascending=False).astype(int)
        result3=result3.rank(ascending=False).astype(int)
        for i in range(1,26):
            if(info == df.loc[i][2]):
                self.text.set(df.loc[i][2]+'의 음주운전 사고 순위 : '+result1[i].astype(str)+'위'+'\n'
                             +df.loc[i][2]+'의 스쿨존 사고 순위 : '+result2[i].astype(str)+'위'+'\n'
                             +df.loc[i][2]+'의 무면허 사고 순위 : '+result3[i].astype(str)+'위')
# 사고 유형 상세 분석 메뉴 설정
class Menu2(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        frame1=tk.Frame() # 프레임 생성
        frame1.pack(fill='both') # 프레임의 위치 지정
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
        TrafficAccident=pd.read_csv('1번.csv',encoding='cp949') #csv 파일을 cp949로 인코딩 후 파일을 불러오는 함수
        for i in range(1,26):
            mylist.insert(tk.END, TrafficAccident.loc[i][2])
        
            
        mylist.pack(side=LEFT,anchor='n',fill=BOTH) # 리스트바를 프레임의 왼쪽에 붙임
        scrollbar.config(command=mylist.yview) #스크롤바와 리스트 박스를 연결하는 함수
        
        R1 = Radiobutton(frame4, text='음주운전',variable=var, value="음주운전",font=20) # 오른쪽 프레임 체크박스 추가
        R1.pack(anchor='w') # 왼쪽으로 정렬
        R2 = Radiobutton(frame4 ,text='무면허',variable=var, value="무면허",font=20)
        R2.pack(anchor='w')
        R3 = Radiobutton(frame4, text='스쿨존',variable=var, value="스쿨존",font=20)
        R3.pack(anchor='w')
        
        bt=Button(frame1,text="사고 유형 분석",width=40,height=3,background='white',font=20,command=lambda: [master.del_frame(),master.switch_frame(Menu1)])
        bt.pack(side=LEFT,expand=True,fill=BOTH) # 버튼의 위치를 조정(side는 방향, expand는 확장 여부, fill은 공간 채움 여부)
        bt1=Button(frame1,text="사고 유형 상세 분석" ,width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu2)])
        bt1.pack(side=LEFT,expand=True,fill=BOTH)
        bt2=Button(frame1,text="유형별 최다 사고",width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu3)])
        bt2.pack(side=LEFT,expand=True,fill=BOTH)
        bt3=Button(frame4,text="연도별",width=40,height=3,background='white',font=20,command=lambda: master.graph_year(mylist,var.get()))
        bt3.pack(side=TOP,fill=BOTH)
        bt3=Button(frame4,text="시간대별",width=40,height=3,background='white',font=20,command=lambda: master.graph_time(mylist,var.get()))
        bt3.pack(side=TOP,fill=BOTH)

# 유형별 최다 사고 메뉴 설정
class Menu3(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)

        frame1=tk.Frame() # 프레임 생성
        frame1.pack(fill='both') # 프레임의 위치 지정
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
        bt.pack(side=LEFT,expand=True,fill=BOTH) # 버튼의 위치를 조정(side는 방향, expand는 확장 여부, fill은 공간 채움 여부)
        bt2=Button(frame1,text="사고 유형 상세 분석" ,width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu2)])
        bt2.pack(side=LEFT,expand=True,fill=BOTH)
        bt3=Button(frame1,text="유형별 최다 사고",width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu3)])
        bt3.pack(side=LEFT,expand=True,fill=BOTH)

if __name__ == "__main__":
    app = Accident()
    app.mainloop() # Ui를 윈도우 창을 띄어 표시