import tkinter as tk
tela = tk.Tk()
tela.title('Empresa do José Carlos de Oliveira Santos')
tela.geometry('700x400')
frame_pr = tk.Frame(master=tela, width= 600, height=300)
fonte = ('Times',15)
campo_responsavel = tk.Label(master=frame_pr, text = 'Responsavel', font=fonte, width=20, height=20)
entrada_responsavel = tk.Entry(master=frame_pr, width=70, font=fonte)
campo_responsavel.grid(row=0, column=0)
entrada_responsavel.grid(row=0, column=1)

frame_pr.pack()
tela.mainloop()