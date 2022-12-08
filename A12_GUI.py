import tkinter as tk
tela = tk.Tk()
tela.title('Empresa do José Carlos de Oliveira Santos')
tela.geometry('700x400')
frame_pr = tk.Frame(master=tela, width= 700, height=400,)
fonte = ('Times',15)
campo_responsavel = tk.Label(master=frame_pr, text = 'Responsavel', font=fonte, width=10, height=2)
entrada_responsavel = tk.Entry(master=frame_pr, width=30, font=fonte)
campo_responsavel.grid(row=0, column=0)
entrada_responsavel.grid(row=0, column=1)

campo_descricao =  tk.Label(master=frame_pr, text='Descrição', font=fonte, width=10, height=2)
entrada_descricao = tk.Entry(master=frame_pr, width=30, font=fonte)
campo_descricao.grid(row=1, column=0)
entrada_descricao.grid(row=1, column=1)
# RESPONSÁVEL, DESCRIÇÃO, ENDEREÇO
frame_pr.pack()
tela.mainloop()