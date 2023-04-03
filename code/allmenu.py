import tkinter as tk # 인터페이스를 만들 때
import saveimg #그래프 이미지 저장 모듈
from tkinter import * #파이썬 GUI 화면 설정 모듈
import pandas as pd #데이터 프래임 모듈
import graph #그래프 보여주는 모듈
from pandastable import Table # tkinter ui에서 pandas 모양으로 데이터 프레임을 만들어주는 모듈
import os #os 설정 모듈
from PIL import Image, ImageTk # 파이썬으로 이미지를 다룰 수 있게 해주는 모듈
import image #이미지 불러오는 모듈 

PATH = os.path.dirname(os.path.realpath(__file__)) # 현재 디렉토리로 이동
os.chdir(PATH)
# 시작메뉴 설정
           
class StartMenu(tk.Frame):
    '''
    함수명:_init__
                변수명    자료형    설명
    매개변수 : ep_menu     menu
    반환값 : 없음
    기능설명: 클래스에 대한 인자값을 받아 GUI화면 구성
    '''  
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        ep_menu = tk.Menu(self)
        ep_menu.add_command(label='도움말',command=lambda :self.openExplainWindow())    
        master.config(menu=ep_menu)
        tk.Label(self, text="서울시 교통사고 조사", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5) # 시작 화면 상단 라벨
        self.photo = ImageTk.PhotoImage(Image.open('car.png')) # ui 아이콘 불러오기
        tk.Label(self,image=self.photo).pack() # 이미지 라벨
        tk.Label(self, text="2팀 : 김민수, 이지운, 장기헌, 장윤종, 전장현", font=('Helvetica', 10, "bold")).pack(side="top", fill="x", pady=5) #시작 화면 팀 라벨
        tk.Button(self, text="start",width=20,height=2,command=lambda: master.switch_frame(Menu1)).pack(side=BOTTOM) # 시작 버튼

    '''
    함수명:openExplainWindow
                변수명          자료형      설명
    매개변수 :  image_viewer   Toplevel   새창을 띄우는 기능
    매개변수 :  image_list     list       사용설명서에  띄울 사진 리스트
    매개변수 :  app               새창을 띄우는 기능
    반환값 : 없음
    기능설명: 사용설명서 새창을 띄우는 함수
    '''  

    def openExplainWindow(self):
        image_viewer = tk.Toplevel(self)
        image_list = ["1.png", "2.png", "3.png", "4.png", "5.png"]
        app = image.ImageViewer(image_viewer, image_list)


