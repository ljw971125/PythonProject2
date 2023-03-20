from tkinter import *
import tkinter as tk # 인터페이스를 만들 때
import csv # csv 파일을 불러올 때 사용합니다
import os 
from PIL import Image, ImageTk

PATH = os.path.dirname(os.path.realpath(__file__)) # 현재 디렉토리로 이동
os.chdir(PATH)
print(PATH)
icon = "car.png"


f = open('서울시.csv') # csv 파일을 불러오기
reader = csv.reader(f) 
data = [row[2] for row in reader] #csv 파일에서 2열부터의 값을 가져오기

window = tk.Tk() 
photo = ImageTk.PhotoImage(Image.open(icon)) # ui 아이콘 불러오기
window.wm_iconphoto(False, photo) # ui 아이콘 적용하기
window.title("서울시 사고유형 분석") # ui 제목
window.geometry("900x500") # ui 크기

# 프레임 생성
frame = tk.Frame(window)
frame.pack(side=LEFT) # 프레임을 왼쪽 정렬

scrollbar = Scrollbar(frame) # 스크롤바 생성
scrollbar.pack(side=RIGHT, fill=Y) # 스크롤바를 프레임의 오른쪽에 붙임

mylist = Listbox(frame, yscrollcommand=scrollbar.set, height=0) # 리스트바 생성, 스크롤바 연결, 높이 0으로 설정
for data in data[3:]: # csv 파일의 3행부터 불러옴
    mylist.insert(tk.END, data)
mylist.pack(side=LEFT) # 리스트바를 프레임의 왼쪽에 붙임

# 레이블 생성
label = tk.Label(window)
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