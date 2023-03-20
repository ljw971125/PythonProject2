from tkinter import *
import tkinter # 인터페이스를 만들 때
import csv # csv 파일을 불러올 때 사용합니다
import os 

PATH = os.path.dirname(os.path.realpath(__file__))
os.chdir(PATH)

f = open('서울시 구별건.csv')
reader = csv.reader(f)
data = [row[1] for row in reader]

window = tkinter.Tk()
window.title("지역별 교통사고 현황")
window.geometry("300x200")

# 프레임 생성
frame = tkinter.Frame(window)
frame.pack(side=LEFT)

scrollbar = Scrollbar(frame) # 스크롤바 생성
scrollbar.pack(side=RIGHT, fill=Y) # 스크롤바를 프레임의 오른쪽에 붙임

mylist = Listbox(frame, yscrollcommand=scrollbar.set, height=0) # 리스트바 생성, 스크롤바 연결, 높이 0으로 설정
for data in data[3:]:
    mylist.insert(tkinter.END, data)
mylist.pack(side=LEFT) # 리스트바를 프레임의 왼쪽에 붙임

# 레이블 생성
label = tkinter.Label(window)
label.pack()

# 콜백 함수 정의
def show_info(event):
    # 선택된 항목의 인덱스와 정보를 레이블에 표시
    index = mylist.curselection()[0]
    info = mylist.get(index)
    label.config(text=f"선택한 지역: {info}")

# 리스트박스에 콜백 함수 연결
mylist.bind("<<ListboxSelect>>", show_info)

window.mainloop()