# 메인메뉴 설정
class Menu1(tk.Frame):
    '''
    함수명:__init__
                변수명          자료형      설명
    매개변수 :  frame1,2,3,4    Frame     위젯 위치설정 기능
    매개변수 :  scrollbar       Scrolbar  스크롤바 생성
    매개변수 :  mylist          Listbox   리스트박스 생성          
    반환값 : 없음
    기능설명: GUI 화면 생성 및 위젯 설정
    '''  
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        menu = tk.Menu(self)
        menu.add_command(label="그래프 저장",command=lambda: [saveimg.SaveImg.save_image(self,mylist,1,None,None,None,None,None,None,None,None)])
        menu.add_command(label="데이터 프레임 보기",command=lambda :self.open_new_window(mylist))
        menu.add_command(label="데이터 프레임 저장",command=lambda :saveimg.SaveImg.save_data_image(self,mylist,1,None,None,None,None,None,None,None,None))
        master.config(menu=menu)
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
        ta_df_int=pd.read_csv('All_TrafficAccident.csv',encoding='cp949') #csv 파일을 cp949로 인코딩 후 파일을 불러오는 함수
        for i in range(1,26):
            mylist.insert(tk.END, ta_df_int.loc[i][2])
        header_label = tk.Label(frame2, text="서울특별시 자치구", font=("Arial", 12, "bold"))
        header_label.pack(pady=10)
        mylist.pack(side=LEFT,fill=BOTH,expand=True) # 리스트바를 프레임의 왼쪽에 붙임
      
        scrollbar.config(command=mylist.yview) #스크롤바와 리스트 박스를 연결하는 함수
        bt=Button(frame1,text="사고 유형 분석",width=40,height=3,background='grey',cursor='hand2',font=20)
        bt.pack(side=LEFT,expand=True,fill=BOTH) # 버튼의 위치를 조정(side는 방향, expand는 확장 여부, fill은 공간 채움 여부)
        bt2=Button(frame1,text="사고 유형 상세 분석" ,width=40,height=3,background='white',font=20,cursor='hand2',command=lambda:[master.del_frame(),master.switch_frame(Menu2)])
        bt2.pack(side=LEFT,expand=True,fill=BOTH)
        bt3=Button(frame1,text="유형별 최다 사고",width=40,height=3,background='white',font=20,cursor='hand2',command=lambda:[master.del_frame(),master.switch_frame(Menu3)])
        bt3.pack(side=LEFT,expand=True,fill=BOTH)
        tk.Label(frame4,textvariable=self.text,font=('Helvetica', 18, "bold")).pack(side=RIGHT,padx=10)
        mylist.bind("<<ListboxSelect>>", lambda event : [graph.Graph.graph(self,mylist,event),self.showRank(mylist)]) # 리스트바에서 값을 선택 할 때 바로 그래프가 출력 되도록 해줌


    '''
    함수명: openDataWindow
                변수명          자료형      설명
    매개변수 :  new_window      Toplevel   새창 생성
    매개변수 :  ta_df           DataFrame  구별 사고 발생 건수 데이터 프래임
    매개변수 :  mylist_index    int         리스트박스에 선택한 인덱스 반환
    매개변수 :  mylist_selection str        리스트박스에 선택값 반환
    반환값 : 없음
    기능설명: 데이터프래임 값 보여주는 기능
    '''  

    def openDataWindiw(self,mylist):
        new_window = tk.Toplevel(self.master)
        ta_df=pd.read_csv('All_TrafficAccident.csv',encoding='cp949')
        mylist_index = mylist.curmylist_selection()[0]
        mylist_selection = mylist.get(mylist_index)
        new_window.title(mylist_selection+' 사고유형 데이터 프레임')
        for i in range(1,26):
            if(mylist_selection == ta_df.loc[i][2]):
                ta_df = pd.DataFrame({'음주운전':[ta_df.loc[i][4], ta_df.loc[i][7], ta_df.loc[i][10],ta_df.loc[i][13],ta_df.loc[i][16]],
                                         '어린이 보호구역사고':[ta_df.loc[i][5], ta_df.loc[i][8], ta_df.loc[i][11],ta_df.loc[i][14],ta_df.loc[i][17]],
                                         '무면허':[ta_df.loc[i][6], ta_df.loc[i][9], ta_df.loc[i][12],ta_df.loc[i][15],ta_df.loc[i][18]]}
                                        )
        table=Table(new_window,dataframe=ta_df)
        table.show()
        
    '''
    함수명: showRank
                변수명          자료형      설명
    매개변수 :  new_window      Toplevel   새창 생성
    매개변수 :  ta_df           DataFrame  구별 사고 발생 건수 데이터 프래임
    매개변수 :  ta_df_int       DataFrame  데이터 프래임 정수화
    매개변수 :  mylist_index    int        리스트박스에 선택한 인덱스 반환
    매개변수 :  mylist_selection str       리스트박스에 선택값 반환
    반환값 : 없음
    기능설명: 데이터프래임 값 보여주는 기능
    '''    
    
    # 자료의 발생 건수를 모두 더하고 순위를 보여주는 함수
    def showRank(self,mylist):
        ta_df=pd.read_csv('All_TrafficAccident.csv',encoding='cp949')
        ta_df_int=ta_df.iloc[1:,4:].astype(int)
        result1=ta_df_int.iloc[:,0::3].sum(axis=1) # csv파일에서 음주운전의 값을 모두 더함
        result2=ta_df_int.iloc[:,1::3].sum(axis=1) # csv파일에서 어린이 보호구역의 값을 모두 더함
        result3=ta_df_int.iloc[:,2::3].sum(axis=1) # csv파일에서 무면허 사고의 값을 모두 더함
        mylist_index = mylist.curselection()[0] # 리스트박스의 선택된 항목의 인덱스를 반환하는 메소드
        mylist_seletion = mylist.get(mylist_index) # 인덱스에 해당하는 항목의 값을 반환하는 메소드
        result1=result1.rank(ascending=False).astype(int) # 
        result2=result2.rank(ascending=False).astype(int)
        result3=result3.rank(ascending=False).astype(int)
        for i in range(1,26):
            if(mylist_seletion == ta_df.loc[i][2]):
                self.text.set(ta_df.loc[i][2]+'의 음주운전 사고 순위 : '+result1[i].astype(str)+'위'+'\n'
                             +ta_df.loc[i][2]+'의 어린이 보호구역 사고 순위 : '+result2[i].astype(str)+'위'+'\n'
                             +ta_df.loc[i][2]+'의 무면허 사고 순위 : '+result3[i].astype(str)+'위')
