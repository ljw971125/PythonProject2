import tkinter.ttk as ttk
from tkinter import *
import csv
import os

PATH = os.path.dirname(os.path.realpath(__file__)) #현재 경로로 불러옴
os.chdir(PATH)

f = open('서울시 구별건.csv')
data=csv.reader(f)
next(data)
next(data)
next(data)
seoul_list=[]
year_list=['2017','2018','2019','2020','2021']
for row in data:
    seoul_list.append(row[1])
#print(seoul_list)


root =Tk()
root.title(" GUI")
root.geometry("640x480")


seoul_combobox = ttk.Combobox(root, height =5, values =seoul_list)
seoul_combobox.place(x=3, y= 240)
seoul_combobox.set("구를 선택하세요") # 최초 목록 제목 설정



year_combobox = ttk.Combobox(root, height =10, values =year_list, state ="readonly")
year_combobox.set("연도를 선택하세요") # 최초 목록 제목 설정
year_combobox.pack()




def btncmd():
    data_1 = 0
    f=open('서울시 구별건.csv',encoding='cp949')
    data=csv.reader(f)
    next(data)
    next(data)
    next(data)

    for row in data:
        if row[1] == seoul_combobox.get():

            test = row[-2009+int(year_combobox.get())]

    print(seoul_combobox.get())
    print(year_combobox.get())

    # 수정된 부분
    print(test)
    f.close()



btn = Button(root, text ="선택", command =btncmd)
btn.pack()

root.mainloop()
f.close()