from tkinter import *
import tkinter as tk # 인터페이스를 만들 때
import csv # csv 파일을 불러올 때 사용합니다
import os 
from PIL import Image, ImageTk

PATH = os.path.dirname(os.path.realpath(__file__)) # 현재 디렉토리로 이동
os.chdir(PATH)

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Start page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go to page one",
                  command=lambda: master.switch_frame(PageOne)).pack()

class PageOne(tk.Frame):
    def __init__(self, master):
        f = open('서울시.csv') # csv 파일을 불러오기
        reader = csv.reader(f) 
        data = [row[2] for row in reader] #csv 파일에서 2열부터의 값을 가져오기

        window = tk.Tk() 
        #photo = ImageTk.PhotoImage(Image.open('car.png')) # ui 아이콘 불러오기
        #window.wm_iconphoto(False, photo) # ui 아이콘 적용하기
        window.title("서울시 사고유형 분석") # ui 제목
        window.geometry("870x450") # ui 크기
        #window.resizable(True,True)

        var = StringVar()
        var.set("1")

        # 프레임 생성
        frame1 = tk.Frame(window)
        frame2 = tk.Frame(window) # 프레임 생성
        frame3 = tk.Frame(window)

        frame1.pack(fill=BOTH)  
        frame2.pack(side=LEFT) # 프레임을 왼쪽 정렬
        frame3.pack(side=RIGHT)


        scrollbar = Scrollbar(frame2) # 스크롤바 생성
        scrollbar.pack(side=RIGHT, fill=Y) # 스크롤바를 프레임의 오른쪽에 붙임


        mylist = Listbox(frame2, yscrollcommand=scrollbar.set, height=0, selectbackground='pink', selectforeground='black') # 리스트바 생성, 스크롤바 연결, 높이 0으로 설정
        for data in data[3:]: # csv 파일의 3행부터 불러옴
            mylist.insert(tk.END, data)
        mylist.pack(side=LEFT) # 리스트바를 프레임의 왼쪽에 붙임

        R1 = Radiobutton(frame3, text='음주운전',variable=var, value="1",command=selection) # 오른쪽 프레임 체크박스 추가
        R1.pack(anchor='w') # 왼쪽으로 정렬
        R2 = Radiobutton(frame3, text='무면허',variable=var, value="2",command=selection)
        R2.pack(anchor='w')
        R3 = Radiobutton(frame3, text='스쿨존',variable=var, value="3",command=selection)
        R3.pack(anchor='w')
        R4 = Radiobutton(frame3, text='과속',variable=var, value="4",command=selection)
        R4.pack(anchor='w')
        R5 = Radiobutton(frame3, text='신호위반',variable=var, value="5",command=selection)
        R5.pack(anchor='w')

        bt=tk.Button(frame1,text="버튼1",width=40,height=4)
        bt.pack(side=LEFT,expand=True,fill=BOTH)
        bt2=tk.Button(frame1,text="버튼2",width=40,height=4)
        bt2.pack(side=LEFT,expand=True,fill=BOTH)
        bt3=tk.Button(frame1,text="버튼3",width=40,height=4)
        bt3.pack(side=LEFT,expand=True,fill=BOTH)

        # 레이블 생성
        def selection():
            label.config(text="You selected " + var.get())
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

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()