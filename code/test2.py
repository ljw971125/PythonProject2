import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
import tkinter as tk

# 임의의 데이터프레임 생성
df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [2, 4, 6, 8]})

# 기본 윈도우 생성
root = tk.Tk()

# 버튼 클릭 시 실행될 함수 정의
def show_plot():
    # 새 프레임 생성
    new_frame = tk.Frame(root)
    new_frame.grid(row=0, column=1)

    # 그래프 그리기 위한 figure와 axes 객체 생성
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    # 판다스 plot 메소드에 axes 객체 전달
    df.plot(x='x', y='y', ax=ax)

    # 새 프레임에 그래프 임베딩하기
    canvas = FigureCanvasTkAgg(fig, master=new_frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0)

# 버튼 생성 및 배치
button = tk.Button(root, text="Show plot", command=show_plot)
button.grid(row=0, column=0)

root.mainloop()