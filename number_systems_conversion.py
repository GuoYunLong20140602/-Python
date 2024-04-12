import json
import tkinter as tk
from tkinter import messagebox, ttk

import pyperclip as pc


class NumberSystemConversion:
    def __init__(self):
        with open(r"./calc_settings.json", encoding="utf-8") as f:
            settings = json.load(f)

        root = tk.Tk()
        root.geometry("300x300+50+50")
        root.title("计算器v6.0-进制转换")

        def on_select_change1(event):
            global value1
            value = system_number.get()

        def on_select_change2(event):
            global value2
            value = to_system_number.get()

        res = '0'

        def process():
            global res
            if system_number.get() == "二进制":
                res = int(sne.get(), 2)
                if to_system_number.get() == "二进制":
                    messagebox.showerror("计算器v6.0-错误", "请勿将二进制转换为二进制")
                elif to_system_number.get() == "八进制":
                    res = oct(res)
                    messagebox.showinfo("计算器v6.0-结果", f"{res}")
                elif to_system_number.get() == "十进制":
                    messagebox.showinfo("计算器v6.0-结果", f"{res}")
                elif to_system_number.get() == "十六进制":
                    res = hex(res)
                    messagebox.showinfo("计算器v6.0-结果", f"{res}")
            elif system_number.get() == "八进制":
                res = int(sne.get(), 8)
                if to_system_number.get() == "八进制":
                    messagebox.showerror("计算器v6.0-错误", "请勿将八进制转换为八进制")
                elif to_system_number.get() == "二进制":
                    res = bin(res)
                    messagebox.showinfo("计算器v6.0-结果", f"{res}")
                elif to_system_number.get() == "十进制":
                    messagebox.showinfo("计算器v6.0-结果", f"{res}")
                elif to_system_number.get() == "十六进制":
                    res = hex(res)
                    messagebox.showinfo("计算器v6.0-结果", f"{res}")

            elif system_number.get() == "十进制":
                res = int(sne.get(), 10)
                if to_system_number.get() == "十进制":
                    messagebox.showerror("计算器v6.0-错误", "请勿将十进制转换为十进制")
                elif to_system_number.get() == "二进制":
                    res = bin(res)
                    messagebox.showinfo("计算器v6.0-结果", f"{res}")
                elif to_system_number.get() == "八进制":
                    res = oct(res)
                    messagebox.showinfo("计算器v6.0-结果", f"{res}")
                elif to_system_number.get() == "十六进制":
                    res = hex(res)
                    messagebox.showinfo("计算器v6.0-结果", f"{res}")
            else:
                res = int(sne.get(), 16)
                if to_system_number.get() == "十六进制":
                    messagebox.showerror("计算器v6.0-错误", "请勿将十六进制转换为十六进制")
                elif to_system_number.get() == "二进制":
                    res = bin(res)
                    messagebox.showinfo("计算器v6.0-结果", f"{res}")
                elif to_system_number.get() == "八进制":
                    res = oct(res)
                    messagebox.showinfo("计算器v6.0-结果", f"{res}")
                elif to_system_number.get() == "十进制":
                    messagebox.showinfo("计算器v6.0-结果", f"{res}")
            return res
        system_number = ttk.Combobox(
            root, font=(settings["expression-font"], settings["expression-font-size"]))
        to_system_number = ttk.Combobox(
            root, font=(settings["expression-font"], settings["expression-font-size"]))
        root.option_add("*TCombobox*Listbox.font", "Arial 20")
        root.config(bg=settings["bg"])

        system_number["values"] = ("二进制", "八进制", "十进制", "十六进制")  # 设置下拉框的选项
        var1 = tk.StringVar()
        var1.set(0)
        sne = tk.Entry(
            root,
            font=(settings["expression-font"], settings["expression-font-size"]),
            textvariable=var1,
        )

        to_system_number["values"] = ("二进制", "八进制", "十进制", "十六进制")  # 设置下拉框的选项
        system_number.current(0)
        to_system_number.current(0)
        system_number.bind("<<ComboboxSelected>>", on_select_change1)  # 绑定事件，当选项变更时触发
        to_system_number.bind(
            "<<ComboboxSelected>>", on_select_change2
        )  # 绑定事件，当选项变更时触发

        system_number.pack()
        sne.pack()
        to_system_number.pack()
        button = tk.Button(
            root,
            font=(settings["expression-font"], settings["expression-font-size"]),
            text="转换",
            command=process,
        )

        button.pack()
        root.mainloop()


if __name__ == "__main__":
    NumberSystemConversion()
