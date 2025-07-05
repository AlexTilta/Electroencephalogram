import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk

# Функция открывающая окно, в котором вводится название файла с данными
def first_scrin():
    # Окно, название, размер, положение на экране, иконка
    root = Tk()
    root.title("Приложение для анализа электроэнцефалограмм")
    w = 460
    h = 150
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    icon = PhotoImage(file = "brain.png")
    root.iconphoto(False, icon)

    # Переменная, записывающее значения из поля ввода entry
    name = StringVar()

    label = ttk.Label(text="Введите название файла с расширением .txt", font=("Arial", 14))
    label.pack(anchor=CENTER, padx=6, pady=12)

    entry = ttk.Entry(textvariable=name)
    entry.pack(ipadx=100, ipady=2, anchor=CENTER, padx=6, pady=6)

    btn = ttk.Button(text="Выбрать файл", command = lambda: root.destroy())
    btn.pack(ipadx=20, ipady=6, anchor=CENTER, padx=6, pady=6)

    root.mainloop()

    return name.get()

# Функция, создающая список из числа столбцов
def setup_data(data, first_line):
    tokens = first_line.split()
    for _ in range(len(tokens)):
        data.append([])

# Функция считывающая данные с файла
def read_file(path_to_file):
    ys = []
    with open(path_to_file) as f:
        n, _, _, fr = f.readline().split()

        for i, line in enumerate(f):
            if line == "":
                continue

            if i == 0:
                setup_data(ys, line)

            next_values = list(map(float, line.split()))

            # Проверка на верность предоставленных данных
            if len(next_values) != len(ys):
                print(f"В строчке #{i + 1} нужно {len(ys)} чисел, а их {len(next_values)}")

            # values - в каждый список кладем по 1 новому значению
            for values, next_value in zip(ys, next_values):
                values.append(next_value)

    return int(n), int(fr), ys

# Построение графиков по номеру коллонки
def graph(x, color):
    x_ax = [i for i in range(0, 200)]
    arr_n = np.array(arr)

    x_time = []
    for i in x_ax:
        x_time.append(i * (1 / 4400))
    plt.xlabel('Time, s')
    plt.ylabel('U, mkV')
    plt.grid()
    plt.plot(x_time[:200], arr_n[x][:200], color)
    plt.show()

# Функция, открывающая окно кнопок для построения графиков
def main_tk():
    # Окно, название, размер, положение на экране, иконка
    root = Tk()
    root.title("Приложение для анализа электроэнцефалограмм")
    w = 500
    h = 300
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    icon = PhotoImage(file = "brain.png")
    root.iconphoto(False, icon)

    # Конфигурация строк и столбцов в окне
    for c in range(2): root.columnconfigure(index=c, weight=1)
    for r in range(3): root.rowconfigure(index=r, weight=1)

    # Создание кнопок
    btn1 = ttk.Button(text="Column 1", command= lambda: graph(0, 'b'))
    btn1.grid(row=0, column=0, ipadx=70, ipady=10, padx=5, pady=5)

    btn2 = ttk.Button(text="Column 2", command=lambda: graph(1, 'g'))
    btn2.grid(row=1, column=0, ipadx=70, ipady=10, padx=5, pady=5)

    btn3 = ttk.Button(text="Column 3", command=lambda: graph(2, 'b'))
    btn3.grid(row=2, column=0, ipadx=70, ipady=10, padx=5, pady=5)

    btn4 = ttk.Button(text="Column 4", command=lambda: graph(3, 'g'))
    btn4.grid(row=0, column=1, ipadx=70, ipady=10, padx=5, pady=5)

    btn5 = ttk.Button(text="Column 5", command=lambda: graph(4, 'b'))
    btn5.grid(row=1, column=1, ipadx=70, ipady=10, padx=5, pady=5)

    btn6 = ttk.Button(text="Column 6", command=lambda: graph(5, 'g'))
    btn6.grid(row=2, column=1, ipadx=70, ipady=10, padx=5, pady=5)

    root.mainloop()

file_name = first_scrin()
N, freq, arr = read_file(file_name) # N, частота оцифровки, массив коллонок из значений y [col1, col2, ...]

main_tk()