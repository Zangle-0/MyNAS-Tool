import tkinter as tk

# 创建一个窗口对象
root = tk.Tk()
root.title("欢迎窗口")

# 创建一个文本输入框对象
entry = tk.Entry(root)
entry.pack()

# 创建一个提交按钮对象
button = tk.Button(root, text="提交")
button.pack()

# 进入窗口消息循环
root.mainloop()
