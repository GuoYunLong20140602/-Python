# 相关代码已经开源到GitHub, 请访问https://github.com/Guo-https://github.com/GuoYunLong20140602/-Python/tree/main
# 需要安装pyperclip 安装方法:pip install pyperclip
"""七代版本的计算器，v7.0"""
# 导入tkinter, math, pyperclip, json 和 tkinter.messagebox
import json
import math
import tkinter as tk
from tkinter import messagebox

import pyperclip as pc

import bmi_calc
import bmi_judge
import number_systems_conversion
import settings

results = [0, 0]
res = 0
res1 = results[-2]
history = []
memory = 0

with open(
    r"C:\Users\Administrator\Desktop\Projects\实战\Python\tkinter库\计算器0-07\calc_settings.json",
    encoding="UTF-8",
) as f:
    settings_dict = json.load(f)
    # print(settings_dict)


class History:
    def __init__(self) -> None:
        self.history = history

    def show_history(self):
        h = "\n".join(self.history)
        messagebox.showinfo("计算器-历史记录v7.0", f"{h}")


class Commands:
    def __init__(self, box):
        self.input_expression = box

    def about_author(self):
        messagebox.showinfo("计算器6.0-关于作者", "作者:郭芸龙")

    def write_one(self):
        self.input_expression.insert("insert", "1")

    def write_two(self):
        self.input_expression.insert("insert", "2")

    def write_three(self):
        self.input_expression.insert("insert", "3")

    def write_four(self):
        self.input_expression.insert("insert", "4")

    def write_five(self):
        self.input_expression.insert("insert", "5")

    def write_six(self):
        self.input_expression.insert("insert", "6")

    def write_seven(self):
        self.input_expression.insert("insert", "7")

    def write_eight(self):
        self.input_expression.insert("insert", "8")

    def write_nine(self):
        self.input_expression.insert("insert", "9")

    def write_zero(self):
        self.input_expression.insert("insert", "0")

    def write_zero_zero(self):
        self.input_expression.insert("insert", "00")

    def write_add(self):
        self.input_expression.insert("insert", "+")

    def write_dot(self):
        self.input_expression.insert("insert", ".")

    def write_subtraction(self):
        self.input_expression.insert("insert", "-")

    def write_multiplication(self):
        self.input_expression.insert("insert", "×")

    def write_division(self):
        self.input_expression.insert("insert", "÷")

    def clear(self):
        self.input_expression.delete(0, tk.END)

    def delete(self):
        self.input_expression.delete(len(self.input_expression.get()) - 1)

    def Sqrt(self):
        self.input_expression.insert("insert", "√()")

    def Sin(self):
        self.input_expression.insert("insert", "sin()")

    def Cos(self):
        self.input_expression.insert("insert", "cos()")

    def Tan(self):
        self.input_expression.insert("insert", "tan()")

    def write_e(self):
        self.input_expression.insert("insert", "e")

    def write_pi(self):
        self.input_expression.insert("insert", "π")

    def write_power(self):
        self.input_expression.insert("insert", "^")

    def write_left_parenthesis(self):
        self.input_expression.insert("insert", "(")

    def write_factorial(self):
        self.input_expression.insert("insert", "!()")

    def write_right_parenthesis(self):
        self.input_expression.insert("insert", ")")

    def plus_or_minus(self):
        if len(self.input_expression.get()) >= 1:
            if self.input_expression.get()[0] == "-":
                self.input_expression.delete(0)
            else:
                self.input_expression.insert(0, "-")
        else:
            messagebox.showerror("计算器-报错v7.0", f"对不起, 您输入的表达式有错误, 请重新输入")

    def write_eq_eq(self):
        self.input_expression.insert("insert", "==")

    def write_greater_than_sign(self):
        self.input_expression.insert("insert", ">")

    def write_greater_than_or_equal(self):
        self.input_expression.insert("insert", "≥")

    def write_less_than_or_equal(self):
        self.input_expression.insert("insert", "≤")

    def write_less_than(self):
        self.input_expression.insert("insert", "<")

    def write_unequal(self):
        self.input_expression.insert("insert", "≠")

    def memory_plus(self):
        global memory
        try:
            memory += float(self.input_expression.get())
        except:
            messagebox.showerror("计算器-报错v7.0", f"对不起, 您输入的表达式有错误, 请重新输入")

    def memory_minus(self):
        global memory
        try:
            memory -= float(self.input_expression.get())
        except:
            messagebox.showerror("计算器-报错v7.0", f"对不起, 您输入的表达式有错误, 请重新输入")

    def memory_clear(self):
        global memory

        memory = 0

    def memory_read(self):
        self.input_expression.insert("insert", memory)

    def write_result(self):
        global res, res1
        try:
            res = expression_display.get()
            res = res.replace("×", "*")
            res = res.replace("÷", "/")
            res = res.replace("^", "**")
            res = res.replace("√", "sqrt")
            res = res.replace("!", "factorial")
            res = res.replace("≥", ">=")
            res = res.replace("≤", "<=")
            res = res.replace("≠", "!=")
            res0 = res
            # print(res)
            res = eval(res)
            results.append(res)
            if len(results) == 3:
                results.pop(0)
            res1 = results[-2]

            a = settings_dict["float-bit"]
            if a == "0":
                messagebox.showinfo("计算器-结果v7.0", f"{int(res)}")
                print(f"{int(res)}")
            elif a == "1":
                messagebox.showinfo("计算器-结果v7.0", f"{res:.1f}")
                print(f"{res:.1f}")
            elif a == "2":
                messagebox.showinfo("计算器-结果v7.0", f"{res:.2f}")
                print(f"{res:.2f}")
            elif a == "3":
                messagebox.showinfo("计算器-结果v7.0", f"{res:.3f}")
                print(f"{res:.3f}")
            elif a == "4":
                messagebox.showinfo("计算器-结果v7.0", f"{res:.4f}")
                print(f"{res:.4f}")
            elif a == "5":
                messagebox.showinfo("计算器-结果v7.0", f"{res:.5f}")
                print(f"{res:.5f}")
            else:
                messagebox.showinfo("计算器-结果v7.0", f"{res}")
                print(f"{res}")

            # 将计算结果添加到历史记录列表中
            history.append(f"{res0}:{res}")

        except:
            messagebox.showerror("计算器-报错v7.0", f"对不起, 您输入的表达式有错误, 请重新输入")
        else:
            pass

    def cut(self):
        # 获取全部的文本内容
        selected_text = self.input_expression.get()

        # 删除所有的文本
        self.input_expression.delete(0, tk.END)

        # copy
        pc.copy(selected_text)

    def copy(self):
        # self.input_expression.event_generate("<<Copy>>")
        pc.copy(self.input_expression.get())

    def paste(self):
        # self.input_expression.event_generate("<<Paste>>")
        n = pc.paste()
        self.input_expression.insert("insert", n)

    def copy_last_res(self):
        pc.copy(res1)

    def answer_copy(self):
        pc.copy(res)

    def open_settings(self):
        settings.Settings()

    def open_number_systems_conversion(self):
        number_systems_conversion.NumberSystemConversion()

    def open_bmi_calc(self):
        bmi_calc.BMICalc()
        
    def open_bmi_judge(self):
        bmi_judge.BMIJudge()


