import json
import tkinter as tk
from tkinter import messagebox

import pyperclip as pc


class BMIJudge:
    def __init__(self):
        with open(
            r"C:\Users\Administrator\Desktop\Projects\实战\Python\tkinter库\计算器0-07\calc_settings.json",
            "r",
            encoding="utf-8",
        ) as f:  # 读取json文件内容，并转换为字典格式。
            settings = json.load(f)  # 读取json文件内容，并转换为字典格式。
        root = tk.Tk()  # 创建tkinter窗口。
        root.geometry("500x200")  # 设置窗口大小。
        root.title("计算器7.0-BMI判断器")  # 设置窗口标题。
        self.bmi = 0
        self.index = "未知"
        tk.Label(
            root,
            font=(settings["expression-font"], settings["expression-font-size"]),
            text="请输入您的BMI:",
        ).grid(
            column=1, row=1
        )  # 创建标签。
        bmi_entry = tk.Entry(
            root,
            font=(settings["expression-font"], settings["expression-font-size"]),
            width=20,
        )  # 创建输入框。
        bmi_entry.grid(column=2, row=1)  # 设置输入框位置。

        def judge():
            try:
                self.bmi = float(bmi_entry.get())  # 获取输入框内容。
            except:
                messagebox.showerror("计算器v7.0-BMI判断器-报错", "请输入正确的BMI值！")  # 弹出错误提示框。
            else:
                if self.bmi < 18.5:  # 判断BMI值是否小于18.5。
                    messagebox.showinfo(
                        "计算器v7.0-BMI判断器-结果", "您的BMI值为：" + str(self.bmi) + "，体重过轻！"
                    )  # 弹出提示框。
                    self.index = "过轻"  # 设置index变量值为'过轻'。
                elif 18.5 <= self.bmi < 24:  # 判断BMI值是否在18.5和24之间。
                    messagebox.showinfo(
                        "计算器v7.0-BMI判断器-结果", "您的BMI值为：" + str(self.bmi) + "，体重正常！"
                    )  # 弹出提示框。
                    self.index = "正常"  # 设置index变量值为'正常'。
                elif 24 <= self.bmi < 27:  # 判断BMI值是否在24和28之间。
                    messagebox.showinfo(
                        "计算器v7.0-BMI判断器-结果", "您的BMI值为：" + str(self.bmi) + "，体重过重！"
                    )  # 弹出提示框。
                    self.index = "过重"  # 设置index变量值为'过重'。
                elif 27 <= self.bmi < 30:  # 判断BMI值是否在27和30之间。
                    messagebox.showinfo(
                        "计算器v7.0-BMI判断器-结果", "您的BMI值为：" + str(self.bmi) + "，体重一度肥胖！"
                    )  # 弹出提示框。
                    self.index = "一度肥胖"  # 设置index变量值为'一度肥胖'。
                elif 30 <= self.bmi < 35:  # 判断BMI值是否在30和35之间。
                    messagebox.showinfo(
                        "计算器v7.0-BMI判断器-结果", "您的BMI值为：" + str(self.bmi) + "，体重二度肥胖！"
                    )  # 弹出提示框。
                    self.index = "二度肥胖"  # 设置index变量值为'二度肥胖'。
                else:  # 判断BMI值是否大于等于35。
                    messagebox.showinfo(
                        "计算器v7.0-BMI判断器-结果", "您的BMI值为：" + str(self.bmi) + "，体重三度肥胖！"
                    )  # 弹出提示框。
                    self.index = "三度肥胖"  # 设置index变量值为'三度肥胖'。

        def copy_index():  # 创建复制函数。
            pc.copy(self.index)

        judge_button = tk.Button(
            root,
            text="判断",
            command=judge,
            font=(settings["expression-font"], settings["expression-font-size"]),
        )  # 创建按钮。
        judge_button.grid(column=1, row=2)  # 设置按钮位置。
        copy_button = tk.Button(
            root,
            text="复制结果",
            command=copy_index,
            font=(settings["expression-font"], settings["expression-font-size"]),
        )  # 创建按钮。
        copy_button.grid(column=2, row=2)  # 设置按钮位置。
        root.mainloop()


if __name__ == "__main__":  # 判断是否为主程序。
    BMIJudge()  # 创建BMIJudge对象。
