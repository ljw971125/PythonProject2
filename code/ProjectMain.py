from tkinter import *
import tkinter
import csv
import os
PATH = os.path.dirname(os.path.realpath(__file__))
os.chdir(PATH)

f = open('서울시 구별건.csv')
reader = csv.reader(f)
data = [row[1] for row in reader]

root = Tk()

frame = Frame(root) # 프레임 생성
frame.pack(side=LEFT) # 프레임을 윈도우에 배치

scrollbar = Scrollbar(frame) # 스크롤바 생성
scrollbar.pack(side=RIGHT, fill=Y) # 스크롤바를 프레임의 오른쪽에 붙임


mylist = Listbox(frame, yscrollcommand=scrollbar.set, height=0) # 리스트바 생성, 스크롤바 연결, 높이 0으로 설정
for data in data[3:]:
    mylist.insert(tkinter.END, data)
mylist.pack(side=LEFT) # 리스트바를 프레임의 왼쪽에 붙임

scrollbar.config(command=mylist.yview) # 스크롤바에 리스트바의 y축 이동을 연결

mainloop()