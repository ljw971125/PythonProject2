from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import tkinter as tk # 인터페이스를 만들 때
from tkinter import messagebox
import seaborn as sns

# 데이터를 분석 정제하고 그래프를 출력하는 함수
class Graph(): 
    def graph(self,mylist,event):
        try:
            global canvas
            canvas.get_tk_widget().pack_forget()
            TrafficAccident=pd.read_csv('All_TrafficAccident.csv',encoding='cp949') #csv 파일을 cp949로 인코딩 후 파일을 불러오는 함수
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
            TrafficAccident=pd.read_csv('All_TrafficAccident.csv',encoding='cp949') #csv 파일을 cp949로 인코딩 후 파일을 불러오는 함수
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
    def show_graph1(self,mylist,var):
        if not mylist.curselection():
            messagebox.showinfo("리스트 박스 선택", "리스트박스 선택을 확인해 주세요.")

        global canvas
        index = mylist.curselection()[0]
        info = mylist.get(index)
        if(var=='음주운전'):
            df=pd.read_csv('연도_나이_음주.csv',encoding='cp949')         
        elif(var=='무면허'):
            df=pd.read_csv('연도_나이_무면허.csv',encoding='cp949')
        elif(var=='스쿨존'):
            df=pd.read_csv('연도_나이_음주.csv',encoding='cp949')
        else:
            messagebox.showinfo("라디오 박스 선택", "라디오박스 체크를 확인해 주세요.")

        df.iloc[1:,3:]=df.iloc[1:,3:].astype(int)

        try:
            canvas.get_tk_widget().pack_forget()
            for i in range(2,27):
                if(info == df.loc[i][2]):
                    title_name=df.loc[i][2]
                    fig=plt.figure()
                    plt.rc('font', family='Malgun Gothic')
                    sum_list=[]
                    sum_list.append([df.iloc[i,3::7].sum(),df.iloc[i,4::7].sum(),
                              df.iloc[i,5::7].sum(),df.iloc[i,6::7].sum(),
                            df.iloc[i,7::7].sum(),df.iloc[i,8::7].sum(),
                            df.iloc[i,9::7].sum()])
                    plt.barh(range(7),sum_list[0],color='grey',label=var)
                    plt.yticks(range(7),df.iloc[0,3:10])
                    plt.title('17~21년간의 '+title_name+'의 전체 나이별 '+var+' 분석')
                    canvas = FigureCanvasTkAgg(fig,master=self)         
                    canvas.get_tk_widget().pack()
                else:
                    continue
        except:
            for i in range(2,27):
                if(info == df.loc[i][2]):
                    title_name=df.loc[i][2]
                    fig=plt.figure()
                    plt.rc('font', family='Malgun Gothic')
                    sum_list=[]
                    sum_list.append([df.iloc[i,3::7].sum(),df.iloc[i,4::7].sum(),
                              df.iloc[i,5::7].sum(),df.iloc[i,6::7].sum(),
                            df.iloc[i,7::7].sum(),df.iloc[i,8::7].sum(),
                            df.iloc[i,9::7].sum()])
                    plt.barh(range(7),sum_list[0],color='grey',label=var)
                    plt.yticks(range(7),df.iloc[0,3:10])
                    plt.title('17~21년간의 '+title_name+'의 전체 나이별 '+var+' 분석')
                    canvas = FigureCanvasTkAgg(fig,master=self)         
                    canvas.get_tk_widget().pack()
                else:
                    continue
    def show_graph2(self,mylist,var):
        if not mylist.curselection():
            messagebox.showinfo("리스트 박스 선택", "리스트박스 선택을 확인해 주세요.")

        global canvas
        index = mylist.curselection()[0]
        info = mylist.get(index)
        if(var=='음주운전'):
            df=pd.read_csv('음주_시간별_re.csv',encoding='cp949')         
        elif(var=='무면허'):
            df=pd.read_csv('무면허_시간별_re.csv',encoding='cp949')
        elif(var=='스쿨존'):
            df=pd.read_csv('음주_시간별_re.csv',encoding='cp949')
        else:
            messagebox.showinfo("라디오 박스 선택", "라디오박스 체크를 확인해 주세요.")

        df.iloc[1:,3:]=df.iloc[1:,3:].astype(int)

        try:
            canvas.get_tk_widget().pack_forget()
            for i in range(2,27):
                if(info == df.loc[i][2]):
                    title_name=df.loc[i][2]
                    fig=plt.figure()
                    plt.rc('font', family='Malgun Gothic')
                    sum_list=[]
                    sum_list.append([df.iloc[i,3::12].sum(),df.iloc[i,4::12].sum(),
                            df.iloc[i,5::12].sum(),df.iloc[i,6::12].sum(),
                            df.iloc[i,7::12].sum(),df.iloc[i,8::12].sum(),
                            df.iloc[i,9::12].sum(),df.iloc[i,10::12].sum(),
                            df.iloc[i,11::12].sum(),df.iloc[i,12::12].sum(),
                            df.iloc[i,13::12].sum(),df.iloc[i,14::12].sum()])
                    plt.barh(range(12),sum_list[0],color='grey',label='무면허')
                    plt.yticks(range(12),df.iloc[0,3:15])
                    plt.title('17~21년간의 '+title_name+'의 전체 시간별 '+var+' 분석')
                    canvas = FigureCanvasTkAgg(fig,master=self)         
                    canvas.get_tk_widget().pack()
                else:
                    continue
        except:
            for i in range(2,27):
                if(info == df.loc[i][2]):
                    title_name=df.loc[i][2]
                    fig=plt.figure()
                    plt.rc('font', family='Malgun Gothic')
                    sum_list=[]
                    sum_list.append([df.iloc[i,3::12].sum(),df.iloc[i,4::12].sum(),
                            df.iloc[i,5::12].sum(),df.iloc[i,6::12].sum(),
                            df.iloc[i,7::12].sum(),df.iloc[i,8::12].sum(),
                            df.iloc[i,9::12].sum(),df.iloc[i,10::12].sum(),
                            df.iloc[i,11::12].sum(),df.iloc[i,12::12].sum(),
                            df.iloc[i,13::12].sum(),df.iloc[i,14::12].sum()])
                    plt.barh(range(12),sum_list[0],color='grey',label='무면허')
                    plt.yticks(range(12),df.iloc[0,3:15])
                    plt.title('17~21년간의 '+title_name+'의 전체 시간별 '+var+' 분석')
                    canvas = FigureCanvasTkAgg(fig,master=self)         
                    canvas.get_tk_widget().pack()
                else:
                    continue
        #연령 그래프        
    def show_graph3(self,mylist,var,var1,var2,var3):

        if not mylist.curselection():
            messagebox.showinfo("리스트 박스 선택", "리스트박스 선택을 확인해 주세요.")

        global canvas
        index = mylist.curselection()[0]
        info = mylist.get(index)
        if(var=='음주운전'):
            df=pd.read_csv('연도_나이_음주.csv',encoding='cp949')         
        elif(var=='무면허'):
            df=pd.read_csv('연도_나이_무면허.csv',encoding='cp949')
        elif(var=='스쿨존'):
            df=pd.read_csv('연도_나이_음주.csv',encoding='cp949')
        else:
            messagebox.showinfo("라디오 박스 선택", "라디오박스 체크를 확인해 주세요.")

        df.iloc[0,4:38:7]='21~30세'
        df.iloc[0,5:38:7]='31~40세'
        df.iloc[0,6:38:7]='41~50세'
        df.iloc[0,7:38:7]='51~60세'
        df.iloc[0,8:38:7]='61~64세'

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

        if(var2+var3 >= 7):
            messagebox.showinfo("범위를 잘못 설정하셨습니다.", "처음 나이가 두번째 나이보다 작아야 합니다.")
        else:
            try:
                canvas.get_tk_widget().pack_forget()
                for i in range(2,27):
                    if(info == df.loc[i][2]):
                        title_name=df.loc[i][2]
                        fig=plt.figure()
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(var1,max_var),list(map(int,df.iloc[i,var1:max_var])),color='grey',label=var)
                        plt.yticks(range(var1,max_var),df.iloc[0,var1:max_var])
                        plt.title(year+title_name+'의 나이별 '+var+' 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    else:
                        continue
            except:
                for i in range(2,27):
                    if(info == df.loc[i][2]):
                        title_name=df.loc[i][2]
                        fig=plt.figure()
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(var1,max_var),list(map(int,df.iloc[i,var1:max_var])),color='grey',label=var)
                        plt.yticks(range(var1,max_var),df.iloc[0,var1:max_var])
                        plt.title(year+title_name+'의 나이별 '+var+' 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    else:
                        continue
    # 시간 그래프
    def show_graph4(self,mylist,var,var1,var4,var5):
        # var : 라디오박스선택값
        # var1 : 연도 선택
        # var6 : 나이 선택
        # var4 : 시작 시간
        # var5 : 끝나는 시간

        if not mylist.curselection():
            messagebox.showinfo("리스트 박스 선택", "리스트박스 선택을 확인해 주세요.")

        global canvas
        index = mylist.curselection()[0]
        info = mylist.get(index)

        if(var=='음주운전'):
            df=pd.read_csv('음주_시간별_re.csv',encoding='cp949')
        elif(var=='무면허'):
            df=pd.read_csv('무면허_시간별_re.csv',encoding='cp949')
        elif(var=='스쿨존'):
            df=pd.read_csv('음주_시간별.csv',encoding='cp949')
        else:
            messagebox.showinfo("라디오 박스 선택", "라디오박스 체크를 확인해 주세요.")
        #year_list=['2017','2018','2019','2020','2021']
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


        if(var4-var5 > 0):
            messagebox.showinfo("범위를 잘못 설정하셨습니다.", "처음 시간이 두번째 시간보다 작아야 합니다.")
        else:
            try:
                canvas.get_tk_widget().pack_forget()
                for i in range(2,27):
                    if(info == df.loc[i][2]):
                        title_name=df.loc[i][2]
                        fig=plt.figure()
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(var1,max_var),list(map(int,df.iloc[i,var1:max_var])),color='grey',label=var)
                        plt.yticks(range(var1,max_var),df.iloc[0,var1:max_var])
                        plt.title(year+title_name+'의 시간별'+var+' 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    else:
                        continue
            except:
                for i in range(2,27):
                    if(info == df.loc[i][2]):
                        title_name=df.loc[i][2]
                        fig=plt.figure()
                        plt.rc('font', family='Malgun Gothic')
                        plt.barh(range(var1,max_var),list(map(int,df.iloc[i,var1:max_var])),color='grey',label=var)
                        plt.yticks(range(var1,max_var),df.iloc[0,var1:max_var])
                        plt.title(year+title_name+'의 시간별'+var+' 분석')
                        canvas = FigureCanvasTkAgg(fig,master=self)         
                        canvas.get_tk_widget().pack()
                    else:
                        continue   

    def graphBubble(self,var):
        plt.rc('font', family='Malgun Gothic')
        if var == '음주운전':
            try:
                global canvas
                canvas.get_tk_widget().pack_forget()
                df1=pd.read_csv('All_TrafficAccident.csv',encoding='cp949')
                df1.iloc[1:,4:]=df1.iloc[1:,4:].astype(int)
                seoul_list = ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구']
                colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#2E294E',
                          '#1B4F72', '#0E6251', '#196F3D', '#7D6608', '#A04000',
                          '#78281F', '#4A235A', '#1B2631', '#B7950B', '#8D6E63',
                          '#2C3E50', '#8E44AD', '#16A085', '#F39C12', '#F5B7B1',
                          '#7FB3D5', '#77DD77', '#FFC300', '#F4D03F','red']
                drunk_list=[]
                for i in range(1,26):
                    drunk_list.append(df1.iloc[i,4]+df1.iloc[i,7]+df1.iloc[i,10]+df1.iloc[i,13]+df1.iloc[i,16])
                fig=plt.figure(figsize=(10, 13))
                # scatterplot() 함수 사용
                sns.scatterplot(x=seoul_list, y=drunk_list, size=drunk_list, sizes=(300, 8000), hue=drunk_list, palette=colors, alpha=0.7, legend=False)
                # 버블 안에 텍스트 삽입하기
                for i, txt in enumerate(seoul_list):
                    plt.annotate(txt, (seoul_list[i], drunk_list[i]), fontsize=10, ha='center', va='center')
                # 그래프 타이틀 설정
                plt.title('서울시 구별 음주운전 교통사고 발생 건수', fontsize=16)
                # x축, y축 라벨 설정
                plt.xlabel('서울시 구', fontsize=14)
                plt.ylabel('음주운전 교통사고 발생 건수', fontsize=14)
                plt.xticks([])
                plt.yticks([])
                plt.rcParams['font.family'] = 'Malgun Gothic'
                canvas = FigureCanvasTkAgg(fig,master=self)         
                canvas.get_tk_widget().pack()
            except:
                df1=pd.read_csv('All_TrafficAccident.csv',encoding='cp949')
                df1.iloc[1:,4:]=df1.iloc[1:,4:].astype(int)
                seoul_list = ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구']
                colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#2E294E',
                          '#1B4F72', '#0E6251', '#196F3D', '#7D6608', '#A04000',
                          '#78281F', '#4A235A', '#1B2631', '#B7950B', '#8D6E63',
                          '#2C3E50', '#8E44AD', '#16A085', '#F39C12', '#F5B7B1',
                          '#7FB3D5', '#77DD77', '#FFC300', '#F4D03F','red']
                drunk_list=[]
                for i in range(1,26):
                    drunk_list.append(df1.iloc[i,4]+df1.iloc[i,7]+df1.iloc[i,10]+df1.iloc[i,13]+df1.iloc[i,16])
                fig=plt.figure(figsize=(10, 13))
                # scatterplot() 함수 사용
                sns.scatterplot(x=seoul_list, y=drunk_list, size=drunk_list, sizes=(300, 8000), hue=drunk_list, palette=colors, alpha=0.7, legend=False)
                # 버블 안에 텍스트 삽입하기
                for i, txt in enumerate(seoul_list):
                    plt.annotate(txt, (seoul_list[i], drunk_list[i]), fontsize=10, ha='center', va='center')
                # 그래프 타이틀 설정
                plt.title('서울시 구별 음주운전 교통사고 발생 건수', fontsize=16)
                # x축, y축 라벨 설정
                plt.xlabel('서울시 구', fontsize=14)
                plt.ylabel('음주운전 교통사고 발생 건수', fontsize=14)
                plt.xticks([])
                plt.yticks([])
                plt.rcParams['font.family'] = 'Malgun Gothic'
                canvas = FigureCanvasTkAgg(fig,master=self)         
                canvas.get_tk_widget().pack()
        elif var == '어린이 보호구역':
            try:
                canvas.get_tk_widget().pack_forget()
                df1=pd.read_csv('All_TrafficAccident.csv',encoding='cp949')
                df1.iloc[1:,4:]=df1.iloc[1:,4:].astype(int)
                seoul_list = ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구']
                colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#2E294E',
                          '#1B4F72', '#0E6251', '#196F3D', '#7D6608', '#A04000',
                          '#78281F', '#4A235A', '#1B2631', '#B7950B', '#8D6E63',
                          '#2C3E50']
                for i in range(1,26):
                    school_list.append(df1.iloc[i,5]+df1.iloc[i,8]+df1.iloc[i,11]+df1.iloc[i,14]+df1.iloc[i,17])
                fig=plt.figure(figsize=(10, 13))
                # scatterplot() 함수 사용
                sns.scatterplot(x=seoul_list, y=drunk_list, size=school_list, sizes=(300, 8000), hue=school_list, palette=colors, alpha=0.7, legend=False)
                # 버블 안에 텍스트 삽입하기
                for i, txt in enumerate(seoul_list):
                    plt.annotate(txt, (seoul_list[i], school_list[i]), fontsize=10, ha='center', va='center')
                # 그래프 타이틀 설정
                plt.title('서울시 구별 어린이 보호구역 교통사고 발생 건수', fontsize=16)
                # x축, y축 라벨 설정
                plt.xlabel('서울시 구', fontsize=14)
                plt.ylabel('교통사고 발생 건수', fontsize=14)
                plt.xticks([])
                plt.yticks([])
                plt.rcParams['font.family'] = 'Malgun Gothic'

                canvas = FigureCanvasTkAgg(fig,master=self)         
                canvas.get_tk_widget().pack()
            except:
                df1=pd.read_csv('All_TrafficAccident.csv',encoding='cp949')
                df1.iloc[1:,4:]=df1.iloc[1:,4:].astype(int)
                seoul_list = ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구']
                colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#2E294E',
                          '#1B4F72', '#0E6251', '#196F3D', '#7D6608', '#A04000',
                          '#78281F', '#4A235A', '#1B2631', '#B7950B', '#8D6E63',
                          '#2C3E50']
                school_list=[]
                for i in range(1,26):
                    school_list.append(df1.iloc[i,5]+df1.iloc[i,8]+df1.iloc[i,11]+df1.iloc[i,14]+df1.iloc[i,17])
                fig=plt.figure(figsize=(10, 13))
                # scatterplot() 함수 사용
                sns.scatterplot(x=seoul_list, y=school_list, size=school_list, sizes=(300, 8000), hue=school_list, palette=colors, alpha=0.7, legend=False)
                # 버블 안에 텍스트 삽입하기
                for i, txt in enumerate(seoul_list):
                    plt.annotate(txt, (seoul_list[i], school_list[i]), fontsize=10, ha='center', va='center')
                # 그래프 타이틀 설정
                plt.title('서울시 구별 어린이 보호구역 교통사고 발생 건수', fontsize=16)
                # x축, y축 라벨 설정
                plt.xlabel('서울시 구', fontsize=14)
                plt.ylabel('교통사고 발생 건수', fontsize=14)
                plt.xticks([])
                plt.yticks([])
                plt.rcParams['font.family'] = 'Malgun Gothic'

                canvas = FigureCanvasTkAgg(fig,master=self)         
                canvas.get_tk_widget().pack()
        elif var == '무면허':
            try:
                canvas.get_tk_widget().pack_forget()
                df1=pd.read_csv('All_TrafficAccident.csv',encoding='cp949')
                df1.iloc[1:,4:]=df1.iloc[1:,4:].astype(int)
                seoul_list = ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구']
                colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#2E294E',
                          '#1B4F72', '#0E6251', '#196F3D', '#7D6608', '#A04000',
                          '#78281F', '#4A235A', '#1B2631', '#B7950B', '#8D6E63',
                          '#2C3E50', '#8E44AD', '#16A085', '#F39C12', '#F5B7B1',
                          '#7FB3D5', '#77DD77', '#FFC300' ]
                ul_list=[]
                for i in range(1,26):
                    ul_list.append(df1.iloc[i,6]+df1.iloc[i,9]+df1.iloc[i,12]+df1.iloc[i,15]+df1.iloc[i,18])
                fig=plt.figure(figsize=(10, 13))
                # scatterplot() 함수 사용
                sns.scatterplot(x=seoul_list, y=ul_list, size=ul_list, sizes=(300, 8000), hue=ul_list, palette=colors, alpha=0.7, legend=False)
                # 버블 안에 텍스트 삽입하기
                for i, txt in enumerate(seoul_list):
                    plt.annotate(txt, (seoul_list[i], ul_list[i]), fontsize=10, ha='center', va='center')
                # 그래프 타이틀 설정
                plt.title('서울시 구별 무면허 교통사고 발생 건수', fontsize=16)
                # x축, y축 라벨 설정
                plt.xlabel('서울시 구', fontsize=14)
                plt.ylabel('교통사고 발생 건수', fontsize=14)
                plt.xticks([])
                plt.yticks([])
                plt.rcParams['font.family'] = 'Malgun Gothic'

                canvas = FigureCanvasTkAgg(fig,master=self)         
                canvas.get_tk_widget().pack()
            except:
                df1=pd.read_csv('All_TrafficAccident.csv',encoding='cp949')
                df1.iloc[1:,4:]=df1.iloc[1:,4:].astype(int)
                seoul_list = ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구']
                colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#2E294E',
                          '#1B4F72', '#0E6251', '#196F3D', '#7D6608', '#A04000',
                          '#78281F', '#4A235A', '#1B2631', '#B7950B', '#8D6E63',
                          '#2C3E50', '#8E44AD', '#16A085', '#F39C12', '#F5B7B1',
                          '#7FB3D5', '#77DD77', '#FFC300' ]
                ul_list=[]
                for i in range(1,26):
                    ul_list.append(df1.iloc[i,6]+df1.iloc[i,9]+df1.iloc[i,12]+df1.iloc[i,15]+df1.iloc[i,18])
                fig=plt.figure(figsize=(10, 13))
                # scatterplot() 함수 사용
                sns.scatterplot(x=seoul_list, y=ul_list, size=ul_list, sizes=(300, 8000), hue=ul_list, palette=colors, alpha=0.7, legend=False)
                # 버블 안에 텍스트 삽입하기
                for i, txt in enumerate(seoul_list):
                    plt.annotate(txt, (seoul_list[i], ul_list[i]), fontsize=10, ha='center', va='center')
                # 그래프 타이틀 설정
                plt.title('서울시 구별 무면허 교통사고 발생 건수', fontsize=16)
                # x축, y축 라벨 설정
                plt.xlabel('서울시 구', fontsize=14)
                plt.ylabel('교통사고 발생 건수', fontsize=14)
                plt.xticks([])
                plt.yticks([])
                plt.rcParams['font.family'] = 'Malgun Gothic'

                canvas = FigureCanvasTkAgg(fig,master=self)         
                canvas.get_tk_widget().pack()