import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

notas = []

def nova_nota():
    titulo = entryTitulo.get()
    texto = entryTexto.get("1.0", tk.END).strip()

    if not titulo or not texto:
        messagebox.showerror('Erro', 'Não foi possível salvar a nova nota. Todos os campos devem ser preenchidos.')
        return
    
    notas.append((titulo, texto))
    messagebox.showinfo('Sucesso', 'Nota salva com sucesso!')
    atualizarLista()
    entryTitulo.delete(0, tk.END)
    entryTexto.delete("1.0", tk.END)

def atualizarLista():
    suas_notas.delete(0, tk.END)
    for titulo, _ in notas:
        suas_notas.insert(tk.END, titulo)

def exibir_nota(event):
    selecionado = suas_notas.curselection()
    if selecionado:
        indice = selecionado[0]
        titulo, texto = notas[indice]
        nova_janela = tk.Toplevel(janela_principal)
        nova_janela.title(titulo)
        nova_janela.geometry('400x300')
        tk.Label(nova_janela, text=titulo, font=('Arial', 14, 'bold')).pack(pady=10)
        caixa_texto = tk.Text(nova_janela, font=('Arial', 12), wrap='word', height=10, width=40)
        caixa_texto.pack(pady=10)
        caixa_texto.insert(tk.END, texto)
        caixa_texto.config(state=tk.DISABLED)

janela_principal = tk.Tk()
janela_principal.title('Bloco de notas')
janela_principal.geometry('600x500')

janelinha = ttk.Notebook(janela_principal)
janelinha.grid(column=0, row=0, sticky='nsew')

tela1 = ttk.Frame(janelinha)
tela1.grid_rowconfigure(0, weight=1)
tela1.grid_columnconfigure(0, weight=1)

tela2 = ttk.Frame(janelinha)
tela2.grid_rowconfigure(0, weight=1)
tela2.grid_columnconfigure(0, weight=1)

janelinha.add(tela1, text='Nova nota')
janelinha.add(tela2, text='Suas notas')

Label_titulo = tk.Label(tela1, text='Insira o título', font=('', 10))
Label_titulo.grid(column=0, row=1, sticky='w', pady=15)
entryTitulo = tk.Entry(tela1, font=('', 10), width=50)
entryTitulo.grid(column=0, row=2, sticky='w')

Label_texto = tk.Label(tela1, text='Digite abaixo', font=('', 10))
Label_texto.grid(column=0, row=3, sticky='w', pady=15)
entryTexto = tk.Text(tela1, font=('', 10), width=82, height=15, pady=10, padx=10)
entryTexto.grid(column=0, row=4, sticky='nsew')

tk.Button(tela1, text='Salvar', font=('', 15), command=nova_nota).grid(column=0, row=5, pady=20)

suas_notas = tk.Listbox(tela2, font=('', 10), width=82, height=20)
suas_notas.grid(column=0, row=0, sticky='nsew')
suas_notas.bind('<<ListboxSelect>>', exibir_nota)

janela_principal.mainloop()