# 创建窗口
root = tk.Tk()

# 设置窗口
root.geometry("700x450")
root.title("计算器v7.0")
# 变量


expression = tk.StringVar()
expression_display = tk.Entry(
    root,
    textvariable=expression,
    width=64,
    font=(settings_dict["expression-font"], settings_dict["expression-font-size"]),
    fg=settings_dict["expression-fg"],
)
expression_display.place(x=0, y=10)
sqrt = math.sqrt

cos = math.cos
sin = math.sin
tan = math.tan
commands = Commands(expression_display)
e = math.e
π = math.pi

# 菜单栏
menu_bar = tk.Menu(root)
# 文件栏
File_bar = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="文件", menu=File_bar)
File_bar.add_command(label="打开设置文件", command=commands.open_settings)
File_bar.add_command(label="打开进制转换器", command=commands.open_number_systems_conversion)
File_bar.add_command(label="打开BMI计算器", command=commands.open_bmi_calc)
File_bar.add_command(label="打开BMI判断器", command=commands.open_bmi_judge)
File_bar.add_separator()
File_bar.add_command(label="退出", command=root.quit)


# 编辑栏
Edit_bar = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="编辑", menu=Edit_bar)
Edit_bar.add_command(label="记忆加", command=commands.memory_plus)
Edit_bar.add_command(label="记忆减", command=commands.memory_minus)
Edit_bar.add_command(label="记忆清空", command=commands.memory_clear)
Edit_bar.add_command(label="记忆读取", command=commands.memory_read)
Edit_bar.add_command(label="复制算式", command=commands.copy)
Edit_bar.add_command(label="剪切算式", command=commands.cut)
Edit_bar.add_command(label="粘贴算式", command=commands.paste)
Edit_bar.add_command(label="复制结果", command=commands.answer_copy)
Edit_bar.add_command(label="复制上一次的结果", command=commands.copy_last_res)


