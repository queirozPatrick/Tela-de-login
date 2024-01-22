from tkinter import *
from tkinter import ttk

# cores

co0 = "#f0f3f5" # Preto / Black
co1 = "#feffff" # Branco / White
co2 = "#3fb5a3" # Verde / Green
co3 = "#38576b" # Valor / Value
co4 = "#403d3d" # Letra / Letters

# criando a janela
janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

# dividindo a janela
frame_cima = Frame(janela, width=310, height=50, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=250, bg=co2, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

janela.mainloop()