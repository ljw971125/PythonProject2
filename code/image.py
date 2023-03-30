from PIL import Image, ImageTk # 파이썬으로 이미지를 다룰 수 있게 해주는 모듈
import tkinter as tk # 인터페이스를 만들 때
import os

PATH = os.path.dirname(os.path.realpath(__file__)) # 현재 디렉토리로 이동
os.chdir(PATH)

class ImageViewer:
    def __init__(self, master, image_paths):
        self.master = master
        self.master.title("도움말")

        self.image_paths = image_paths
        self.current_index = 0

        self.image_label = tk.Label(self.master)
        self.image_label.pack()

        self.prev_button = tk.Button(master, text="<<", command=self.show_previous_image)
        self.prev_button.pack(side=tk.LEFT)

        self.next_button = tk.Button(master, text=">>", command=self.show_next_image)
        self.next_button.pack(side=tk.RIGHT)

        # 첫 번째 이미지에서는 이전 버튼을 비활성화
        self.prev_button.config(state=tk.DISABLED)

        self.show_image()

    def show_image(self):
        image_path = self.image_paths[self.current_index]
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo  # To prevent garbage collection

        if self.current_index == 0:
            self.prev_button.config(state=tk.DISABLED)
        else:
            self.prev_button.config(state=tk.NORMAL)

        if self.current_index == len(self.image_paths) - 1:
            self.next_button.config(state=tk.DISABLED)
        else:
            self.next_button.config(state=tk.NORMAL)

    def show_previous_image(self):
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = 0
        self.show_image()

    def show_next_image(self):
        self.current_index += 1
        if self.current_index >= len(self.image_paths):
            self.current_index = len(self.image_paths) - 1
        self.show_image()