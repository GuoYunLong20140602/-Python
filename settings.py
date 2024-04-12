import json
import tkinter as tk


class Settings:
    def __init__(self):
        with open(r"./calc_settings.json", encoding="UTF-8") as f:
            self.settings_dict = json.load(f)

        root = tk.Tk()
        root.config(bg=self.settings_dict["bg"])
        root.geometry("670x610+150+150")
        root.title("计算器v6.0-设置")
        contents = self.settings_dict.keys()
        # contents = [
        #     "expression-font",
        #     "expression-font-size",
        #     "expression-bg",
        #     "bg",
        #     "button-font",
        #     "button-font-size",
        #     "button-bg",
        #     "settings-bg",
        #     "settings-font",
        #     "settings-font-size",
        #     "settings-font-fg",
        #      ...
        # ]
        for c in contents:
            tk.Label(
                root,
                font=(
                    self.settings_dict["settings-font"],
                    self.settings_dict["settings-font-size"],
                ),
                text=c + ":",
                fg=self.settings_dict["settings-font-fg"],
                bg=self.settings_dict["settings-bg"],
                justify="left",
            ).grid(row=list(contents).index(c) + 1, column=1)
        variables = [tk.StringVar().set(str(i)) for i in self.settings_dict.values()]
        variables = []
        for i in self.settings_dict.values():
            # print(i)
            j = tk.StringVar()
            j.set(str(i))

            variables.append(j)
        # print(variables)
        expression_font = tk.Entry(
            root,
            font=(
                self.settings_dict["settings-font"],
                self.settings_dict["settings-font-size"],
            ),
            textvariable=variables[list(contents).index("expression-font")],
            bg=self.settings_dict["settings-bg"],
            fg=self.settings_dict["settings-font-fg"],
        )

        expression_font_size = tk.Entry(
            root,
            font=(
                self.settings_dict["settings-font"],
                self.settings_dict["settings-font-size"],
            ),
            textvariable=variables[list(contents).index("expression-font-size")],
            bg=self.settings_dict["settings-bg"],
            fg=self.settings_dict["settings-font-fg"],
        )
        expression_bg = tk.Entry(
            root,
            font=(
                self.settings_dict["settings-font"],
                self.settings_dict["settings-font-size"],
            ),
            textvariable=variables[list(contents).index("expression-bg")],
            bg=self.settings_dict["settings-bg"],
            fg=self.settings_dict["settings-font-fg"],
        )
        expression_fg = tk.Entry(
            root,
            font=(
                self.settings_dict["settings-font"],
                self.settings_dict["settings-font-size"],
            ),
            textvariable=variables[list(contents).index("expression-fg")],
            bg=self.settings_dict["settings-bg"],
            fg=self.settings_dict["settings-font-fg"],
        )
        bg = tk.Entry(
            root,
            font=(
                self.settings_dict["settings-font"],
                self.settings_dict["settings-font-size"],
            ),
            textvariable=variables[list(contents).index("bg")],
            bg=self.settings_dict["settings-bg"],
            fg=self.settings_dict["settings-font-fg"],
        )
        button_font = tk.Entry(
            root,
            font=(
                self.settings_dict["settings-font"],
                self.settings_dict["settings-font-size"],
            ),
            textvariable=variables[list(contents).index("button-font")],
            bg=self.settings_dict["settings-bg"],
            fg=self.settings_dict["settings-font-fg"],
        )
        button_font_size = tk.Entry(
            root,
            font=(
                self.settings_dict["settings-font"],
                self.settings_dict["settings-font-size"],
            ),
            textvariable=variables[list(contents).index("button-font-size")],
            bg=self.settings_dict["settings-bg"],
            fg=self.settings_dict["settings-font-fg"],
        )
        button_bg = tk.Entry(
            root,
            font=(
                self.settings_dict["settings-font"],
                self.settings_dict["settings-font-size"],
            ),
            textvariable=variables[list(contents).index("button-bg")],
            bg=self.settings_dict["settings-bg"],
            fg=self.settings_dict["settings-font-fg"],
        )
        button_fg = tk.Entry(
            root,
            font=(
                self.settings_dict["settings-font"],
                self.settings_dict["settings-font-size"],
            ),
            textvariable=variables[list(contents).index("button-fg")],
            bg=self.settings_dict["settings-bg"],
            fg=self.settings_dict["settings-font-fg"],
        )
        settings_font = tk.Entry(
            root,
            font=(
                self.settings_dict["settings-font"],
                self.settings_dict["settings-font-size"],
            ),
            textvariable=variables[list(contents).index("settings-font")],
            bg=self.settings_dict["settings-bg"],
            fg=self.settings_dict["settings-font-fg"],
        )
        settings_font_size = tk.Entry(
            root,
            font=(
                self.settings_dict["settings-font"],
                self.settings_dict["settings-font-size"],
            ),
            textvariable=variables[list(contents).index("settings-font-size")],
            bg=self.settings_dict["settings-bg"],
            fg=self.settings_dict["settings-font-fg"],
        )
        settings_bg = tk.Entry(
            root,
            font=(
                self.settings_dict["settings-font"],
                self.settings_dict["settings-font-size"],
            ),
            textvariable=variables[list(contents).index("settings-bg")],
            bg=self.settings_dict["settings-bg"],
            fg=self.settings_dict["settings-font-fg"],
        )
        settings_font_fg = tk.Entry(
            root,
            font=(
                self.settings_dict["settings-font"],
                self.settings_dict["settings-font-size"],
            ),
            textvariable=variables[list(contents).index("settings-font-fg")],
            bg=self.settings_dict["settings-bg"],
            fg=self.settings_dict["settings-font-fg"],
        )
        float_bit = tk.Entry(
            root,
            font=(
                self.settings_dict["settings-font"],
                self.settings_dict["settings-font-size"],
            ),
            textvariable=variables[list(contents).index("float-bit")],
            bg=self.settings_dict["settings-bg"],
            fg=self.settings_dict["settings-font-fg"],
        )
        expression_font.grid(row=1, column=2)
        expression_font_size.grid(row=2, column=2)
        expression_bg.grid(row=3, column=2)
        expression_fg.grid(row=4, column=2)
        bg.grid(row=5, column=2)
        button_font.grid(row=6, column=2)
        button_font_size.grid(row=7, column=2)
        button_bg.grid(row=8, column=2)
        button_fg.grid(row=9, column=2)
        settings_font.grid(row=10, column=2)
        settings_font_size.grid(row=11, column=2)
        settings_font_fg.grid(row=12, column=2)
        settings_bg.grid(row=13, column=2)
        float_bit.grid(row=14, column=2)

        def save():
            if expression_font.get():
                self.settings_dict["expression-font"] = expression_font.get()
            if expression_font_size.get():
                self.settings_dict["expression-font-size"] = expression_font_size.get()
            if expression_bg.get():
                self.settings_dict["expression-bg"] = expression_bg.get()
            if expression_fg.get():
                self.settings_dict["expression-fg"] = expression_fg.get()
            if bg.get():
                self.settings_dict["bg"] = bg.get()
            if button_font.get():
                self.settings_dict["button-font"] = button_font.get()
            if button_font_size.get():
                self.settings_dict["button-font-size"] = button_font_size.get()
            if button_bg.get():
                self.settings_dict["button-bg"] = button_bg.get()
            if button_fg.get():
                self.settings_dict["button-fg"] = button_bg.get()
            if settings_font.get():
                self.settings_dict["settings-font"] = settings_font.get()
            if settings_font_size.get():
                self.settings_dict["settings-font-size"] = settings_font_size.get()
            if settings_font_fg.get():
                self.settings_dict["settings-font-fg"] = settings_font_fg.get()
            if settings_bg.get():
                self.settings_dict["settings-bg"] = settings_bg.get()
            if float_bit.get():
                self.settings_dict["float-bit"] = float_bit.get()
            # print(self.settings_dict)
            data = json.dumps(self.settings_dict)
            with open(r"./calc_settings.json", "w", encoding="UTF-8") as f:
                f.write(data)

        tk.Button(
            root,
            command=save,
            font=(
                self.settings_dict["settings-font"],
                self.settings_dict["settings-font-size"],
            ),
            text="保存",
        ).grid(row=16, column=1)

        root.mainloop()
