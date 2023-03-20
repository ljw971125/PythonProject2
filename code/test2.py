# 필요한 모듈 임포트
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 샘플 데이터프레임 생성
data = {
    "Year": [2010, 2011, 2012, 2013, 2014],
    "Sales": [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)

# 메인 윈도우 생성
win = tk.Tk()

# 그래프를 그릴 피규어 객체 생성
figure = plt.Figure(figsize=(5, 4), dpi=100)

# 피규어에 서브플롯 추가
ax = figure.add_subplot(111)

# 데이터프레임으로 선 그래프 그리기
df.plot(kind="line", x="Year", y="Sales", ax=ax)

# 피규어를 캔버스에 연결하기
canvas = FigureCanvasTkAgg(figure, win)

# 캔버스를 윈도우에 배치하기
canvas.get_tk_widget().pack()

# 메인 루프 실행
win.mainloop()