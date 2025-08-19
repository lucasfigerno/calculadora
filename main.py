from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculadora")

# ===== DISPLAY =====
display = Entry(root, font=("Arial", 24), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Função para inserir caracteres no display
def inserir(valor):
    display.insert(END, valor)

# Função para limpar o display
def limpar():
    display.delete(0, END)

# Função para calcular o resultado
def calcular():
    try:
        expressao = display.get()
        resultado = eval(expressao)  # Avalia a expressão digitada
        display.delete(0, END)
        display.insert(END, str(resultado))
    except:
        display.delete(0, END)
        display.insert(END, "Erro")

# ===== BOTÕES NUMÉRICOS =====
botoes = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
]

for (texto, linha, coluna) in botoes:
    if texto == "C":
        cmd = limpar
    else:
        cmd = lambda t=texto: inserir(t)
    Button(root, text=texto, width=5, height=2, font=("Arial", 14), command=cmd).grid(row=linha, column=coluna, padx=2, pady=2, sticky="nsew")

# Botão de igual
Button(root, text="=", width=5, height=2, font=("Arial", 14), command=calcular).grid(row=5, column=0, columnspan=4, padx=2, pady=2, sticky="nsew")

# Ajusta redimensionamento
for i in range(4):
    root.columnconfigure(i, weight=1)
for j in range(6):
    root.rowconfigure(j, weight=1)

root.mainloop()
