from tkinter import *

#Configurações Menu Inicial
m_i = Tk()
m_i.title('Exercite Matemática!')
comp_T = m_i.winfo_screenwidth()
alt_T = m_i.winfo_screenheight()
comp_M = 500
alt_M = 300
inf1 = comp_T/2 - comp_M/2
inf2 = alt_T/2 - alt_M/2 - 50
m_i.geometry('%dx%d+%d+%d'%(comp_M, alt_M, inf1, inf2))
m_i.mainloop()

#Botões