# 사고 유형 상세 분석 메뉴 설정

class Menu2(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        menu = tk.Menu(self)
        menu.add_command(label="그래프 저장",command=lambda:saveimg.SaveImg.save_image(self,mylist,2,var.get(),var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),bt5.cget('text'),bt6.cget('text')))
        menu.add_command(label="데이터 프레임 보기",command=lambda :self.open_data_Frame2(mylist,var.get(),var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),bt5.cget('text'),bt6.cget('text')))
        menu.add_command(label="데이터 프레임 저장",command=lambda :saveimg.SaveImg.save_data_image(self,mylist,2,var.get(),var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),bt5.cget('text'),bt6.cget('text')))
        master.config(menu=menu)
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

        mylist = Listbox(frame2, yscrollcommand=scrollbar.set, height=0, selectbackground='pink' ,selectforeground='black',font=20) # 리스트바 생성, 스크롤바 연결, 높이 0으로 설정
        df1=pd.read_csv('All_TrafficAccident.csv',encoding='cp949')
        for i in range(1,26): 
            mylist.insert(tk.END, df1.loc[i][2])
        header_label = tk.Label(frame2, text="서울특별시 자치구", font=("Arial", 12, "bold"))
        header_label.pack(pady=10)
        mylist.pack(side=LEFT,fill=BOTH) # 리스트바를 프레임의 왼쪽에 붙임
        scrollbar.config(command=mylist.yview)
      
        
        R1 = Radiobutton(frame4 ,text='음주운전',variable=var, value="음주운전",font=20)
        R1.pack(anchor='w') # 왼쪽으로 정렬
        R2 = Radiobutton(frame4, text='무면허',variable=var, value="무면허",font=20)
        R2.pack(anchor='w')
        R3 = Radiobutton(frame4, text='어린이 보호구역',variable=var, value="어린이 보호구역",font=20)
        R3.pack(anchor='w')
        bt3=Button(frame4,text="연령별",width=10,height=5,background='white',font=20,cursor='hand2',command=lambda: [self.hide_widget(option_menu4),self.hide_widget(label2),self.hide_widget(option_menu5),self.hide_widget(bt6),self.change_text(bt6,1),self.change_text(bt5,1),self.change_option(var1,1),self.change_option(var2,2),self.change_option(var3,2),self.show_widget(option_menu1),self.show_widget(option_menu2),self.show_widget(label1),self.show_widget(option_menu3),self.show_widget(bt5),graph.Graph.show_graph1(self,mylist,var.get())])
        bt3.pack()
        bt4=Button(frame4,text="시간별",width=10,height=5,background='white',font=20,cursor='hand2',command=lambda: [self.hide_widget(option_menu2),self.hide_widget(label1),self.hide_widget(option_menu3),self.hide_widget(bt5),self.change_text(bt6,2),self.change_text(bt5,2),self.change_option(var1,1),self.change_option(var4,3),self.change_option(var5,3),self.show_widget(option_menu1),self.show_widget(option_menu4),self.show_widget(label2),self.show_widget(option_menu5),self.show_widget(bt6),graph.Graph.show_graph2(self,mylist,var.get())])
        bt4.pack()
    
        bt=Button(frame1,text="사고 유형 분석",width=40,height=3,background='white',font=20,cursor='hand2',command=lambda: [master.del_frame(),master.switch_frame(Menu1)])
        bt.pack(side=LEFT,expand=True,fill=BOTH)
        bt1=Button(frame1,text="사고 유형 상세 분석" ,width=40,height=3,background='grey',font=20,cursor='hand2',command=lambda:[master.del_frame(),master.switch_frame(Menu2)])
        bt1.pack(side=LEFT,expand=True,fill=BOTH)
        bt2=Button(frame1,text="유형별 최다 사고",width=40,height=3,background='white',font=20,cursor='hand2',command=lambda:[master.del_frame(),master.switch_frame(Menu3)])
        bt2.pack(side=LEFT,expand=True,fill=BOTH)

        var1 = tk.StringVar()
        var1.set('연도')
        option_menu1 = tk.OptionMenu(frame3, var1, '2017', '2018', '2019', '2020', '2021')
        option_menu1.config(width=8)

        var2=tk.StringVar()
        var2.set('연령대')
        option_menu2 = tk.OptionMenu(frame3, var2, '20세이하','21세','31세','41세','51세','61세','65세이상')
        option_menu2.config(width=8)

        label1 = tk.Label(frame3, text="~")

        var3=tk.StringVar()
        var3.set('연령대')
        option_menu3 = tk.OptionMenu(frame3, var3, '20세이하','30세','40세','50세','60세','64세','65세이상')
        option_menu3.config(width=8)

        var4=tk.StringVar()
        var4.set('시간대')
        option_menu4 = tk.OptionMenu(frame3, var4, '00:00','02:00','04:00','06:00','08:00','10:00','12:00','14:00','16:00','18:00','20:00','22:00')
        option_menu4.config(width=8)

        label2 = tk.Label(frame3, text="~")

        var5=tk.StringVar()
        var5.set('시간대')
        option_menu5 = tk.OptionMenu(frame3, var5, '02:00','04:00','06:00','08:00','10:00','12:00','14:00','16:00','18:00','20:00','22:00','24:00')
        option_menu5.config(width=8)

        bt5=Button(frame3,text="나이",width=8,font=10,cursor='hand2',command=lambda: graph.Graph.show_graph3(self,mylist,var.get(),var1.get(),var2.get(),var3.get()))
        bt6=Button(frame3,text="시간",width=8,font=10,cursor='hand2',command=lambda: graph.Graph.show_graph4(self,mylist,var.get(),var1.get(),var4.get(),var5.get()))
    
    def change_text(self,bt,value):
        if(value==1):
            bt['text'] = '나이'
        else:
            bt['text'] = '시간'

    def change_option(self,var,value):
        if(value==1):
            var.set('연도')
        elif(value==2):
            var.set('연령대')
        elif(value==3):
            var.set('시간대')

    def hide_widget(self,widget):
        try:
            widget.pack_forget()
        except:
            widget.pack_forget()
    def show_widget(self,widget):
        widget.pack(side=LEFT)

    def del_frame(self,master):
        for widget in master.winfo_children():
            widget.destroy()


    def open_data_Frame2(self,mylist,var,var1,var2,var3,var4,var5,bt1,bt2):

        mylist_index = mylist.curselection()[0]
        mylist_seletion = mylist.get(mylist_index)

        if bt1=='나이' and bt2=='나이':
            if(var=='음주운전'):
                df1=pd.read_csv('연도_나이_음주.csv',encoding='cp949')         
            elif(var=='무면허'):
                df1=pd.read_csv('연도_나이_무면허.csv',encoding='cp949')
            elif(var=='어린이 보호구역'):
                df1=pd.read_csv('연도_나이_어린이.csv',encoding='cp949')
            else:
                pass

            df1.iloc[1:,3:]=df1.iloc[1:,3:].astype(int)

            if(var2=='연령대' or var3=='연령대'):
                
                new_window = tk.Toplevel(self.master)
                new_window.title('17~21년간의 '+mylist_seletion+'의 '+var+'의 전체 연령 데이터 프레임')
                for i in range(2,27):
                    if(mylist_seletion == df1.loc[i][2]):
                        ta_df=pd.DataFrame([{'20세이하':df1.iloc[i,3::7].sum(),
                                '21~30세':df1.iloc[i,4::7].sum(),
                                '31~40세':df1.iloc[i,5::7].sum(),
                                '41~50세':df1.iloc[i,6::7].sum(),
                                '51~60세':df1.iloc[i,7::7].sum(),
                                '61~64세':df1.iloc[i,8::7].sum(),
                                '65세이상':df1.iloc[i,9::7].sum()}
                                ])
                table=Table(new_window,dataframe=ta_df)
                table.show()

            else:
                if(var2=='20세이하'):
                    var2=0
                elif(var2=='21세'):
                    var2=1
                elif(var2=='31세'):
                    var2=2
                elif(var2=='41세'):
                    var2=3
                elif(var2=='51세'):
                    var2=4
                elif(var2=='61세'):
                    var2=5
                elif(var2=='65세이상'):
                    var2=6

                if(var3=='20세이하'):
                    var3=6
                elif(var3=='30세'):
                    var3=5
                elif(var3=='40세'):
                    var3=4
                elif(var3=='50세'):
                    var3=3
                elif(var3=='60세'):
                    var3=2
                elif(var3=='64세'):
                    var3=1
                else:
                    var3=0

                if(var1=='2017'):
                    var1=3+var2
                    max_var=10-var3
                    year='2017년 '
                elif(var1=='2018'):
                    var1=10+var2
                    max_var=17-var3
                    year='2018년 '
                elif(var1=='2019'):
                    var1=17+var2
                    max_var=24-var3
                    year='2019년 '
                elif(var1=='2020'):
                    var1=24+var2
                    max_var=31-var3
                    year='2020년 '
                elif(var1=='2021'):
                    var1=31+var2
                    max_var=38
                    year='2021년 '

                if(var2+var3 < 7):
                    for i in range(2,27):
                        if(mylist_seletion == df1.loc[i][2]):
                            new_window = tk.Toplevel(self.master)
                            new_window.title(year+mylist_seletion+'의 '+var+' 의 연령별 데이터 프레임')

                            if(max_var-var1==1):
                                ta_df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1]}])

                            elif(max_var-var1==2):
                                ta_df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                df1.iloc[0,var1+1]:df1.iloc[i,var1+1]}])
                                    
                            elif(max_var-var1==3):
                                ta_df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                df1.iloc[0,var1+2]:df1.iloc[i,var1+2]}])
                                                
                                    
                            elif(max_var-var1==4):
                                ta_df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                df1.iloc[0,var1+3]:df1.iloc[i,var1+3]}])
                                    
                            elif(max_var-var1==5):
                                ta_df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                df1.iloc[0,var1+3]:df1.iloc[i,var1+3],
                                                df1.iloc[0,var1+4]:df1.iloc[i,var1+4]}])
                            elif(max_var-var1==6):
                                ta_df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                df1.iloc[0,var1+3]:df1.iloc[i,var1+3],
                                                df1.iloc[0,var1+4]:df1.iloc[i,var1+4],
                                                df1.iloc[0,var1+5]:df1.iloc[i,var1+5]}])
                                    
                            elif(max_var-var1==7):
                                ta_df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                df1.iloc[0,var1+3]:df1.iloc[i,var1+3],
                                                df1.iloc[0,var1+4]:df1.iloc[i,var1+4],
                                                df1.iloc[0,var1+5]:df1.iloc[i,var1+5],
                                                df1.iloc[0,var1+6]:df1.iloc[i,var1+6]}])
                    
                            table=Table(new_window,dataframe=ta_df)
                            table.show()

        elif bt1=='시간' and bt2=='시간':
            if(var=='음주운전'):
                df1=pd.read_csv('음주_시간별_re.csv',encoding='cp949')
            elif(var=='무면허'):
                df1=pd.read_csv('무면허_시간별_re.csv',encoding='cp949')
            elif(var=='어린이 보호구역'):
                df1=pd.read_csv('어린이_시간별.csv',encoding='cp949')
            else:
                pass

            df1.iloc[1:,3:]=df1.iloc[1:,3:].astype(int)

            if(var4=='시간대' or var5=='시간대'):
                new_window = tk.Toplevel(self.master)
                new_window.title('17~21년간의 '+mylist_seletion+'의 '+var+'의 전체 시간 데이터 프레임')
                for i in range(2,27):
                    if(mylist_seletion == df1.loc[i][2]):  
                        ta_df=pd.DataFrame([{'00시~02시':df1.iloc[i,3::12].sum(),
                                        '02시~04시':df1.iloc[i,4::12].sum(),
                                        '04시~06시':df1.iloc[i,5::12].sum(),
                                        '06시~08시':df1.iloc[i,6::12].sum(),
                                        '08시~10시':df1.iloc[i,7::12].sum(),
                                        '10시~12시':df1.iloc[i,8::12].sum(),
                                        '12시~14시':df1.iloc[i,9::12].sum(),
                                        '14시~16시':df1.iloc[i,10::12].sum(),
                                        '16시~18시':df1.iloc[i,11::12].sum(),
                                        '18시~20시':df1.iloc[i,12::12].sum(),
                                        '20시~22시':df1.iloc[i,13::12].sum(),
                                        '22시~24시':df1.iloc[i,14::12].sum()}
                                        ])
                table=Table(new_window,dataframe=ta_df)
                table.show()
            else:
                if(var4=='00:00'):
                    var4=0
                elif(var4=='02:00'):
                    var4=1
                elif(var4=='04:00'):
                    var4=2
                elif(var4=='06:00'):
                    var4=3
                elif(var4=='08:00'):
                    var4=4
                elif(var4=='10:00'):
                    var4=5
                elif(var4=='12:00'):
                    var4=6
                elif(var4=='14:00'):
                    var4=7
                elif(var4=='16:00'):
                    var4=8
                elif(var4=='18:00'):
                    var4=9
                elif(var4=='20:00'):
                    var4=10
                else:
                    var4=11

                if(var5=='02:00'):
                    var5=0
                elif(var5=='04:00'):
                    var5=1
                elif(var5=='06:00'):
                    var5=2
                elif(var5=='08:00'):
                    var5=3
                elif(var5=='10:00'):
                    var5=4
                elif(var5=='12:00'):
                    var5=5
                elif(var5=='14:00'):
                    var5=6
                elif(var5=='16:00'):
                    var5=7
                elif(var5=='18:00'):
                    var5=8
                elif(var5=='20:00'):
                    var5=9
                elif(var5=='22:00'):
                    var5=10
                else:
                    var5=11

                if(var1=='2017'):
                    var1=3+var4
                    max_var=4+var5
                    year='2017년 '
                elif(var1=='2018'):
                    var1=15+var4
                    max_var=16+var5
                    year='2018년 '
                elif(var1=='2019'):
                    var1=27+var4
                    max_var=28+var5
                    year='2019년 '
                elif(var1=='2020'):
                    var1=39+var4
                    max_var=40+var5
                    year='2020년 '
                elif(var1=='2021'):
                    var1=51+var4
                    max_var=52+var5
                    year='2021년 '

                new_window = tk.Toplevel(self.master)
                new_window.title(year+mylist_seletion+'의 '+var+ '의 시간별 데이터 프레임')
                if(var4-var5 <= 0):
                    for i in range(2,27):
                        if(mylist_seletion == df1.loc[i][2]):
                            if(var5-var4==0):
                                ta_df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1]}])

                            elif(var5-var4==1):
                                ta_df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                  df1.iloc[0,var1+1]:df1.iloc[i,var1+1]}])
                                
                            elif(var5-var4==2):
                                ta_df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                  df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                  df1.iloc[0,var1+2]:df1.iloc[i,var1+2]}])
                                
                            elif(var5-var4==3):
                                ta_df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                  df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                  df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                  df1.iloc[0,var1+3]:df1.iloc[i,var1+3]}])
                                
                            elif(var5-var4==4):
                                ta_df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                  df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                  df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                  df1.iloc[0,var1+3]:df1.iloc[i,var1+3],
                                                  df1.iloc[0,var1+4]:df1.iloc[i,var1+4]}])
                                
                            elif(var5-var4==5):
                                ta_df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                  df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                  df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                  df1.iloc[0,var1+3]:df1.iloc[i,var1+3],
                                                  df1.iloc[0,var1+4]:df1.iloc[i,var1+4],
                                                  df1.iloc[0,var1+5]:df1.iloc[i,var1+5]}])
                                
                            elif(var5-var4==6):
                                ta_df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                  df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                  df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                  df1.iloc[0,var1+3]:df1.iloc[i,var1+3],
                                                  df1.iloc[0,var1+4]:df1.iloc[i,var1+4],
                                                  df1.iloc[0,var1+5]:df1.iloc[i,var1+5],
                                                  df1.iloc[0,var1+6]:df1.iloc[i,var1+6]}])
                                
                            elif(var5-var4==7):
                                ta_df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                  df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                  df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                  df1.iloc[0,var1+3]:df1.iloc[i,var1+3],
                                                  df1.iloc[0,var1+4]:df1.iloc[i,var1+4],
                                                  df1.iloc[0,var1+5]:df1.iloc[i,var1+5],
                                                  df1.iloc[0,var1+6]:df1.iloc[i,var1+6],
                                                  df1.iloc[0,var1+7]:df1.iloc[i,var1+7]}])
                                
                            elif(var5-var4==8):
                                ta_df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                  df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                  df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                  df1.iloc[0,var1+3]:df1.iloc[i,var1+3],
                                                  df1.iloc[0,var1+4]:df1.iloc[i,var1+4],
                                                  df1.iloc[0,var1+5]:df1.iloc[i,var1+5],
                                                  df1.iloc[0,var1+6]:df1.iloc[i,var1+6],
                                                  df1.iloc[0,var1+7]:df1.iloc[i,var1+7],
                                                  df1.iloc[0,var1+8]:df1.iloc[i,var1+8]}])
                                
                            elif(var5-var4==9):
                                ta_df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                  df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                  df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                  df1.iloc[0,var1+3]:df1.iloc[i,var1+3],
                                                  df1.iloc[0,var1+4]:df1.iloc[i,var1+4],
                                                  df1.iloc[0,var1+5]:df1.iloc[i,var1+5],
                                                  df1.iloc[0,var1+6]:df1.iloc[i,var1+6],
                                                  df1.iloc[0,var1+7]:df1.iloc[i,var1+7],
                                                  df1.iloc[0,var1+8]:df1.iloc[i,var1+8],
                                                  df1.iloc[0,var1+9]:df1.iloc[i,var1+9]}])
                                
                            elif(var5-var4==10):
                                ta_df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                  df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                  df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                  df1.iloc[0,var1+3]:df1.iloc[i,var1+3],
                                                  df1.iloc[0,var1+4]:df1.iloc[i,var1+4],
                                                  df1.iloc[0,var1+5]:df1.iloc[i,var1+5],
                                                  df1.iloc[0,var1+6]:df1.iloc[i,var1+6],
                                                  df1.iloc[0,var1+7]:df1.iloc[i,var1+7],
                                                  df1.iloc[0,var1+8]:df1.iloc[i,var1+8],
                                                  df1.iloc[0,var1+9]:df1.iloc[i,var1+9],
                                                  df1.iloc[0,var1+10]:df1.iloc[i,var1+10]}])
                                
                            elif(var5-var4==11):
                                ta_df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                  df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                  df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                  df1.iloc[0,var1+3]:df1.iloc[i,var1+3],
                                                  df1.iloc[0,var1+4]:df1.iloc[i,var1+4],
                                                  df1.iloc[0,var1+5]:df1.iloc[i,var1+5],
                                                  df1.iloc[0,var1+6]:df1.iloc[i,var1+6],
                                                  df1.iloc[0,var1+7]:df1.iloc[i,var1+7],
                                                  df1.iloc[0,var1+8]:df1.iloc[i,var1+8],
                                                  df1.iloc[0,var1+9]:df1.iloc[i,var1+9],
                                                  df1.iloc[0,var1+10]:df1.iloc[i,var1+10],
                                                  df1.iloc[0,var1+11]:df1.iloc[i,var1+11]}])
                    table=Table(new_window,dataframe=ta_df)
                    table.show()


