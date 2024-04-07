from tkinter import * 
from contas import *

#Configurações Menu Inicial
m_i = Tk()
m_i.title('Exercite Matemática!')
comp_T = m_i.winfo_screenwidth()
alt_T = m_i.winfo_screenheight()
comp_M = 750
alt_M = 450
inf1 = comp_T/2 - comp_M/2
inf2 = alt_T/2 - alt_M/2 - 50
#m_i.geometry('%dx%d+%d+%d'%(comp_M, alt_M, inf1, inf2))

#frames
frame_botoes = Frame(m_i)
frame_texto_inicial = Frame(m_i)
frame_texto_exercícios = Frame(m_i)

#Textos
label_1 = Label(frame_texto_inicial, text='Escolha seu exercício:', font='bahscript 24')
label_1.grid()
#---


#Botões
btn_soma_i=PhotoImage(file="Imagens\Mais.png")
btn_subtracao_i=PhotoImage(file="Imagens\Menos.png")
btn_multiplicacao_i=PhotoImage(file="Imagens\Vezes.png")
btn_divisao_i=PhotoImage(file="Imagens\Dividido.png")
btn_soma = Button(frame_botoes, image=btn_soma_i, command=soma)
btn_soma.grid(row=1,column=0)
btn_subtracao = Button(frame_botoes, image=btn_subtracao_i, command=subtracao)
btn_subtracao.grid(row=1,column=1)
btn_multiplicacao = Button(frame_botoes, image=btn_multiplicacao_i,command=multiplicacao)
btn_multiplicacao.grid(row=2,column=0)
btn_divisao = Button(frame_botoes, image=btn_divisao_i, command=divisao)
btn_divisao.grid(row=2,column=1)

frame_texto_inicial.grid(row=0,column=0)
frame_botoes.grid(row=1,column=0) 

m_i.mainloop()