from tkinter import *
import tkinter as tk # 인터페이스를 만들 때
import os # 운영체제와 상호 작용을 하기 위한 모듈
from PIL import Image, ImageTk # 파이썬으로 이미지를 다룰 수 있게 해주는 모듈
import pandas as pd # 데이터 프레임을 만들 수 있는 모듈
import sys # 파이썬의 인터프리터를 제어할 수 있는 모듈
import allmenu

PATH = os.path.dirname(os.path.realpath(__file__)) # 현재 디렉토리로 이동
os.chdir(PATH)

# Ui 정의

class Accident(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None # 현재 프레임을 None으로 초기화
        self.switch_frame(allmenu.StartMenu) # StartMenu 프레임으로 전환
        self.title("서울시 사고유형 분석") # ui 제목
        self.geometry("1200x700") # ui 시작 해상도
        photo = ImageTk.PhotoImage(Image.open('car.png')) # ui 아이콘 불러오기
        self.wm_iconphoto(False, photo) # ui 아이콘 적용하기

    # 프레임 이동 함수
    def switch_frame(self, frame_class): 
        new_frame = frame_class(self)
        if self._frame is not None: # 프레임이 비어 있지 않을 때
            self._frame.destroy() # 프레임을 비움
        self._frame = new_frame
        self._frame.pack() # pack 메소드는 프레임의 크기와 위치를 자동으로 조절하여 윈도우에 적절하게 맞춤

    # 프레임을 지우는 함수
    def del_frame(self):
        for widget in self.winfo_children(): # 윈도우의 모든 자식 위젯을 지움
            widget.destroy()


if __name__ == "__main__":
    app = Accident()
    app.mainloop() # Ui를 윈도우 창을 띄어 표시