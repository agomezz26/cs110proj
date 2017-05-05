import tkinter
from tkinter import *
import question
'''import csv
import json'''


master = Tk()
master.title("Roommate Match")
#master.geometry(("900X900"))
#master.wm_iconbitmap("Troll_Face.ico")

class Questionaire(Frame):	
    def createEntry(self,question):
        Label(master,text=question).grid(row= self.row_count)
        e = Entry(master)
        e.grid(row=self.row_count+1,column=1)
        self.row_count+=2
        

    def create_yesno(self, question):
        var= IntVar()
        column=1
        Label(master, text = question).grid(row = self.row_count)
        Radiobutton(master, text="yes", variable= var, value= 1).grid(row = self.row_count,column = column, sticky = W)
        column+=1
        Radiobutton(master, text="no", variable= var, value= 2).grid(row = self.row_count,column = column, sticky = W)
        self.answer_key[question] = var        
        self.row_count+=1
        

    def multi_choice(self, question):
        var= IntVar()
        column=1
        Label(master, text = question).grid(row = self.row_count)
        Radiobutton(master, text="frequently", variable= var, value= 1).grid(row = self.row_count,column = column, sticky = W)
        column+=1
        Radiobutton(master, text="moderate", variable= var, value= 2).grid(row = self.row_count,column = column, sticky = W)
        column+=1
        Label(master, text = question).grid(row = self.row_count)
        Radiobutton(master, text="never", variable= var, value= 3).grid(row = self.row_count,column = column+2)
        column+=1        
        self.row_count+=1
        

    def multi_answr(self, question):
        var= IntVar()
        column=1
        Label(master, text = question).grid(row = self.row_count)
        Radiobutton(master, text="before 10", variable= var, value= 1).grid(row = self.row_count,column = 1, sticky = W)
        column+=1
        Radiobutton(master, text="10-11", variable= var, value= 2).grid(row = self.row_count,column = 2, sticky = W)
        self.answer_key[question] = var        
        column=1
        Label(master, text = question).grid(row = self.row_count)
        Radiobutton(master, text="11-12", variable= var, value= 3).grid(row = self.row_count,column = 3, sticky = W)
        column+=1
        Radiobutton(master, text="after 12", variable= var, value= 4).grid(row = self.row_count,column = 4, sticky = W)
        column+=1
        self.row_count+=1
        self.answer_key[question] = var
        
    '''def callback():
        peeps = {}
        done = 'n'
        
        while done == 'n':
            peeps.append(name)
        peeps_str = json.dumps(peeps)
        fptr = open('people.json', 'w')
        fptr.write(peeps_str)
        fptr.close()'''
        
    def money(self,question):
        var= IntVar()
        column=1
        Label(master, text = question).grid(row = self.row_count)
        Radiobutton(master, text="200-400", variable= var, value= 1).grid(row = self.row_count,column = 1, sticky = W)
        column+=1
        Radiobutton(master, text="400-600", variable= var, value= 2).grid(row = self.row_count,column = 2, sticky = W)
        column+=1
        Label(master, text = question).grid(row = self.row_count)
        Radiobutton(master, text="600-800", variable= var, value= 3).grid(row = self.row_count,column = 3, sticky = W)
        column+=1
        Radiobutton(master, text="800+", variable= var, value= 4).grid(row = self.row_count,column = 4, sticky = W)
        self.answer_key[question] = var

 #   def createWidgets(self):
 #       Button(master, text= "Quit", command=master.quit).grid(row= self.row_count, sticky=W, pady=4)
 #       Button(master, text= "Submit", command= Questionaire.callback()).grid(row= self.row_count, column=2)


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.row_count=5
 #       self.createWidgets()
        self.answer_key = {}

q_sheet = Questionaire()

for i in question.fill_in().fq:
    q_sheet.createEntry(i)
for i in question.ynquestions().qs:
    q_sheet.create_yesno(i)
for i in question.multquestions().mq:
    q_sheet.multi_choice(i)
for i in question.mult_answer().mas:
    q_sheet.multi_answr(i)
for i in question.rent_q().mo:
    q_sheet.money(i)


'''csvfile = open('.csv', 'r')
jsonfile = open('people.json', 'w')
fieldnames = ("FirstName","LastName","IDNumber","Message")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')'''
       
master.mainloop()
