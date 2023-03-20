import tkinter.ttk as ttk
from tkinter import *
import csv
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import pandas as pd


seoul_list=['종로구','중구','용산구','성동구','광진구','동대문구','중랑구','성북구','강북구','도봉구','노원구','은평구','서대문구','마포구','양천구','강서구','구로구','금천구','영등포구','동작구','관악구','서초구','강남구','송파구','강동구']
accident_list=['음주운전','어린이 사고','과속운전','신호위반','무면허','무단횡단']
year_list=['2017','2018','2019','2020','2021']


root =Tk()
root.title("GUI")
root.geometry("700x700")

# 이미지 열기
# image = Image.open("seoul.png")
# # PhotoImage로 변환
# photo = ImageTk.PhotoImage(image)

# # 이미지 레이블 생성
# image_label = Label(root, image=photo)
# image_label.grid(row=0, column=0)


#blank_0=Label(root,text='',width=5)
#blank_0.grid(row=1,column=0)

seoul_combobox = ttk.Combobox(root, height =10, values =seoul_list)
seoul_combobox.grid(row=1, column=0)
seoul_combobox.set("구를 선택하세요") # 최초 목록 제목 설정

year_combobox = ttk.Combobox(root, height =10, values =year_list, state ="readonly")
year_combobox.set("연도를 선택하세요") # 최초 목록 제목 설정
year_combobox.grid(row=2, column=0)

accident_combobox = ttk.Combobox(root, height =10, values =accident_list, state ="readonly")
accident_combobox.set("사고유형를 선택하세요") # 최초 목록 제목 설정
accident_combobox.grid(row=3, column=0)


result_label = Label(root, text="")
result_label.grid(row=5,column=0)

def btncmd():
    if accident_combobox.get()=='음주운전':
        if year_combobox.get()=='2017':
            plt.rcParams['figure.figsize']=(12,9)
            plt.rc('font',family="Malgun Gothic")
            df_a=pd.read_csv('서울시 교통사고_a.csv',encoding='cp949')
            df1 = df_a.astype({'음주운전':'int32'})
            df1.plot.bar(x='자치구별', y='음주운전',rot=45)
            plt.show()
            result_label.config(text="구: {}\n연도: {} \n사고유형: {} ".format(seoul_combobox.get(), year_combobox.get(),accident_combobox.get()))
        if year_combobox.get()=='2020':
            plt.rcParams['figure.figsize']=(12,9)
            plt.rc('font',family="Malgun Gothic")
            df_a=pd.read_csv('서울시 교통사고_a.csv',encoding='cp949')
            df1 = df_a.astype({'음주운전.3':'int32'})
            df1.plot.bar(x='자치구별', y='음주운전',rot=45)
            plt.show()
            result_label.config(text="구: {}\n연도: {} \n사고유형: {} ".format(seoul_combobox.get(), year_combobox.get(),accident_combobox.get()))
        for i in range(1,3):
            if year_combobox.get()=='201'+str(i+7):
                plt.rcParams['figure.figsize']=(12,9)
                plt.rc('font',family="Malgun Gothic")
                df_a=pd.read_csv('서울시 교통사고_a.csv',encoding='cp949')
                df1 = df_a.astype({'음주운전.'+str(i)+'':'int32'})
                df1.plot.bar(x='자치구별', y='음주운전.1',rot=45)
                plt.show()
                result_label.config(text="구: {}\n연도: {} \n사고유형: {} ".format(seoul_combobox.get(), year_combobox.get(),accident_combobox.get()))
        for i in range(1,2):
            if year_combobox.get()=='202'+str(i):
                plt.rcParams['figure.figsize']=(12,9)
                plt.rc('font',family="Malgun Gothic")
                df_a=pd.read_csv('서울시 교통사고_a.csv',encoding='cp949')
                df1 = df_a.astype({'음주운전.'+str(i+3)+'':'int32'})
                df1.plot.bar(x='자치구별', y='음주운전.1',rot=45)
                plt.show()
                result_label.config(text="구: {}\n연도: {} \n사고유형: {} ".format(seoul_combobox.get(), year_combobox.get(),accident_combobox.get()))



btn = Button(root, text ="선택", command =btncmd)
btn.grid(row=4, column=0)

root.mainloop()