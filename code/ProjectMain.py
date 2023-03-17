from tkinter import *
import tkinter

root = Tk()

frame = Frame(root) # 프레임 생성
frame.pack(side=LEFT) # 프레임을 윈도우에 배치

scrollbar = Scrollbar(frame) # 스크롤바 생성
scrollbar.pack(side=RIGHT, fill=Y) # 스크롤바를 프레임의 오른쪽에 붙임

districts = ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로 구','금천 구',
             '노원 구','도봉 구','동대문 구','동작 구','마포 구','서대문 구','서초 구',
             '성동 구','성북 구','송파 구','양천 구','영등포 구','용산 구','은평 구',
             '종로 구','중 구','중랑 구']

mylist = Listbox(frame, yscrollcommand=scrollbar.set, height=0) # 리스트바 생성, 스크롤바 연결, 높이 0으로 설정
for district in districts:
    mylist.insert(tkinter.END, district)
mylist.pack(side=LEFT) # 리스트바를 프레임의 왼쪽에 붙임

scrollbar.config(command=mylist.yview) # 스크롤바에 리스트바의 y축 이동을 연결

mainloop()