# 帮助栏
Help_bar = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="帮助", menu=Help_bar)
Help_bar.add_command(label="关于作者", command=commands.about_author)
Help_bar.add_command(label="历史记录", command=History().show_history)


def factorial(num: int):
    res = 1
    for i in range(1, num + 1):
        res *= i
    return res


OneButton = tk.Button(
    root,
    text="1",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_one,
    bg=settings_dict["button-bg"],
)
TwoButton = tk.Button(
    root,
    text="2",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_two,
    bg=settings_dict["button-bg"],
)
ThreeButton = tk.Button(
    root,
    text="3",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_three,
    bg=settings_dict["button-bg"],
)
FourButton = tk.Button(
    root,
    text="4",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_four,
    bg=settings_dict["button-bg"],
)
FiveButton = tk.Button(
    root,
    text="5",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_five,
    bg=settings_dict["button-bg"],
)
SixButton = tk.Button(
    root,
    text="6",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_six,
    bg=settings_dict["button-bg"],
)
SevenButton = tk.Button(
    root,
    text="7",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_seven,
    bg=settings_dict["button-bg"],
)
EightButton = tk.Button(
    root,
    text="8",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_eight,
    bg=settings_dict["button-bg"],
)
NineButton = tk.Button(
    root,
    text="9",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_nine,
    bg=settings_dict["button-bg"],
)
ZeroButton = tk.Button(
    root,
    text="0",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_zero,
    bg=settings_dict["button-bg"],
)
ZeroZeroButton = tk.Button(
    root,
    text="00",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_zero_zero,
    bg=settings_dict["button-bg"],
)
DotButton = tk.Button(
    root,
    text=".",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_dot,
    bg=settings_dict["button-bg"],
)
AddButton = tk.Button(
    root,
    text="＋",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_add,
    bg=settings_dict["button-bg"],
)
SubtractionButton = tk.Button(
    root,
    text="－",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_subtraction,
    bg=settings_dict["button-bg"],
)
MultiplicationButton = tk.Button(
    root,
    text="×",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_multiplication,
    bg=settings_dict["button-bg"],
)
DivisionButton = tk.Button(
    root,
    text="÷",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_division,
    bg=settings_dict["button-bg"],
)
EqualButton = tk.Button(
    root,
    text="=",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_result,
    bg=settings_dict["button-bg"],
)

