import tkinter
from tkinter import filedialog as fd
import networkx as nx
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
# класс модулуля - простой компонент
class SimpleComplement:
    def __init__(self):
        self.root = tkinter.Tk()
        self.fig = Figure(figsize=(7, 7), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.root)
        self.root.wm_title("Simple complement")
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        self.k = 2
        self.ax = self.fig.add_subplot(111)
    def _quit(self):
        self.root.quit()
        self.root.destroy()
    # функция нахождения вершин которые должны быть в состоянии 1
    def _funcFind(self):
        # получаем граф из файла
        S = nx.read_pajek(self.filename)
        # проходим по вершинам
        for node in self.G.nodes():
            # для посчета соседей используем переменную
            val = 0
            for neigb in self.G.neighbors(node):
                # подсчет соседних узлов
                val = val + 1
            # если количество соседних узлов недостаточно, то удаляем с графа вершину
            if val < self.k:
                S.remove_node(node)
            # возвращаем граф
        return S
    def _open(self):
        self.filename = fd.askopenfilename()
        self.G = nx.read_pajek(self.filename)
        self.ax.clear()
        S = self._funcFind()
        color_map = []
        isIn = False
        num = S.number_of_nodes()
        print(S.nodes)
        # проходим по узлам графа
        for node in self.G.nodes():
            for i in range(num):
                # если узел входит в состав графа, то он красный
                if node in S.nodes:
                    isIn=True
                else:
                    isIn=False
            if isIn:
                color_map.append('red')
            else:
                color_map.append('blue')
        nx.draw(self.G, node_color=color_map, with_labels=True, ax=self.ax)
        self.canvas.draw()
    def start(self):
        self.button = tkinter.Button(master=self.root, text="Quit", command=self._quit)
        self.button.pack(side=tkinter.BOTTOM)
        self.button = tkinter.Button(master=self.root, text="Open", command=self._open)
        self.button.pack(side=tkinter.BOTTOM)
        tkinter.mainloop()

if __name__ == '__main__':
    p = SimpleComplement()
    p.start()