class Menu3(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        menu = tk.Menu(self)
        menu.add_command(label="그래프 저장",command=lambda:saveimg.SaveImg.save_image(self,None,3,var.get(),None,None,None,None,None,None,None))
        menu.add_command(label="데이터 프래임 보기",command=lambda :self.open_data_Frame3(var.get()))
        menu.add_command(label="데이터 프래임 저장",command=lambda :saveimg.SaveImg.save_data_image(self,None,3,var.get(),None,None,None,None,None,None,None))
        master.config(menu=menu)

        frame1=tk.Frame()
        frame1.pack(fill='both')
        frame2=tk.Frame()
        frame2.pack(side=RIGHT)
        var=StringVar()
        var.set(NONE)


        R1 = Radiobutton(frame2, text='음주운전',variable=var, value="음주운전",font=20,command=lambda:graph.Graph.graphBubble(self,var.get())) # 오른쪽 프레임 체크박스 추가
        R1.pack(anchor='w') # 왼쪽으로 정렬
        R2 = Radiobutton(frame2, text='무면허',variable=var, value="무면허",font=20,command=lambda:graph.Graph.graphBubble(self,var.get()))
        R2.pack(anchor='w')
        R3 = Radiobutton(frame2, text='어린이 보호구역',variable=var, value="어린이 보호구역",font=20,command=lambda:graph.Graph.graphBubble(self,var.get()))
        R3.pack(anchor='w')
        
        
        bt=Button(frame1,text="사고 유형 분석",width=40,height=3,background='white',font=20,command=lambda: [master.del_frame(),master.switch_frame(Menu1)])
        bt.pack(side=LEFT,expand=True,fill=BOTH)
        bt2=Button(frame1,text="사고 유형 상세 분석" ,width=40,height=3,background='white',font=20,command=lambda:[master.del_frame(),master.switch_frame(Menu2)])
        bt2.pack(side=LEFT,expand=True,fill=BOTH)
        bt3=Button(frame1,text="유형별 최다 사고",width=40,height=3,background='grey',font=20)
        bt3.pack(side=LEFT,expand=True,fill=BOTH)
        


    def open_data_Frame3(self,var):
        if var != None:
            new_window = tk.Toplevel(self.master)
            new_window.title('사고유형 데이터 프레임')
            df1=pd.read_csv('All_TrafficAccident.csv',encoding='cp949')
            #구 ,발생건수
            df1.iloc[1:,4:]=df1.iloc[1:,4:].astype(int)
            seoul_list=['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구']
            drunk_list=[]
            ul_list=[]
            school_list=[]
            if var=='무면허':
                for i in range(1,26):
                    ul_list.append(df1.iloc[i,6]+df1.iloc[i,9]+df1.iloc[i,12]+df1.iloc[i,15]+df1.iloc[i,18])
                df=pd.DataFrame({'무면허':ul_list},index=seoul_list)
                df=df.rename_axis('자치구')
                df =df.sort_values(by='무면허', ascending=False)
                text = tk.Text(new_window)
                text.insert('end', df.to_markdown())
                text.pack()
            elif var=='음주운전':
                for i in range(1,26):
                    drunk_list.append(df1.iloc[i,5]+df1.iloc[i,8]+df1.iloc[i,11]+df1.iloc[i,14]+df1.iloc[i,17])
                df=pd.DataFrame({'음주운전':drunk_list},index=seoul_list)
                df=df.rename_axis('자치구')
                df =df.sort_values(by='음주운전', ascending=False)
                text = tk.Text(new_window)
                text.insert('end', df.to_markdown())
                text.pack()
            elif var=='어린이 보호구역':
                for i in range(1,26):
                    school_list.append(df1.iloc[i,4]+df1.iloc[i,7]+df1.iloc[i,10]+df1.iloc[i,13]+df1.iloc[i,16])
                df=pd.DataFrame({'어린이 보호구역':school_list},index=seoul_list)
                df=df.rename_axis('자치구')
                df =df.sort_values(by='어린이 보호구역', ascending=False)
                text = tk.Text(new_window)
                text.insert('end', df.to_markdown())
                text.pack()