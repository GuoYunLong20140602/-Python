import json
import tkinter as tk
from tkinter import messagebox

import pyperclip as pc


class BMICalc:
    def __init__(self):
        with open(
            r"C:\Users\Administrator\Desktop\Projects\实战\Python\tkinter库\计算器0-07\calc_settings.json",
            encoding="utf-8",
        ) as f:  # 读取settings.json文件。
            settings = json.load(f)
        root = tk.Tk()
        root.geometry("500x300")  # 设置窗口大小为300x100像素。
        root.title("计算器v7.0-BMI计算器")
        height = 0
        weight = 0
        self.ans = 0

        # BMI计算公式
        # BMI = 体重(kg) / (身高(m) * 身高(m))
        tk.Label(
            root,
            text="请输入身高（m）：",
            font=(settings["expression-font"], settings["expression-font-size"]),
        ).grid(column=1, row=1)
        tk.Label(
            root,
            text="请输入体重（kg）：",
            font=(settings["expression-font"], settings["expression-font-size"]),
        ).grid(
            column=1, row=2
        )  # 设置标签的位置。
        height_entry = tk.Entry(
            root,
            width=10,
            font=(settings["expression-font"], settings["expression-font-size"]),
        )  # 身高输入框。
        height_entry.grid(column=2, row=1)  # 设置身高输入框的位置。
        weight_entry = tk.Entry(
            root,
            width=10,
            font=(settings["expression-font"], settings["expression-font-size"]),
        )  # 体重输入框。
        weight_entry.grid(column=2, row=2)  # 设置体重输入框的位置。

        def get_height():  # 定义get_height函数，用于获取身高输入框的值。
            # global height  # 声明全局变量height。
            try:
                height = float(height_entry.get())  # 获取身高输入框的值。
                return height
            except:
                messagebox.showerror("计算器7.0-BMI计算器-报错", "身高输入错误，请输入数字！")  # 弹出错误提示框。

        def get_weight():  # 定义get_weight函数，用于获取体重输入框的值。
            # global weight  # 声明全局变量weight。
            try:
                weight = float(weight_entry.get())  # 获取体重输入框的值。
                return weight
            except:
                messagebox.showerror("计算器7.0-BMI计算器-报错", "体重输入错误，请输入数字！")  # 弹出错误提示框。

        def calculate():  # 定义calculate函数，用于计算BMI值。
            global height, weight  # 声明全局变量height和weight。
            height = get_height()  # 获取身高输入框的值。
            weight = get_weight()  # 获取体重输入框的值。

            if settings["float-bit"] == "0":
                r = round(float(weight) / (float(height) ** 2), 0)  # 计算BMI值，保留0位小数。
            elif settings["float-bit"] == "1":
                r = round(float(weight) / (float(height) ** 2), 1)  # 计算BMI值，保留1位小数。
            elif settings["float-bit"] == "2":
                r = round(float(weight) / (float(height) ** 2), 2)  # 计算BMI值，保留2位小数。
            elif settings["float-bit"] == "3":
                r = round(float(weight) / (float(height) ** 2), 3)  # 计算BMI值，保留3位小数。
            elif settings["float-bit"] == "4":
                r = round(float(weight) / (float(height) ** 2), 4)  # 计算BMI值，保留4位小数。
            elif settings["float-bit"] == "5":
                r = round(float(weight) / (float(height) ** 2), 5)  # 计算BMI值，保留5位小数。
            else:
                r = float(weight) / (float(height) ** 2)  # 计算BMI值，不保留小数。
            self.ans = r  # 保存BMI值。
            # return self.ans
            messagebox.showinfo("计算器7.0-BMI计算器-结果", str(self.ans))

        def copy_bmi():
            print(self.ans)

            pc.copy(self.ans)  # 复制BMI值到剪贴板。
            messagebox.showinfo("计算器7.0-BMI计算器-提示", "已复制到剪贴板。")

        tk.Button(
            root,
            text="计算",
            command=calculate,
            font=(settings["expression-font"], settings["expression-font-size"]),
        ).grid(
            column=2, row=3
        )  # 计算按钮，点击后执行calculate函数。
        tk.Button(
            root,
            font=(settings["expression-font"], settings["expression-font-size"]),
            text="复制",
            command=copy_bmi,
        ).grid(column=1, row=3)

        root.mainloop()


if __name__ == "__main__":
    BMICalc()
