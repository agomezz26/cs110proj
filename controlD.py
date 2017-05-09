import tkinter
from tkinter import *
import json


master = Tk()
master.title("Roommate Match")

class Questionaire(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.row_count=5
        self.createWidgets()
        self.answer_key = {}	
       
    def createEntry(self,question):
        Label(master,text=question).grid(row= self.row_count)
        e = Entry(master)
        e.grid(row=self.row_count+1,column=1)
        self.row_count+=2


    def callback():
        """num = 0
        num+=1"""
        peeps = {}
        peeps["response"] = (E1.get(), E2.get(), E3.get(), E4.get(), E5.get(), E6.get(), E7.get(), E8.get(), E9.get(), E10.get())
        '''
        peeps.append(E1.get())
        peeps.append(E2.get())
        peeps.append(E3.get())
        peeps.append(E4.get())
        peeps.append(E5.get())
        peeps.append(E6.get())
        peeps.append(E7.get())
        peeps.append(E8.get())
        peeps.append(E9.get())
        peeps.append(E10.get())
        peeps_str = json.dump(peeps, fptr)'''
        fptr = open('people.json', 'a')
        peeps_str = json.dump(peeps, fptr)
  #      fptr.write(peeps_str)
        fptr.close()

    def createWidgets(self):
        
        MyButton1 = Button(master, text="Submit", width=10, command=Questionaire.callback)
        MyButton1.grid(row=11, column=1)

    
q_sheet = Questionaire()

L1 = Label(master, text='Are you willing/expecting to share personal items such as clothes, cleaning supplies, etc?, (y or n)')
L1.grid(row=0, column=0)
E1 = Entry(master, bd = 5)
E1.grid(row=0, column=1)

L2 = Label(master, text='Which do you prefer?,(a) Quiet living space,(b) Noisy living space, (c) Some combination of the two')
L2.grid(row=1, column=0)
E2 = Entry(master, bd = 5)
E2.grid(row=1, column=1)

L3 = Label(master, text='Do you have and/or want pets?, (y or n)')
L3.grid(row=2, column=0)
E3 = Entry(master, bd = 5)
E3.grid(row=2, column=1)

L4 = Label(master, text='At about what hour do you go to sleep?,(a)10,(b)11,(c)12,(d)1') 
L4.grid(row=3, column=0)
E4 = Entry(master, bd = 5)
E4.grid(row=3, column=1)

L5 = Label(master, text='At about what hour do you wake up?,(a)7,(b)8,(c)9,(d)10')
L5.grid(row=4, column=0)
E5 = Entry(master, bd = 5)
E5.grid(row=4, column=1)

L6 = Label(master, text='Do you smoke?, (y or n)')
L6.grid(row=5, column=0)
E6 = Entry(master, bd = 5)
E6.grid(row=5, column=1)

L7 = Label(master, text='Do you have a significant other? If no, do you plan on having over night guests of any kind?, (y or n)')
L7.grid(row=6, column=0)
E7 = Entry(master, bd = 5)
E7.grid(row=6, column=1)

L8 = Label(master, text='Which desribes you best?,(a)Complete mess,(b)Sometimes messy but relatively organized,(c) Pretty Tidy,(d)Neat Freak')
L8.grid(row=7, column=0)
E8 = Entry(master, bd = 5)
E8.grid(row=7, column=1)

L9 = Label(master, text='Do you mind if your roommate has frequent over night guests?, (y or n)')
L9.grid(row=8, column=0)
E9 = Entry(master, bd = 5)
E9.grid(row=8, column=1)

L10 = Label(master, text='Where would you like to live?,(a)Near a big city,(b)Suburbs,(c)Rural area')
L10.grid(row=9, column=0)
E10 = Entry(master, bd = 5)
E10.grid(row=9, column=1)

master.mainloop()
