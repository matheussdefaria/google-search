from googlesearch import search
from tkinter import *
from tkinter import ttk

# Funções

def get_term():
    term = termentry.get()
    return term

def seach_term():
    lista_search = []
    search_term = search(get_term(),num_results=6,lang='pt')
    for item in search_term:
        lista_search.append(item)
    return lista_search
    
def save_arq():
    term = get_term()
    lista = seach_term()
    text = open(f'{term}.txt','w+')
    for x,y in enumerate(range(len(lista))):
        text.write(f'{x + 1} - {lista[y]}\n')

# Interface
root = Tk()
root.title('Search')
root.geometry('200x220')
root.resizable(False,False)
root.config(bg='#A9A9A9')

# Style

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="#A9A9A9",relief='flat', font=('comics sans', 12))
style.map('TButton', background=[('active', '#90EE90')])

titlelabel = ttk.Label(root,text='Google - Search',style='BW.TLabel')
titlelabel.place(width=150, height=20, x = 25, y = 10)

termlabel = Label(root,text='Termo',bg='#A9A9A9')
termlabel.place(width=80,height=20, y = 60)

termentry = ttk.Entry(root)
termentry.place(width=150, height=21, x = 30, y = 86)

botao = ttk.Button(root,text='Pesquisar',command=save_arq)
botao.place(width=100,height=26, x = 50, y = 126)



root.mainloop()