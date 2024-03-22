from tkinter import * 
#from contas import *

#Configurações Menu Inicial
m_i = Tk()
m_i.title('Exercite Matemática!')
comp_T = m_i.winfo_screenwidth()
alt_T = m_i.winfo_screenheight()
comp_M = 750
alt_M = 450
inf1 = comp_T/2 - comp_M/2
inf2 = alt_T/2 - alt_M/2 - 50
m_i.geometry('%dx%d+%d+%d'%(comp_M, alt_M, inf1, inf2))

#Frames e Labels
#label_1 = Label(m_i, text='Escolha seu exercício:', font='bahscript 24', bd=3)
#label_1.grid(row=0, column=0)
#Botões
btn_soma_i=PhotoImage(file="Imagens\Mais.png")
btn_subtracao_i=PhotoImage(file="Imagens\Menos.png")
btn_multiplicacao_i=PhotoImage(file="Imagens\Vezes.png")
btn_divisao_i=PhotoImage(file="Imagens\Dividido.png")
btn_soma = Button(m_i, image=btn_soma_i)
btn_soma.grid(row=1,column=0)
btn_subtracao = Button(m_i, image=btn_subtracao_i)
btn_subtracao.grid(row=1,column=1)
btn_multiplicacao = Button(m_i, image=btn_multiplicacao_i)
btn_multiplicacao.grid(row=2,column=0)
btn_divisao = Button(m_i, image=btn_divisao_i)
btn_divisao.grid(row=2,column=1)

 

m_i.mainloop()