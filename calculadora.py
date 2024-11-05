import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("CALCULATOR")
        self.root.configure(bg='#2d8a99')

        self.pantalla = tk.Entry(self.root, width=50, bg='#3b4b5b', borderwidth=5, fg='white')
        self.pantalla.grid(row=0, column=0, padx=5, pady=10, columnspan=4)

        self.crear_botones()

    def crear_botones(self):
        botones = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('7', 3, 0),
            ('8', 3, 1), ('9', 3, 2), ('0', 4, 0), ('+', 1, 3), ('-', 2, 3), ('*', 3, 3),
            ('/', 4, 3), ('=', 4, 1), ('C', 4, 2),
        ]

        for (text, row, col) in botones:
            button = tk.Button(self.root, text=text, padx=30, pady=30, bg='#4b5b6b', fg='white', command=lambda t=text: self.boton_click(t))
            button.grid(row=row, column=col)

    def boton_click(self, valor):
        if valor == "=":
            try:
                result = str(eval(self.pantalla.get()))
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, result)
            except:
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, "Error")
        elif valor == "C":
            self.pantalla.delete(0, tk.END)
        else:
            self.pantalla.insert(tk.END, valor)

root = tk.Tk()
calculadora = Calculadora(root)
root.mainloop()
