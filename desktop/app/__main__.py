import tkinter as tk

class CashRegisterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registratore di Cassa")

        # Variabile per tenere traccia del totale
        self.total = 0

        # Frame per l'area a sinistra
        self.left_frame = LeftFrame(self)

        # Frame per l'area a destra
        self.right_frame = RightFrame(self)

        # Etichetta per visualizzare il totale
        self.total_label = tk.Label(self.left_frame, text="Totale: 0")
        self.total_label.pack()

        # Lista di importi per i pulsanti
        self.prices = [1, 2, 5, 10, 20, 50]

        # Creazione dei pulsanti
        for price in self.prices:
            btn = Button(self.right_frame, type='category', text=f"+{price}", command=lambda p=price: self.add_to_total(p))
            btn.pack(pady=5)

    def add_to_total(self, price):
        # Aggiungi l'importo al totale
        self.total += price
        # Aggiorna l'etichetta del totale
        self.total_label.config(text=f"Totale: {self.total}")
        
class Button(tk.Button):
    def __init__(self, master, type, **kwargs):
        super().__init__(master, **kwargs)
        self.config(font=("Arial", 12), width=10, height=2)
        
        if type == 'table':
            self.config(bg="blue")
        elif type == 'category':
            self.config(bg="green")
        elif type == 'product':
            self.config(bg="red")
            
class RightFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.config(bg="yellow")
        self.place(relx=0.4, rely=0, relwidth=0.6, relheight=1)
        
class LeftFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.config(bg="blue")
        self.place(relx=0, rely=0, relwidth=0.4, relheight=1)

if __name__ == "__main__":
    app = CashRegisterApp()
    app.mainloop()
