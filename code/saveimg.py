from tkinter import filedialog # 파일 저장 창을 만들어 주는 모듈
import matplotlib.pyplot as plt # 그래프 그려주는 모듈
import pandas as pd # 데이터 프레임을 만들 수 있는 모
import dataframe_image as dfi # 데이터 프레임을 이미지로 저장
import os
import seaborn as sns
from tkinter import messagebox

PATH = os.path.dirname(os.path.realpath(__file__)) # 현재 디렉토리로 이동
os.chdir(PATH)
# 이미지를 저장하는 함수
class SaveImg():
    '''
    함수명: saveImage
                변수명          자료형      설명
    매개변수 :  mylist          listbox    리스트박스
    매개변수 :  value           int        메뉴를 구분하기 위한 정수형 변수
    매개변수 :  var             string     라디오버튼 텍스트 값
    매개변수 :  var1            string     연도 옵션 메뉴 텍스트 값
    매개변수 :  var2            string     나이 시작 조건 텍스트 값
    매개변수 :  var3            string     나이 끝 조건 텍스트 값
    매개변수 :  var4            string     시간 시작 조건 텍스트 값
    매개변수 :  var5            string     시간 끝 조건 텍스트 값
    매개변수 :  bt1             string     조건 버튼 텍스트 값
    매개변수 :  bt2             string     조건 버튼 텍스트 값
    반환값 : 없음
    기능설명: 각 메뉴에 대한 그래프 이미지 저장 모듈
    '''  
    def saveImage(self,mylist,value,var,var1,var2,var3,var4,var5,bt1,bt2):
        if value==1 :
            # 이미지 저장 대화상자 띄우기
            df1=pd.read_csv('All_TrafficAccident.csv',encoding='cp949')
            if not mylist.curselection():
                messagebox.showinfo("경고","리스트 박스가 선택되지 않았습니다.")
            else:
                index = mylist.curselection()[0]
                info = mylist.get(index)
                filetypes = [('PNG images', '*.png')]
                file_path = filedialog.asksaveasfilename(filetypes=filetypes)  
                # 이미지 저장하기
                if file_path != None:

                    for i in range(1,26):
                        if(info == df1.loc[i][2]):
                            year_list=['2017','2018','2019','2020','2021']
                            title_name=df1.loc[i][2]
                            fig=plt.figure()
                            plt.rc('font', family='Malgun Gothic')
                            plt.bar(range(4,19,3),list(map(int,df1.iloc[i,4::3])),color='grey',label='음주운전')
                            plt.bar(range(5,19,3),list(map(int,df1.iloc[i,5::3])),color='royalblue',label='어린이 보호구역 사고')
                            plt.bar(range(6,19,3),list(map(int,df1.iloc[i,6::3])),color='skyblue',label='무면허')
                            plt.xticks(range(5,19,3),year_list)
                            plt.legend()
                            plt.rcParams['font.family'] = 'Malgun Gothic'

                            plt.title(title_name+' 사고 유형 연도별 분석')
                            plt.savefig(file_path)
        elif value == 2:
            if not mylist.curselection():
                messagebox.showinfo("경고","리스트 박스가 선택되지 않았습니다.")
            elif(var!='음주운전' and var!='무면허' and var!='어린이 보호구역'):
                messagebox.showinfo("라디오 박스 선택", "라디오박스 체크를 확인해 주세요.")
            else:
                filetypes = [('PNG images', '*.png')]
                file_path = filedialog.asksaveasfilename(filetypes=filetypes)  
                index = mylist.curselection()[0]
                info = mylist.get(index)
                if bt1=='나이 설정' and bt2=='나이 설정':
                    if var1=='연도' and var2 == '연령대' and var3=='연령대':
                        if(var=='음주운전'):
                            df=pd.read_csv('연도_나이_음주.csv',encoding='cp949')         
                        elif(var=='무면허'):
                            df=pd.read_csv('연도_나이_무면허.csv',encoding='cp949')
                        elif(var=='어린이 보호구역'):
                            df=pd.read_csv('연도_나이_어린이.csv',encoding='cp949')
                        df.iloc[1:,3:]=df.iloc[1:,3:].astype(int)
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
                                plt.plot(range(7),sum_list[0],color='mediumpurple',label=var,marker='o',markerfacecolor='r',markersize=10,linestyle='-')
                                plt.xticks(range(7),df.iloc[0,3:10])
                                plt.title('17~21년간의 '+title_name+'의 전체 나이별 '+var+' 분석')
                                plt.savefig(file_path)
                    else:
                        if(var1=='연도'):
                            messagebox.showinfo("연도 선택", "연도를 설정해 주세요.")
                        elif(var2=='연령대'):
                            messagebox.showinfo("연령대 선택", "연령대를 설정해 주세요.")
                        elif(var3=='연령대'):
                            messagebox.showinfo("연령대 선택", "연령대를 설정해 주세요.")
                        else:
                            if(var=='음주운전'):
                                df=pd.read_csv('연도_나이_음주.csv',encoding='cp949')         
                            elif(var=='무면허'):
                                df=pd.read_csv('연도_나이_무면허.csv',encoding='cp949')
                            elif(var=='어린이 보호구역'):
                                df=pd.read_csv('연도_나이_어린이.csv',encoding='cp949')
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
                            for i in range(2,27):
                                if(info == df.loc[i][2]):
                                    title_name=year+df.loc[i][2]
                                    fig=plt.figure()
                                    plt.rc('font', family='Malgun Gothic')
                                    plt.barh(range(var1,max_var),list(map(int,df.iloc[i,var1:max_var])),color='skyblue',label=var)
                                    plt.yticks(range(var1,max_var),df.iloc[0,var1:max_var])
                                    plt.title(year+title_name+'의 나이별 '+var+' 분석')
                                    plt.savefig(file_path)

                elif bt1=='시간 설정' and bt2=='시간 설정':
                    if var1=='연도' and var4=='시간대' and var5=='시간대':
                        if(var=='음주운전'):
                            df=pd.read_csv('음주_시간별_re.csv',encoding='cp949')         
                        elif(var=='무면허'):
                            df=pd.read_csv('무면허_시간별_re.csv',encoding='cp949')
                        elif(var=='어린이 보호구역'):
                            df=pd.read_csv('어린이_시간별.csv',encoding='cp949')
                        df.iloc[1:,3:]=df.iloc[1:,3:].astype(int)
                        for i in range(2,27):
                            if(info == df.loc[i][2]):
                                title_name=df.loc[i][2]
                                fig=plt.figure(figsize=(20,7))
                                plt.rc('font', family='Malgun Gothic')
                                sum_list=[]
                                sum_list.append([df.iloc[i,3::12].sum(),df.iloc[i,4::12].sum(),
                                        df.iloc[i,5::12].sum(),df.iloc[i,6::12].sum(),
                                        df.iloc[i,7::12].sum(),df.iloc[i,8::12].sum(),
                                        df.iloc[i,9::12].sum(),df.iloc[i,10::12].sum(),
                                        df.iloc[i,11::12].sum(),df.iloc[i,12::12].sum(),
                                        df.iloc[i,13::12].sum(),df.iloc[i,14::12].sum()])
                                plt.plot(range(12),sum_list[0],color='aquamarine',label=var,marker='o',markerfacecolor='r',markersize=10,linestyle='-')
                                plt.xticks(range(12),df.iloc[0,3:15],fontsize=9)
                                plt.title('17~21년간의 '+title_name+'의 전체시간 '+var+' 분석')
                                plt.savefig(file_path)
                    else:
                        if(var1=='연도'):
                            messagebox.showinfo("연도 선택", "연도를 설정해 주세요.")
                        elif(var4=='시간대'):
                            messagebox.showinfo("시간대 선택", "시간대를 설정해 주세요.")
                        elif(var5=='시간대'):
                            messagebox.showinfo("시간대 선택", "시간대를 설정해 주세요.")
                        else:
                            if(var=='음주운전'):
                                df=pd.read_csv('음주_시간별_re.csv',encoding='cp949')
                            elif(var=='무면허'):
                                df=pd.read_csv('무면허_시간별_re.csv',encoding='cp949')
                            elif(var=='어린이 보호구역'):
                                df=pd.read_csv('어린이_시간별.csv',encoding='cp949')
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

                            if(var4-var5 <= 0):
                                for i in range(2,27):
                                    if(info == df.loc[i][2]):
                                        title_name=df.loc[i][2]
                                        fig=plt.figure()
                                        plt.rc('font', family='Malgun Gothic')
                                        plt.barh(range(var1,max_var),list(map(int,df.iloc[i,var1:max_var])),color='violet',label=var)
                                        plt.yticks(range(var1,max_var),df.iloc[0,var1:max_var])
                                        plt.title(year+title_name+'의 시간별'+var+' 분석')
                                        plt.savefig(file_path)

        elif value == 3:
            if(var!='음주운전' and var!='무면허' and var!='어린이 보호구역'):
                messagebox.showinfo("라디오 박스 선택", "라디오박스 체크를 확인해 주세요.")
            else:
                if var == '음주운전':
                    filetypes = [('PNG images', '*.png')]
                    file_path = filedialog.asksaveasfilename(filetypes=filetypes)  
                    df1=pd.read_csv('All_TrafficAccident.csv',encoding='cp949')
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
                    fig=plt.figure(figsize=(10, 7))
                    sns.scatterplot(x=seoul_list, y=drunk_list, size=drunk_list, sizes=(300, 8000), hue=drunk_list, palette=colors, alpha=0.7, legend=False)
                    for i, txt in enumerate(seoul_list):
                        plt.annotate(txt, (seoul_list[i], drunk_list[i]), fontsize=10, ha='center', va='center')
                    plt.title('2017~2021년 서울시 구별 음주운전 교통사고 종합 발생 건수', fontsize=16)
                    plt.xlabel('서울시 구', fontsize=14)
                    plt.ylabel('음주운전 교통사고 발생 건수', fontsize=14)
                    plt.xticks([])
                    plt.yticks([])
                    #plt.ylim(200,1700)
                    plt.rcParams['font.family'] = 'Malgun Gothic'

                    plt.savefig(file_path)
    
                elif var == '어린이 보호구역':
                    filetypes = [('PNG images', '*.png')]
                    file_path = filedialog.asksaveasfilename(filetypes=filetypes)         
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
                    fig=plt.figure(figsize=(10, 7))
                    sns.scatterplot(x=seoul_list, y=school_list, size=school_list, sizes=(300, 8000), hue=school_list, palette=colors, alpha=0.7, legend=False)
                    for i, txt in enumerate(seoul_list):
                        plt.annotate(txt, (seoul_list[i], school_list[i]), fontsize=10, ha='center', va='center')
                    plt.title('2017~2021년 서울시 구별 어린이 보호구역 교통사고 종합 발생 건수', fontsize=16)
                    plt.xlabel('서울시 구', fontsize=14)
                    plt.ylabel('교통사고 발생 건수', fontsize=14)
                    plt.xticks([])
                    plt.yticks([])
                    #plt.ylim(1100,3800)
                    plt.rcParams['font.family'] = 'Malgun Gothic'

                    plt.savefig(file_path)

                elif var == '무면허':
                    filetypes = [('PNG images', '*.png')]
                    file_path = filedialog.asksaveasfilename(filetypes=filetypes)  
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
                    fig=plt.figure(figsize=(10, 7))
                    
                    sns.scatterplot(x=seoul_list, y=ul_list, size=ul_list, sizes=(300, 8000), hue=ul_list, palette=colors, alpha=0.7, legend=False)

                    for i, txt in enumerate(seoul_list):
                        plt.annotate(txt, (seoul_list[i], ul_list[i]), fontsize=10, ha='center', va='center')
                    plt.title('2017~2021년 서울시 구별 무면허 교통사고 종합 발생 건수', fontsize=16)
                    plt.xlabel('서울시 구', fontsize=14)
                    plt.ylabel('교통사고 발생 건수', fontsize=14)
                    plt.xticks([])
                    plt.yticks([])
                    #plt.ylim(50,300)
                    plt.rcParams['font.family'] = 'Malgun Gothic'

                    plt.savefig(file_path)
    '''
    함수명: saveDataImage
                변수명          자료형      설명
    매개변수 :  mylist          listbox    리스트박스
    매개변수 :  value           int        메뉴를 구분하기 위한 정수형 변수
    매개변수 :  var             string     라디오버튼 텍스트 값
    매개변수 :  var1            string     연도 옵션 메뉴 텍스트 값
    매개변수 :  var2            string     나이 시작 조건 텍스트 값
    매개변수 :  var3            string     나이 끝 조건 텍스트 값
    매개변수 :  var4            string     시간 시작 조건 텍스트 값
    매개변수 :  var5            string     시간 끝 조건 텍스트 값
    매개변수 :  bt1             string     조건 버튼 텍스트 값
    매개변수 :  bt2             string     조건 버튼 텍스트 값
    반환값 : 없음
    기능설명: 각 메뉴에 대한 데이터테이블 이미지 저장 모듈
    '''  
    def saveDataImage(self,mylist,value,var,var1,var2,var3,var4,var5,bt1,bt2):
        if value==1:
            if not mylist.curselection():
                messagebox.showinfo("리스트 박스 선택", "리스트박스 체크를 확인해 주세요.")
            else:
                # 이미지 저장 대화상자 띄우기
                index = mylist.curselection()[0]
                info = mylist.get(index)
                df1=pd.read_csv('All_TrafficAccident.csv',encoding='cp949')
                if info != None :
                    filetypes = [('PNG images', '*.png')]
                    file_path = filedialog.asksaveasfilename(filetypes=filetypes,defaultextension='.png')  
                    # 이미지 저장하기
                    if file_path != None:
                        for i in range(1,26):
                            if(info == df1.loc[i][2]):
                                df = pd.DataFrame({'음주운전':[df1.loc[i][4], df1.loc[i][7], df1.loc[i][10],df1.loc[i][13],df1.loc[i][16]],
                                                '어린이 보호구역사고':[df1.loc[i][5], df1.loc[1][8], df1.loc[i][11],df1.loc[i][14],df1.loc[i][17]],
                                                '무면허':[df1.loc[i][6], df1.loc[i][9], df1.loc[i][12],df1.loc[i][15],df1.loc[i][18]]},
                                                index=['2017','2018','2019','2020','2021'])
                    df=df.rename_axis('연도') 
                    dfi.export(df,file_path,max_cols = -1, max_rows = -1,table_conversion='matplotlib')
        elif value==2:
            if not mylist.curselection():
                messagebox.showinfo("리스트 박스 선택","리스트 박스 선택을 확인해 주세요.")
            elif(var!='음주운전' and var!='무면허' and var!='어린이 보호구역'):
                messagebox.showinfo("라디오 박스 선택", "라디오박스 체크를 확인해 주세요.")
            else:
                index = mylist.curselection()[0]
                info = mylist.get(index)
                if info != None :
                    filetypes = [('PNG images', '*.png')]
                    file_path = filedialog.asksaveasfilename(filetypes=filetypes,defaultextension='.png')  
                    # 이미지 저장하기
                    if file_path != None:
                        index = mylist.curselection()[0]
                        info = mylist.get(index)
                        if bt1=='나이 설정' and bt2=='나이 설정':
                            if(var=='음주운전'):
                                df1=pd.read_csv('연도_나이_음주.csv',encoding='cp949')         
                            elif(var=='무면허'):
                                df1=pd.read_csv('연도_나이_무면허.csv',encoding='cp949')
                            elif(var=='어린이 보호구역'):
                                df1=pd.read_csv('연도_나이_어린이.csv',encoding='cp949')
                            else:
                                pass

                            df1.iloc[1:,3:]=df1.iloc[1:,3:].astype(int)

                            if(var1=='연도' and var2=='연령대' and var3=='연령대'):
                                for i in range(2,27):
                                    if(info == df1.loc[i][2]):
                                        df=pd.DataFrame([{'20세이하':df1.iloc[i,3::7].sum(),
                                                '21~30세':df1.iloc[i,4::7].sum(),
                                                '31~40세':df1.iloc[i,5::7].sum(),
                                                '41~50세':df1.iloc[i,6::7].sum(),
                                                '51~60세':df1.iloc[i,7::7].sum(),
                                                '61~64세':df1.iloc[i,8::7].sum(),
                                                '65세이상':df1.iloc[i,9::7].sum()}],index=['17~21년'])                             
                                dfi.export(df,file_path,max_cols = -1, max_rows = -1,table_conversion='matplotlib')    

                            else:
                                if(var1=='연도'):
                                    messagebox.showinfo("연도 선택", "연도를 설정해 주세요.")
                                elif(var2=='연령대'):
                                    messagebox.showinfo("연령대 선택", "연령대를 설정해 주세요.")
                                elif(var3=='연령대'):
                                    messagebox.showinfo("연령대 선택", "연령대를 설정해 주세요.")
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
                                            if(info == df1.loc[i][2]):
                                                if(max_var-var1==1):
                                                    df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1]}],index=[year])

                                                elif(max_var-var1==2):
                                                    df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                                    df1.iloc[0,var1+1]:df1.iloc[i,var1+1]}],index=[year])
                                                        
                                                elif(max_var-var1==3):
                                                    df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                                    df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                                    df1.iloc[0,var1+2]:df1.iloc[i,var1+2]}],index=[year])
                                                                    
                                                        
                                                elif(max_var-var1==4):
                                                    df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                                    df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                                    df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                                    df1.iloc[0,var1+3]:df1.iloc[i,var1+3]}],index=[year])
                                                        
                                                elif(max_var-var1==5):
                                                    df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                                    df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                                    df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                                    df1.iloc[0,var1+3]:df1.iloc[i,var1+3],
                                                                    df1.iloc[0,var1+4]:df1.iloc[i,var1+4]}],index=[year])
                                                elif(max_var-var1==6):
                                                    df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                                    df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                                    df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                                    df1.iloc[0,var1+3]:df1.iloc[i,var1+3],
                                                                    df1.iloc[0,var1+4]:df1.iloc[i,var1+4],
                                                                    df1.iloc[0,var1+5]:df1.iloc[i,var1+5]}],index=[year])
                                                        
                                                elif(max_var-var1==7):
                                                    df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                                    df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                                    df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                                    df1.iloc[0,var1+3]:df1.iloc[i,var1+3],
                                                                    df1.iloc[0,var1+4]:df1.iloc[i,var1+4],
                                                                    df1.iloc[0,var1+5]:df1.iloc[i,var1+5],
                                                                    df1.iloc[0,var1+6]:df1.iloc[i,var1+6]}],index=[year])   
                                        dfi.export(df,file_path,max_cols = -1, max_rows = -1,table_conversion='matplotlib')            

                        elif bt1=='시간 설정' and bt2=='시간 설정':
                            if(var=='음주운전'):
                                df1=pd.read_csv('음주_시간별_re.csv',encoding='cp949')
                            elif(var=='무면허'):
                                df1=pd.read_csv('무면허_시간별_re.csv',encoding='cp949')
                            elif(var=='어린이 보호구역'):
                                df1=pd.read_csv('어린이_시간별.csv',encoding='cp949')
                            else:
                                pass

                            df1.iloc[1:,3:]=df1.iloc[1:,3:].astype(int)

                            if(var1=='연도' and var4=='시간대' or var5=='시간대'):
                                for i in range(2,27):
                                    if(info == df1.loc[i][2]):  
                                        df=pd.DataFrame([{'00시~02시':df1.iloc[i,3::12].sum(),
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
                                                        ],index=['17~21년'])
                                dfi.export(df,file_path,fontsize=8,table_conversion='matplotlib')

                            else:
                                if(var1=='연도'):
                                    messagebox.showinfo("연도 선택", "연도를 설정해 주세요.")
                                elif(var4=='시간대'):
                                    messagebox.showinfo("시간대 선택", "시간대를 설정해 주세요.")
                                elif(var5=='시간대'):
                                    messagebox.showinfo("시간대 선택", "시간대를 설정해 주세요.")
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

                                    if(var4-var5 <= 0):
                                        for i in range(2,27):
                                            if(info == df1.loc[i][2]):
                                                if(var5-var4==0):
                                                    df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1]}],index=[year])

                                                elif(var5-var4==1):
                                                    df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                                    df1.iloc[0,var1+1]:df1.iloc[i,var1+1]}],index=[year])
                                                    
                                                elif(var5-var4==2):
                                                    df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                                    df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                                    df1.iloc[0,var1+2]:df1.iloc[i,var1+2]}],index=[year])
                                                    
                                                elif(var5-var4==3):
                                                    df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                                    df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                                    df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                                    df1.iloc[0,var1+3]:df1.iloc[i,var1+3]}],index=[year])
                                                    
                                                elif(var5-var4==4):
                                                    df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                                    df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                                    df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                                    df1.iloc[0,var1+3]:df1.iloc[i,var1+3],
                                                                    df1.iloc[0,var1+4]:df1.iloc[i,var1+4]}],index=[year])
                                                    
                                                elif(var5-var4==5):
                                                    df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                                    df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                                    df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                                    df1.iloc[0,var1+3]:df1.iloc[i,var1+3],
                                                                    df1.iloc[0,var1+4]:df1.iloc[i,var1+4],
                                                                    df1.iloc[0,var1+5]:df1.iloc[i,var1+5]}],index=[year])
                                                    
                                                elif(var5-var4==6):
                                                    df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                                    df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                                    df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                                    df1.iloc[0,var1+3]:df1.iloc[i,var1+3],
                                                                    df1.iloc[0,var1+4]:df1.iloc[i,var1+4],
                                                                    df1.iloc[0,var1+5]:df1.iloc[i,var1+5],
                                                                    df1.iloc[0,var1+6]:df1.iloc[i,var1+6]}],index=[year])
                                                    
                                                elif(var5-var4==7):
                                                    df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                                    df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                                    df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                                    df1.iloc[0,var1+3]:df1.iloc[i,var1+3],
                                                                    df1.iloc[0,var1+4]:df1.iloc[i,var1+4],
                                                                    df1.iloc[0,var1+5]:df1.iloc[i,var1+5],
                                                                    df1.iloc[0,var1+6]:df1.iloc[i,var1+6],
                                                                    df1.iloc[0,var1+7]:df1.iloc[i,var1+7]}],index=[year])
                                                    
                                                elif(var5-var4==8):
                                                    df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                                    df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                                    df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                                    df1.iloc[0,var1+3]:df1.iloc[i,var1+3],
                                                                    df1.iloc[0,var1+4]:df1.iloc[i,var1+4],
                                                                    df1.iloc[0,var1+5]:df1.iloc[i,var1+5],
                                                                    df1.iloc[0,var1+6]:df1.iloc[i,var1+6],
                                                                    df1.iloc[0,var1+7]:df1.iloc[i,var1+7],
                                                                    df1.iloc[0,var1+8]:df1.iloc[i,var1+8]}],index=[year])
                                                    
                                                elif(var5-var4==9):
                                                    df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                                    df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                                    df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                                    df1.iloc[0,var1+3]:df1.iloc[i,var1+3],
                                                                    df1.iloc[0,var1+4]:df1.iloc[i,var1+4],
                                                                    df1.iloc[0,var1+5]:df1.iloc[i,var1+5],
                                                                    df1.iloc[0,var1+6]:df1.iloc[i,var1+6],
                                                                    df1.iloc[0,var1+7]:df1.iloc[i,var1+7],
                                                                    df1.iloc[0,var1+8]:df1.iloc[i,var1+8],
                                                                    df1.iloc[0,var1+9]:df1.iloc[i,var1+9]}],index=[year])
                                                    
                                                elif(var5-var4==10):
                                                    df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
                                                                    df1.iloc[0,var1+1]:df1.iloc[i,var1+1],
                                                                    df1.iloc[0,var1+2]:df1.iloc[i,var1+2],
                                                                    df1.iloc[0,var1+3]:df1.iloc[i,var1+3],
                                                                    df1.iloc[0,var1+4]:df1.iloc[i,var1+4],
                                                                    df1.iloc[0,var1+5]:df1.iloc[i,var1+5],
                                                                    df1.iloc[0,var1+6]:df1.iloc[i,var1+6],
                                                                    df1.iloc[0,var1+7]:df1.iloc[i,var1+7],
                                                                    df1.iloc[0,var1+8]:df1.iloc[i,var1+8],
                                                                    df1.iloc[0,var1+9]:df1.iloc[i,var1+9],
                                                                    df1.iloc[0,var1+10]:df1.iloc[i,var1+10]}],index=[year])
                                                    
                                                elif(var5-var4==11):
                                                    df=pd.DataFrame([{df1.iloc[0,var1]:df1.iloc[i,var1],
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
                                                                    df1.iloc[0,var1+11]:df1.iloc[i,var1+11]}],index=[year])
                                        dfi.export(df,file_path,fontsize=8,table_conversion='matplotlib')
        else:
            if(var!='음주운전' and var!='무면허' and var!='어린이 보호구역'):
                messagebox.showinfo("라디오 박스 선택", "라디오박스 체크를 확인해 주세요.")
            else:
                filetypes = [('PNG images', '*.png')]
                file_path = filedialog.asksaveasfilename(filetypes=filetypes,defaultextension='.png')  
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
                    dfi.export(df,file_path,max_cols = -1, max_rows = -1,fontsize=8,table_conversion='matplotlib')
                elif var=='음주운전':
                    for i in range(1,26):
                        drunk_list.append(df1.iloc[i,5]+df1.iloc[i,8]+df1.iloc[i,11]+df1.iloc[i,14]+df1.iloc[i,17])
                    df=pd.DataFrame({'음주운전':drunk_list},index=seoul_list)
                    df=df.rename_axis('자치구')
                    df =df.sort_values(by='음주운전', ascending=False)
                    dfi.export(df,file_path,max_cols = -1, max_rows = -1,fontsize=8,table_conversion='matplotlib')
                elif var=='어린이 보호구역':
                    for i in range(1,26):
                        school_list.append(df1.iloc[i,4]+df1.iloc[i,7]+df1.iloc[i,10]+df1.iloc[i,13]+df1.iloc[i,16])
                    df=pd.DataFrame({'어린이 보호구역':school_list},index=seoul_list)
                    df=df.rename_axis('자치구')
                    df =df.sort_values(by='어린이 보호구역', ascending=False)
                    dfi.export(df,file_path,max_cols = -1, max_rows = -1,fontsize=8,table_conversion='matplotlib')