PowerButton = tk.Button(
    root,
    text="xⁿ",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_power,
    bg=settings_dict["button-bg"],
)
SqrtButton = tk.Button(
    root,
    text="√",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.Sqrt,
    bg=settings_dict["button-bg"],
)
SinButton = tk.Button(
    root,
    text="sin",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.Sin,
    bg=settings_dict["button-bg"],
)
CosButton = tk.Button(
    root,
    text="cos",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.Cos,
    bg=settings_dict["button-bg"],
)
TanButton = tk.Button(
    root,
    text="tan",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.Tan,
    bg=settings_dict["button-bg"],
)
PiButton = tk.Button(
    root,
    text="π",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_pi,
    bg=settings_dict["button-bg"],
)
EButton = tk.Button(
    root,
    text="e",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_e,
    bg=settings_dict["button-bg"],
)
LeftParenthesisButton = tk.Button(
    root,
    text="(",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_left_parenthesis,
    bg=settings_dict["button-bg"],
)
RightParenthesisButton = tk.Button(
    root,
    text=")",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_right_parenthesis,
    bg=settings_dict["button-bg"],
)
PlusOrMinus = tk.Button(
    root,
    text="+/-",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.plus_or_minus,
    bg=settings_dict["button-bg"],
)
EqEq = tk.Button(
    root,
    text="==",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_eq_eq,
    bg=settings_dict["button-bg"],
)
less_than = tk.Button(
    root,
    text="<",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_less_than,
    bg=settings_dict["button-bg"],
)
less_than_eq = tk.Button(
    root,
    text="≤",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_less_than_or_equal,
    bg=settings_dict["button-bg"],
)
greater_than_eq = tk.Button(
    root,
    text="≥",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_greater_than_or_equal,
    bg=settings_dict["button-bg"],
)
greater_than = tk.Button(
    root,
    text=">",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_greater_than_sign,
    bg=settings_dict["button-bg"],
)
uneq = tk.Button(
    root,
    text="≠",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.write_unequal,
    bg=settings_dict["button-bg"],
)
BackspaceButton = tk.Button(
    root,
    text="←",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.delete,
    bg=settings_dict["button-bg"],
)
ClearButton = tk.Button(
    root,
    text="C",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=commands.clear,
    bg=settings_dict["button-bg"],
)
OFFButton = tk.Button(
    root,
    text="OFF",
    font=(settings_dict["button-font"], settings_dict["button-font-size"]),
    width=6,
    command=root.destroy,
    bg=settings_dict["button-bg"],
)
Copybutton = tk.Button(
    root,
    text="复制结果到剪切板",
    font=("楷体", 30),
    width=20,
    command=commands.answer_copy,
    bg=settings_dict["button-bg"],
)

## 绘制0~9, Clear和+-×÷=←按钮
OneButton.place(y=100, x=100 * 1, anchor="center")
TwoButton.place(y=100, x=100 * 2, anchor="center")
ThreeButton.place(y=100, x=100 * 3, anchor="center")
FourButton.place(y=100, x=100 * 4, anchor="center")
FiveButton.place(y=100, x=100 * 5, anchor="center")
SixButton.place(y=100, x=100 * 6, anchor="center")

SevenButton.place(y=150, x=100 * 1, anchor="center")
EightButton.place(y=150, x=100 * 2, anchor="center")
NineButton.place(y=150, x=100 * 3, anchor="center")
ZeroButton.place(y=150, x=100 * 4, anchor="center")
ZeroZeroButton.place(y=150, x=100 * 5, anchor="center")
DotButton.place(y=150, x=100 * 6, anchor="center")

AddButton.place(y=200, x=100 * 1, anchor="center")
SubtractionButton.place(y=200, x=100 * 2, anchor="center")
MultiplicationButton.place(y=200, x=100 * 3, anchor="center")
DivisionButton.place(y=200, x=100 * 4, anchor="center")
EqualButton.place(y=200, x=100 * 5, anchor="center")
PowerButton.place(y=200, x=100 * 6, anchor="center")

SqrtButton.place(y=250, x=100 * 1, anchor="center")
SinButton.place(y=250, x=100 * 2, anchor="center")
CosButton.place(y=250, x=100 * 3, anchor="center")
TanButton.place(y=250, x=100 * 4, anchor="center")
PiButton.place(y=250, x=100 * 5, anchor="center")
EButton.place(y=250, x=100 * 6, anchor="center")

LeftParenthesisButton.place(y=300, x=100 * 1, anchor="center")
RightParenthesisButton.place(y=300, x=100 * 2, anchor="center")
PlusOrMinus.place(y=300, x=100 * 3, anchor="center")
EqEq.place(y=300, x=100 * 4, anchor="center")
uneq.place(y=300, x=100 * 5, anchor="center")
less_than.place(y=300, x=100 * 6, anchor="center")

less_than_eq.place(y=350, x=100 * 1, anchor="center")
greater_than.place(y=350, x=100 * 2, anchor="center")
greater_than_eq.place(y=350, x=100 * 3, anchor="center")
BackspaceButton.place(y=350, x=100 * 4, anchor="center")
ClearButton.place(y=350, x=100 * 5, anchor="center")
OFFButton.place(y=350, x=100 * 6, anchor="center")

Copybutton.place(y=410, x=350, anchor="center")
root.config(menu=menu_bar, bg=settings_dict["bg"])
# 显示窗口
root.mainloop()
