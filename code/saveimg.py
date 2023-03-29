from tkinter import filedialog # 파일 저장 창을 만들어 주는 모듈
import matplotlib.pyplot as plt # 그래프 그려주는 모듈
import pandas as pd # 데이터 프레임을 만들 수 있는 모
import dataframe_image as dfi # 데이터 프레임을 이미지로 저장
import os
import seaborn as sns

PATH = os.path.dirname(os.path.realpath(__file__)) # 현재 디렉토리로 이동
os.chdir(PATH)
# 이미지를 저장하는 함수
class SaveImg(): 
    def save_image(self,mylist,value,var):
        if value==1 or value==2:
            # 이미지 저장 대화상자 띄우기
            df1=pd.read_csv('1번.csv',encoding='cp949')
            index = mylist.curselection()[0]
            info = mylist.get(index)
            if info != None :
                file_path = filedialog.asksaveasfilename(defaultextension='.png')
                # 이미지 저장하기
                if file_path != None:

                    for i in range(1,26):
                        if(info == df1.loc[i][2]):
                            year_list=['2017','2018','2019','2020','2021']
                            title_name=df1.loc[i][2]
                            fig=plt.figure()
                            plt.rc('font', family='Malgun Gothic')
                            plt.bar(range(4,19,3),list(map(int,df1.iloc[i,4::3])),color='grey',label='음주운전')
                            plt.bar(range(5,19,3),list(map(int,df1.iloc[i,5::3])),color='royalblue',label='스쿨존 사고')
                            plt.bar(range(6,19,3),list(map(int,df1.iloc[i,6::3])),color='skyblue',label='무면허')
                            plt.xticks(range(5,19,3),year_list)
                            plt.legend()
                            plt.rcParams['font.family'] = 'Malgun Gothic'

                            plt.title(title_name+' 사고 유형 연도별 분석')
                            plt.savefig(file_path)
        else:
            if var == '음주운전':
                
                file_path = filedialog.asksaveasfilename(defaultextension='.png')
                df1=pd.read_csv('1번.csv',encoding='cp949')
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
                sns.scatterplot(x=seoul_list, y=drunk_list, size=drunk_list, sizes=(300, 8000), hue=drunk_list, palette=colors, alpha=0.7, legend=False)
                for i, txt in enumerate(seoul_list):
                    plt.annotate(txt, (seoul_list[i], drunk_list[i]), fontsize=10, ha='center', va='center')
                plt.title('서울시 구별 음주운전 교통사고 발생 건수', fontsize=16)
                plt.xlabel('서울시 구', fontsize=14)
                plt.ylabel('음주운전 교통사고 발생 건수', fontsize=14)
                plt.xticks([])
                plt.yticks([])
                plt.rcParams['font.family'] = 'Malgun Gothic'

                plt.savefig(file_path)
 
            elif var == '어린이 보호구역':
                file_path = filedialog.asksaveasfilename(defaultextension='.png')        
                df1=pd.read_csv('1번.csv',encoding='cp949')
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
                sns.scatterplot(x=seoul_list, y=school_list, size=school_list, sizes=(300, 8000), hue=school_list, palette=colors, alpha=0.7, legend=False)
                for i, txt in enumerate(seoul_list):
                    plt.annotate(txt, (seoul_list[i], school_list[i]), fontsize=10, ha='center', va='center')
                plt.title('서울시 구별 어린이 보호구역 교통사고 발생 건수', fontsize=16)
                plt.xlabel('서울시 구', fontsize=14)
                plt.ylabel('교통사고 발생 건수', fontsize=14)
                plt.xticks([])
                plt.yticks([])
                plt.rcParams['font.family'] = 'Malgun Gothic'

                plt.savefig(file_path)

            elif var == '무면허':
                file_path = filedialog.asksaveasfilename(defaultextension='.png')
                df1=pd.read_csv('1번.csv',encoding='cp949')
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
                
                sns.scatterplot(x=seoul_list, y=ul_list, size=ul_list, sizes=(300, 8000), hue=ul_list, palette=colors, alpha=0.7, legend=False)

                for i, txt in enumerate(seoul_list):
                    plt.annotate(txt, (seoul_list[i], ul_list[i]), fontsize=10, ha='center', va='center')
                plt.title('서울시 구별 무면허 교통사고 발생 건수', fontsize=16)
                plt.xlabel('서울시 구', fontsize=14)
                plt.ylabel('교통사고 발생 건수', fontsize=14)
                plt.xticks([])
                plt.yticks([])
                plt.rcParams['font.family'] = 'Malgun Gothic'

                plt.savefig(file_path)

            
        
            
    #def save_image3(self,)                    
    
    def save_data_image(self,mylist,value,var):
        if value==1 or value==2:
            # 이미지 저장 대화상자 띄우기
            df1=pd.read_csv('1번.csv',encoding='cp949')
            index = mylist.curselection()[0]
            info = mylist.get(index)
            if info != None :
                file_path = filedialog.asksaveasfilename(defaultextension='.png')

                # 이미지 저장하기
                if file_path != None:
                     for i in range(1,26):
                        if(info == df1.loc[i][2]):

                            df = pd.DataFrame({'음주운전':[df1.loc[i][4], df1.loc[i][7], df1.loc[i][10],df1.loc[i][13],df1.loc[i][16]],
                                             '스쿨존사고':[df1.loc[i][5], df1.loc[1][8], df1.loc[i][11],df1.loc[i][14],df1.loc[i][17]],
                                             '무면허':[df1.loc[i][6], df1.loc[i][9], df1.loc[i][12],df1.loc[i][15],df1.loc[i][18]]},
                                            index=['2017','2018','2019','2020','2021'])
                df=df.rename_axis('연도') 
                dfi.export(df,file_path,max_cols = -1, max_rows = -1)
        else:
            file_path = filedialog.asksaveasfilename(defaultextension='.png')
            df1=pd.read_csv('1번.csv',encoding='cp949')
            #구 ,발생건수
            df1.iloc[1:,4:]=df1.iloc[1:,4:].astype(int)
            seoul_list=['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구']
            drunk_list=[]
            ul_list=[]
            school_list=[]
            for i in range(1,26):
                ul_list.append(df1.iloc[i,6]+df1.iloc[i,9]+df1.iloc[i,12]+df1.iloc[i,15]+df1.iloc[i,18])
            for i in range(1,26):
                school_list.append(df1.iloc[i,5]+df1.iloc[i,8]+df1.iloc[i,11]+df1.iloc[i,14]+df1.iloc[i,17])
            for i in range(1,26):
                drunk_list.append(df1.iloc[i,4]+df1.iloc[i,7]+df1.iloc[i,10]+df1.iloc[i,13]+df1.iloc[i,16])
            df=pd.DataFrame({'무면허':ul_list,
                            '음주운전':drunk_list,
                            '어린이 보호구역':school_list},
                            index=seoul_list)
            df
            df=df.rename_axis('자치구')
            dfi.export(df,file_path,max_cols = -1, max_rows = -1)