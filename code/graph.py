from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import tkinter as tk # 인터페이스를 만들 때

# 데이터를 분석 정제하고 그래프를 출력하는 함수
class Graph(): 
    def graph_time(self,mylist,var):
        try:
            global canvas
            canvas.get_tk_widget().pack_forget()
            TrafficAccident=pd.read_csv('All_TrafficAccident.csv',encoding='cp949') #csv 파일을 cp949로 인코딩 후 파일을 불러오는 함수 
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
                        return self,mylist,var
                    else:
                        continue
                else:
                    continue
        except:
            TrafficAccident=pd.read_csv('All_TrafficAccident.csv',encoding='cp949') #csv 파일을 cp949로 인코딩 후 파일을 불러오는 함수
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
                        return self,mylist,var
                    else:
                        continue
                else:
                    continue
    def graph_year(self,mylist,var):
            try:
                global canvas
                canvas.get_tk_widget().pack_forget() # ui에 그려져 있는 그래프를 지움
                TrafficAccident=pd.read_csv('All_TrafficAccident.csv',encoding='cp949') #csv 파일을 cp949로 인코딩 후 파일을 불러오는 함수
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
                            return self,mylist,var
                        else:
                            continue
                    else:
                        continue
            except:
                TrafficAccident=pd.read_csv('All_TrafficAccident.csv',encoding='cp949') #csv 파일을 cp949로 인코딩 후 파일을 불러오는 함수
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
                            return self,mylist,var
                        else:
                            continue
                    else:
                        continue

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