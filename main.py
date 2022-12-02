# Sources: Mr. Cozort

# Fridge Project 2022
# 1 Input Expiration Date and Item
# 2 Add Item to List
# 3 Sort List by Expiration Date
# 4 Visual Component

# using os to create file, using tkinter for window
from tkinter import *
from tkinter import ttk
import uuid
import os
from pathlib import Path

#Create an instance of tkinter frame
win = Tk()
#Set the geometry of tkinter frame
win.geometry("750x400")

fridge = []

#Define a function to show a message
# def myclick():
#    message= "Hello "+ fooditem.get()
#    label= Label(frame, text= message, font= ('Times New Roman', 14, 'italic'))
#    fooditem.delete(0, 'end')
#    label.pack(pady=30)

#Define a function to show a message
def add_item():
   contents = str({"UID":str(uuid.uuid1()), "fooditem": fooditem.get(), "category": category.get(), "ExDate": ExDate.get()})
   label = Label(frame, text= contents, font= ('Times New Roman', 9, 'italic'))
   # fooditem.delete(0, 'end')
   label.pack(pady=30)
   # print current working directory
   # print(Path.cwd())
   # change current working directory
   os.chdir('C:/github')
   # print(Path.cwd())
   dirname = "dataFolder"
   # dirname = str(uuid.uuid1())
   type(dirname)
   if os.path.exists('C:/github/dataFolder'):
      print("folder already exists")
   else:
      os.makedirs('C:/github/' + dirname)
   os.chdir('C:/github/' + dirname)
   # print(Path.cwd())

   # instantiate Path and create file
   # up = str(uuid.uuid1())

   p = Path("data.txt")
   print(p.exists(), 'the file exists...')
   # write content into the file...
   # fridge.append({"UID":uuid.uuid1(), "name": fooditem.get(), "ftype": category.get(), "ExDate": exp_date.get()})
   if not p.exists():
      print("the file didn't exist...") 
      p.write_text(contents)
   # p.write_text(exp_date.get())
   else:
      with p.open('a') as f:
         f.write(contents)

   # print(fridge)
   # # p.read_text()

def sort():
   os.chdir('C:/github')
   # print(Path.cwd())
   dirname = "dataFolder"
   # dirname = str(uuid.uuid1())
   type(dirname)
   if os.path.exists('C:/github/dataFolder'):
      print("folder already exists")
   else:
      os.makedirs('C:/github/' + dirname)
   os.chdir('C:/github/' + dirname)
   # print(Path.cwd())
   p = Path("data.txt")
   print(p)
   sortlist = []
   with p.open("r") as f:
         lines = f.readlines()
         # print(type(lines))
         dobject = ""
         for i in lines:
            for l in i:
               if l == '}':
                  print('BANG')
                  dobject+=l
                  sortlist.append(dobject)
                  dobject = ""
               else:
                  dobject += l
   print(sortlist)
   # for i in sortlist:
   #    print(i)
   #    print(i.ExDate)
   #    print(sortlist.index(i))

#Creates a Frame
frame = LabelFrame(win, width= 400, height= 180, bd=5)
frame.pack()
#Stop the frame from propagating the widget to be shrink or fit
frame.pack_propagate(False)

#Create an Entry widget in the Frame
fooditem= ttk.Entry(frame, width= 40)
fooditem.insert(INSERT, "Enter Food")
fooditem.pack()
category= ttk.Entry(frame, width= 40)
category.insert(INSERT, "Enter Category")
category.pack()
ExDate= ttk.Entry(frame, width= 40)
ExDate.insert(INSERT, "Enter Expiry Date")
ExDate.pack()
#Create a Button
# ttk.Button(win, text= "Click", command= myclick).pack(pady=20)
ttk.Button(win, text= "Add Item", command= add_item).pack(pady=20)
ttk.Button(win, text= "Sort", command = sort).pack(pady=20)
win.mainloop()

# fooditems = {
#   "id" : uuid.uuid1(),
#   "fooditem": fooditem.get(),
#   "category": category.get(),
#   "ExDate": ExDate.get()
# }
